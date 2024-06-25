# Creamos esta clase porque necesitamos CREAR USUARIOS
# y crear Entidades dentro de BASE DE DATOS

# y ademas para gestionar las autenticaciones

# y ademas vamos a usar un metodo para poder CHEQUEAR EL PASSWORD

from werkzeug.security import check_password_hash #generate_password_hash #generate_password_hash ESTO ES NECESARIO PARA CREAR MANUALMENTE UN HASH , para un usuario USUARIO
from flask_login import UserMixin                   #esto es para que la instancia de la clase User herede de UserMixin

class User(UserMixin):
    def __init__(self, id, username, password, fullname="") -> None:
        self.id = id
        self.username = username
        self.password = password
        self.fullname = fullname

    @classmethod                                        #esto me sirve para usar el metodo sin necesidad de instanciar la clase
    def check_password(self, hashed_password, password): #un parametro es el "hasheado" otro parametro es texto plano
        return check_password_hash(hashed_password, password) #me devuelve lo que la funcion nos indica
    
#print(generate_password_hash("facil")) esto fue solo para crear usuario Angel con la contraseña "facil" que luego se guarda hasheada