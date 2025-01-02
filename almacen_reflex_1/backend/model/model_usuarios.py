import reflex as rx
from typing import Optional
from sqlmodel import Field

# la clase tiene que llamarse iguar que la tabla de la que modela los datos


class Usuarios(rx.Model, table=True):
    idusuario: Optional[int] = Field(default=None, primary_key=True)
    codigo_operador: str
    password: str
    perfil: str
