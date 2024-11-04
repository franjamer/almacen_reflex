import reflex as rx
from almacen_reflex.componentes.colder import colder
from almacen_reflex.componentes.colizq import colizq
from almacen_reflex.componentes.colcen import colcen


def home() -> rx.Component:
    return rx.flex(
        rx.box(
            rx.hstack(
                rx.vstack(
                    colizq(),
                    padding="2px"
                ),
                rx.spacer(),
                rx.vstack(
                    colcen(),
                    padding="2px"
                ),
                rx.spacer(),
                rx.vstack(
                    colder(),
                    # padding="2px"
                ),
                # align="between"
                justify="between",
            ),
            width="100%"
        ),
        width="100%",
        height="93vh",
        # align= "between",
    )
