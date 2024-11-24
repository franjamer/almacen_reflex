import reflex as rx

from almacen_reflex.componentes.sidebar import sidebar_items,sidebar
from almacen_reflex.componentes.footer import footer
from almacen_reflex.componentes.alterna_componentes import match_demo
def home() -> rx.Component:
    return rx.flex(
    rx.hstack(
        sidebar(),
        justify="start",
        align="start",
    ),    
    rx.hstack(
        footer(),
        align="end",
        justify="center",
        ),    
    # alternar_componentes(),
    match_demo(),
    width="100%",
    height="100vh",
    align_content="start",
    justify="between",
    background_color="yellow",
)





# from almacen_reflex.componentes.colizq import colizq
# from almacen_reflex.componentes.colcen import colcen
# from almacen_reflex.componentes.colder import colder
        #     rx.card("Pagina Home"),
        # # este componente solo es para maquetado, despues se eliminará
        # rx.card(
        #     rx.text("Componente home con fondo amarillo",color="red")
        # ),
        # padding_y="5px",

    # sidebar_items(),
    # colizq(),
    # colcen(),
    # sidebar_items(), 
    # colder(),