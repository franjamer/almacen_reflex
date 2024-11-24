import reflex as rx
from almacen_reflex.state import State



def sidebar():
    return rx.box(
        rx.vstack(

        rx.button("Home", on_click=lambda: State.set_component("home")),
        rx.button("About", on_click=lambda: State.set_component("about")),
        rx.button("Contact", on_click=lambda: State.set_component("contact")),
        rx.button("Busqueda", on_click=lambda: State.set_component("busqueda")),
        rx.button("Legal", on_click=lambda:State.set_component("legal")),
        justify="between",
        align="center"
        ),
        width="20%",
        height="100vh",
        bg="gray",
        padding="1em",
        spacing="1em",
    )


