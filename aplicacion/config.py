import os

SECRET_KEY = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
PWD = os.path.abspath(os.curdir)

DEBUG = True # En despliegue esto pasa a FALSE
#SQLALCHEMY_DATABASE_URI = 'sqlite:///{}/dbase.db'.format(PWD)
#SQLALCHEMY_TRACK_MODIFICATIONS = False

# Ejemplo basico de postgresql
# Comparalo con ejemplo de Mysql
SQLALCHEMY_DATABASE_URI= 'postgresql://aplicacion_despliegue_user:q62zOdprL3ZTvXyhcEjIOqDZWYY77wJ7@dpg-cu1vo78gph6c73elqh40-a.frankfurt-postgres.render.com/aplicacion_despliegue'
SQLALCHEMY_TRACK_MODIFICATIONS = False

