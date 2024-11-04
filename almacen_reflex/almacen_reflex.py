import reflex as rx
from almacen_reflex.componentes.navbar import navbar
from almacen_reflex.vistas.home import home

class State(rx.State):
    pass

def index() -> rx.Component:
    return rx.box(
                navbar(),
                    rx.flex(        
                        rx.vstack(       
                        home(),
                        max_width="100vw",
                        max_heigth="99vh",
                        width= "95%",
                        height="98%",
                        ),                    
                    ),
                    max_heigth="100vh",
                    height="100vh",
                    bg="tomato",   
                    # padding_y="2%",
                    # padding_x="1%" 
    )
    
app = rx.App()
app.add_page(index)
