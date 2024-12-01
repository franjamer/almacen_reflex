"""
PÁGINA PRINCIPAL DE LA TABLA USER

Aquí se muestran todas las variables de estado,
métodos y procedimientos que actuarán directamente
en la página web.
"""

import reflex as rx
from .model import Usuarios
from .service.usuario_service import seleccion_todos_usuarios_service
import asyncio

""" PÁGINA DE USUARIOS """


class UsuarioEstado(rx.State):
    # Variables de estado
    usuarios: list[Usuarios] = []
    buscar_usuario: str = ""
    error_message: str = ""
    error: str = ""

    @rx.event(background=True)
    async def conseguir_todos_usuarios(self):
        """Obtiene todos los usuarios desde el servicio y los almacena en la lista de usuarios."""
        async with self:
            try:
                usuarios = seleccion_todos_usuarios_service()
                self.usuarios = [usuario for usuario in usuarios]
            except Exception as e:
                self.error_message = f"Error al obtener usuarios: {e}"
                self.error = str(e)
                print(error_message)


def buscar_on_change(self, valor: str):
    """Actualiza el estado de búsqueda."""
    self.buscar_usuario = valor


@rx.page(route="/usuarios", title="Usuarios", on_load=UsuarioEstado.conseguir_todos_usuarios)
def user_page() -> rx.Component:
    """Genera la página principal de usuarios."""
    return rx.flex(
        rx.heading("Usuarios", align="center"),
        # Puedes habilitar las funcionalidades de búsqueda y creación más adelante.
        # rx.hstack(
        #     buscar_usuario_component(),
        #     create_user_dialogo_component(),
        #     justify="center",
        #     style={"margin-top": "30px"}
        # ),
        table_use(UsuarioEstado.usuarios),
        # Mostrar errores si existen
        rx.cond(
            UsuarioEstado.error != "",
            rx.box(
                title="Error",
                description=UsuarioEstado.error_message,
                status="error",
                variant="left-accent",
            ),
        ),
        direction="column",
        style={"width": "50vw", "margin": "auto", "background_color": "gray"},
    )


def table_use(list_user: list[Usuarios]) -> rx.Component:
    """Genera la tabla para mostrar la lista de usuarios."""
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell("Código Usuario"),
                rx.table.column_header_cell("Perfil"),
                rx.table.column_header_cell("Acción"),
            )
        ),
        rx.table.body(
            rx.foreach(
                list_user,
                row_table,  # Usa row_table para evitar duplicar lógica
            ),
        ),
    )


def row_table(usuario: Usuarios) -> rx.Component:
    """Genera una fila de la tabla con los datos de un usuario."""
    return rx.table.row(
        rx.table.cell(usuario.codigo_operador),
        rx.table.cell(usuario.perfil),
        rx.table.cell(
            rx.hstack(
                rx.button("Eliminar"),
            )
        ),
    )
