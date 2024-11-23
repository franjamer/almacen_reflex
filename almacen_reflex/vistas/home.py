import reflex as rx

from almacen_reflex.componentes.colizq import colizq
from almacen_reflex.componentes.colcen import colcen
from almacen_reflex.componentes.colder import colder
from almacen_reflex.componentes.sidebar import sidebar_items,sidebar
# from almacen_reflex.componentes.sidebar import sidebar




def home() -> rx.Component:
    return rx.flex(
        rx.center(
        #     rx.card("Pagina Home"),
    sidebar(),
    # sidebar_items(),
    # colizq(),
    # colcen(),
    # sidebar_items(), 
    # colder(),
        ),
    width="100%",
    align="center",
    background_color="yellow",
    padding="10px",
    
)

