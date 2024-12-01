"""Creación de la conexion a la base de datos"""
# from sqlmodel import create_engine as crear_motor
from sqlalchemy import create_engine as crear_motor


def conecta():
    # Configuración del motor de conexión a la base de datos
    username = "root"
    password = "root"
    host = "localhost:3306"
    database = "almacenrepuestos"

    return crear_motor(f"mysql+pymysql://{username}:{password}@{host}/{database}")


# Va a tener los datos de conexion con la base de datos
# Instrucciones de sqlmodel
# para mysql la libreria a importar es pymysql
