import reflex as rx
from almacen_reflex.componentes.botones import menu_boton

def colcen() -> rx.Component:
    return rx.vstack(
        menu_boton("",""),
            width="100%",
            height="93vh",
            max_heigth="100%",
            max_width="100%",
            padding="2px",            
            background_color= "white",
            align="center"
            
    )