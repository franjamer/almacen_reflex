import reflex as rx

# from almacen_reflex.state import State
# from almacen_reflex.main_area import main_area
# from almacen_reflex.componentes.sidebar_component import sidebar
# from .usuario_pagina import user_page


# Página principal


def main_page():
    return rx.flex(
        rx.text("texto en el sidebar"),
        # sidebar(),
        rx.box(
            rx.text("Texto en el main area"),
            # main_area(),
            # user_service(),
            width="100vw",
            padding="0.1em",
            bg="black"
        ),
        direction="row",
    )


app = rx.App()
app.add_page(main_page, route="/")
# app.add_page(user_page, route="/usuarios")
