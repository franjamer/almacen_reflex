import reflex as rx
from almacen_reflex_1.componentes.lista_a_tabla import index


def movimientos_component():
    return rx.container(
        rx.text("Movimientos de almacen(Entradas y salidas)",
                color="tomato"),
        index(),
        padding="2em",
        bg="lightcoral",
    )
