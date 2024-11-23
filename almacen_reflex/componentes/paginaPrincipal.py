import reflex as rx
# from almacen_reflex.vistas.home import home

def paginaPrincipal(text: str) -> rx.Component:
    return rx.stack(
        # rx.text(text),
        # rx.button(
        #     "Regreso de la página ",text,
        #     on_click=rx.redirect(
        #         "/"
        #     ),
        home()
        ),

    # )
