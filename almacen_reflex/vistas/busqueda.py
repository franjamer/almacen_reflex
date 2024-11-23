import reflex as rx
from almacen_reflex.componentes.paginaPrincipal import paginaPrincipal
def vista_busqueda():
    rx.box(        
        rx.center(
            rx.vstack(
                paginaPrincipal(),
                rx.hstack(
                    rx.text("vista busqueda")
                ),
            )
        )
    )