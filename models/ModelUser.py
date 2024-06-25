from .entities.User import User

      
class ModelUser():

    @classmethod                   #y esto tambien lo ponemos como CLASSMETHOD = PORQUE NECESITAMOS USARLO SIN LA NECESIDAD DE INSTANCIAR "MODEL USER"
    def login(self, mysql, user):  #en esta funcion vamos a mandar BASE DE DATOS Y USUARIO, para autenticar
        try:
            cursor = mysql.connection.cursor()
            sql = """SELECT id, username, password, fullname FROM user
                        WHERE username = '{}'""".format(user.username)   #vamos a listar si es que existe el usuario, sino existe no tiene sentido buscar la contraseña
            cursor.execute(sql)
            row = cursor.fetchone() #aca queremos tener una FILA que sea el resultado de lo que ejecutamos arriba
            if row != None:         #aca si encontramos un USER que existe JOYA
                user = User(row[0], row[1], User.check_password(row[2], user.password), row[3]) #creamos objetos tipo User y le pasamos los parametros que el OBJETO NECESITA
                                                                                                #todos los parametros los conocemos y se lo pasamos PERO...
                                                                                                #el PASSWORD lo que queremos hacer es pasarlo por la funcion para que lo hashee y compruebe entre el HASH y el PASSWORD PLANO                                                                                              
                return user
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
        
    
    @classmethod   
    def get_by_id(self, mysql, id):
        try:
            cursor = mysql.connection.cursor()
            sql = """SELECT id, username, fullname FROM user WHERE id = '{}'""".format(id)   #password no porque el usuario aca ya esta logueado
            cursor.execute(sql)
            row = cursor.fetchone() 
            if row != None:         
                logged_user = User(row[0], row[1], None, row[2]) #aca no hace el password y fullname esta en posicion 2
                return logged_user
            else:
                return None
        except Exception as ex:
            raise Exception(ex)