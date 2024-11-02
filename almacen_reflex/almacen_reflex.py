import reflex as rx
from rxconfig import config
class State(rx.State):
    pass


def index() -> rx.Component:
    return rx.container(rx.text("Página principal", color= "white"),
    rx.vstack(
        rx.button(
        rx.link(
            "Pagina busqueda", 
            color="white",
            href="/busqueda"
            )
        ),
        rx.button(
        rx.link(
            "Pagina Detalle", 
            color="white",
            href="/detalle"
            )
        ),
        rx.button(
        rx.link(
            "Pagina Pedidos", 
            color="white",
            href="/pedidos"
            )
        ),
        rx.button(
        rx.link(
            "Pagina Movimientos", 
            color="white",
            href="/movimientos"
            )
        ),
        rx.button(
        rx.link(
            "Pagina Inventario", 
            color="white",
            href="/inventario"
            )
        )
    )
    
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




app = rx.App()
app.add_page(index)
app.add_page(Busqueda)
app.add_page(Pedidos)
app.add_page(Movimientos)
app.add_page(Inventario)
app.add_page(Detalle)
