import reflex as rx
from almacen_reflex.componentes.menu_boton import menu_boton
from almacen_reflex.componentes.sidebar import sidebar_item


def colder() -> rx.Component:
        return rx.stack(
             rx.vstack(
        sidebar_item("Movimientos", "layout-dashboard", "movimientos"),
        sidebar_item("Inventario", "square-library", "/inventario"),
        sidebar_item("Analytics", "bar-chart-4", "/#"),
        sidebar_item("Messages", "mail", "/#"),
        spacing="10",
        width="100%",
    ), 
        # menu_boton("Movimientos","movimientos"),
        # menu_boton("Inventario","inventario"),
        # menu_boton("Home",""),
        # flex_direction="column",
        # width="20vw",
        # height="95vh",
        # bg="violet",
        # justify="between",
        # align="center",
        # padding_y="1em"
        ),



def movimientos():
    return rx.vstack(
        # navbar(),
        rx.text("Movimientos"),
            rx.button(
                "Página Principal",
                on_click=rx.redirect(
                "/"
            ),
        ),
    
    )      

def inventario():
    return rx.vstack(
        rx.text("Inventario"),
            rx.button(
                "Página Principal",
                on_click=rx.redirect(
                "/"
            ),
    ),
    
)      