class Config:
    SECRET_KEY = 'mysecretkey'          #esto es para que funcione "flash()"

class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = ''
    MYSQL_DB = 'flaskcontacts'
    MYSQL_UNIX_SOCKET = '/opt/lampp/var/mysql/mysql.sock' #aca tuve problemas y esta linea la tuve que agregar, PORQUE DE LOS EJEMPLOS NO DECIA NADA
                                                            #ESTO ESTABA DIRECTO EN APP.PY

config = {
    'development': DevelopmentConfig
}                                                        