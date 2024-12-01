""" Métodos que interactuan con la base de datos."""

# Importamos todo lo que necesitamos.

from ..model.model_usuarios import Usuarios
from .conexion_db import conecta
from sqlmodel import Session, select


# Este método seleciona todos los elementos de la tabla que
# estamos utilizando de nuestra base de datos.

def seleccion_todos():
    # Conexión a la base de datos
    motor = conecta()
    # manejo de contexto.
    # Abrimos sesion
    with Session(motor) as session:
        # Ejecutamos la consulta para obtener todos los usuarios
        # La siguiente linea es equivalente a "SELECT * FROM Usuario"
        query = select(Usuarios)
        # devuelve una lista de todos los usuarios
        # que tengamos en nuestra tabla Usuario
        # y cerramos sesion
        # con esta linea verificamos en consola, si estamos trayendo los datos correctamente.
        print(query)

        return session.exec(query).all()
