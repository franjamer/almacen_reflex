import reflex as rx
from almacen_reflex.state import State


def sidebar():
    return rx.box(
        rx.stack(

            rx.button("Home", on_click=lambda: State.set_component("home")),
            rx.button(
                "Busqueda", on_click=lambda: State.set_component("busqueda")),
            rx.button("Detalle", on_click=lambda: State.set_component("detalle")),
            rx.button("Pedidos", on_click=lambda: State.set_component("pedidos")),
            rx.button("Movimientos",
                      on_click=lambda: State.set_component("movimientos")),
            rx.button("Inventario",
                      on_click=lambda: State.set_component("inventario")),


            justify="end",
            align="center",
            spacing="9",
            direction="column",
            # ), rx.stack(
            #     user_service(),
            #     width='9%',
            #     height="20vh",
            #     bg="sky",
            #     padding="1em"
        ),
        width="10%",
        height="100vh",
        bg="red",
        padding="1em",
        spacing="1em",
    )
