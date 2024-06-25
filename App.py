from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
from flask_bootstrap import Bootstrap
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager, login_user, logout_user, login_required  #manejador de login, con login/logout para que tmb los maneje, y required para que CIERTAS RUTAS estas se accedan luego de loguearse

from config import config

#Models:
from models.ModelUser import ModelUser

#Entities:
from models.entities.User import User

app = Flask(__name__)

bootstrap = Bootstrap(app)

#conexion a mysql
#app.config['MYSQL_HOST'] = 'localhost'
#app.config['MYSQL_USER'] = 'root'
#app.config['MYSQL_PASSWORD'] = ''
#app.config['MYSQL_DB'] = 'flaskcontacts'
#app.config['MYSQL_UNIX_SOCKET'] = '/opt/lampp/var/mysql/mysql.sock' #aca tuve problemas y esta linea la tuve que agregar, PORQUE DE LOS EJEMPLOS NO DECIA NADA

csrf = CSRFProtect(app)  #por lo que vi no hay que pasarle como parametro a la "app", si hay que indicar dentro del MAIN que la inicie la app

mysql = MySQL(app)

login_manager_app = LoginManager(app)
    #esto es para manejar los logins como un constructor

#settings                       = esto fue antes del "config.py"
#app.secret_key = 'mysecretkey'

@login_manager_app.user_loader
def load_user(id):
    return ModelUser.get_by_id(mysql, id) 

    #user_loader = metodo que se tiene que crear para que luego de iniciar sesion TOME LOS DATOS DEL USUARIO
    #y usamos el ModelUser de nuevo para obtener mediante "id" los datos del usuario

@app.route('/')
def Index():
    return redirect(url_for('login'))

#@app.route('/')                            RAIZ SIN LOGIN
#def Index():
#    cur = mysql.connection.cursor()
#    cur.execute('SELECT * FROM contacts')
#    data = cur.fetchall()
#    return render_template('index.html', contacts = data)

@app.route('/login', methods=['GET','POST']) 
def login():                                 #Ésta "def" se tiene que llamar "index()" simplemente?
    if request.method == 'POST':
        user = User(0, request.form['username'], request.form['password']) #ponemos NADA en "fullname" porque de primeras se lo pusimos asi por defecto
        logged_user = ModelUser.login(mysql, user)                          #puede ser NONE si no existe o el usuario logueado
        if logged_user != None:
            #ahora aca dentro comprobar si el password existe o no
            if logged_user.password:
                login_user(logged_user) #esto es para que lo reciba como usuario logueado en la HOME
                return redirect(url_for('protected'))
            else:
                flash("Password invalido ...")
                return render_template('auth/login.html')    
        else:
            flash("Usuario no encontrado ...")
            return render_template('auth/login.html')
    else:
        return render_template('auth/login.html') #aca lo que estamos haciendo es redirigir al login SI INGRESO CON METODO "GET"
    

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/add_contact', methods=['POST'])
@login_required
def add_contact():
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO contacts (fullname, phone, email) VALUES (%s, %s, %s)', 
                    (fullname, phone, email))
        mysql.connection.commit()
        flash('Contacto agregado con exito')
        return redirect(url_for('protected')) #aca tuve problemas porque por mas que index.html se tiene que poner Index

@app.route('/edit/<id>')
@login_required
def get_contact(id):  
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM contacts WHERE id = %s', (id,))
    data = cur.fetchall()
    return render_template('edit-contact.html', contact = data[0]) #aca va el nombre completo dentro del render_template, tene cuidado con eso

@app.route('/update/<id>', methods = ['POST'])
@login_required
def update_contact(id):
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE contacts
            SET fullname = %s,
                phone = %s,
                email = %s
            WHERE id = %s
        """, (fullname, phone, email, id,))
        mysql.connection.commit()
        flash('contacto actualizado satisfactoriamente')
        return redirect(url_for('protected'))

@app.route('/delete/<string:id>')
@login_required
def delete_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM contacts WHERE id = {0}'.format(id))
    mysql.connection.commit()
    flash('contacto removido satisfactoriamente')
    return redirect(url_for('protected'))

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/protected')            #este era el antiguo index
@login_required
def protected():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM contacts')
    data = cur.fetchall()
    return render_template('index.html', contacts = data)
    #return "<h1> Vista protegida, usuarios logueados. Aca tiene que estar la vista INGRESAR CONTACTOS </h1> "

def status_401(error):                  #en caso de no estar autorizado el error lo maneja asi:
    return redirect(url_for('login'))

def status_404(error):                  #en caso de que la pagina o vista que no exista
    return "<h1> Pagina no encontrada </h1>", 404

                                        #errores que TENGO REGISTRARLO EN EL MAIN de App.py

if __name__ == '__main__':
    app.config.from_object(config['development']) # = ESTO ES NECESARIO PARA config.py
    csrf.init_app(app)                              #inicia la app con la proteccion, pero en login tenemos que agregar "input en hidden"
    app.register_error_handler(401, status_401)
    app.register_error_handler(404, status_404)
    app.run(port = 3000) #, debug=True              = ANTES DEL "CONFIG.PY"
