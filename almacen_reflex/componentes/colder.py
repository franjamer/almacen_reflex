import reflex as rx
from almacen_reflex.componentes.botones import menu_boton

def colder() -> rx.Component:
    return rx.vstack(
        
                menu_boton("Movimientos","movimientos"),
                menu_boton("Inventario","inventario"),
                menu_boton("Home",""),
                background_color= "white",
                width="6vw",
                height="93vh",
                max_heigth="100%",                
                align="end"            
            )

def Movimientos():
    return rx.vstack(
        rx.text("Pagina Movimientos"),
            rx.button(
                "Página Principal",
                on_click=rx.redirect(
                "/"
            ),
        ),
    
    )      

def Inventario():
    return rx.vstack(
        rx.text("Pagina Inventario"),
            rx.button(
                "Página Principal",
                on_click=rx.redirect(
                "/"
            ),
    ),
    
)      