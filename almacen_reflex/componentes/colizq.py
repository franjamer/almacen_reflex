import reflex as rx
from almacen_reflex.componentes.botones import menu_boton

def colizq() -> rx.Component:
    return rx.vstack(
                menu_boton("Busqueda","busqueda"),
                menu_boton("Detalle","detalle"),
                menu_boton("Pedidos","pedidos"),
                background_color= "white",
                width="6vw",
                height="93vh",
                max_heigth="100%",
                padding="2px",
                align="start"
            )

def Busqueda():
    return rx.vstack(
        rx.text("Pagina Busqueda"),
    rx.button(
        "Página Principal",
        on_click=rx.redirect(
            "/"
        ),
    ),
    
) 

def Detalle():
    return rx.vstack(
        rx.text("Pagina Detalle"),
    rx.button(
        "Página Principal",
        on_click=rx.redirect(
            "/"
        ),
    ),
    
) 

def Pedidos():
    return rx.vstack(
        rx.text("Pagina Pedidos"),
            rx.button(
                "Página Principal",
                on_click=rx.redirect(
                "/"
            ),
        ),
    
    ) 