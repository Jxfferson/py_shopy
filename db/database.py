from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

#conection string:
#Cadena de conexión que representa la BD a conectarse 
#Depende de la BD que se use y el lenguaje de programación
SQLALCHEMY_DATABASE_URL="mysql+pymysql://root:admin@localhost:3315/py-shopy"

#Crear el objeto que nos permitira ingresar a la BD
conn = create_engine(SQLALCHEMY_DATABASE_URL)


#Clase base para los modelos
Base = declarative_base()