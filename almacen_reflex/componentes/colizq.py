import reflex as rx
from almacen_reflex.componentes.sidebar import sidebar


def colizq() -> rx.Component:
    return rx.stack(        
    sidebar(),
)


