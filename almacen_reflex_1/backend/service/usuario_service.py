"""
Métodos de servicio.Es decir son los 
métodos que pasan la información a 
nuestras páginas.
"""
from ..repository.usuario_repository import seleccion_todos
from ..model.model_usuarios import Usuarios

# metodos que ya sirven la informacion a nuestras páaginas
# Aquí tambien se hace la lógica de negocio.
# así como las validaciones.


def seleccion_todos_usuarios_service():
    try:
        usuarios = seleccion_todos()
        print(usuarios)
        return usuarios
    except Exception as e:
        print("Error obteniendo usuarios:{e}")
        return []
