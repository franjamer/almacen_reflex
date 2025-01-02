import reflex as rx
from .state import State
from almacen_reflex_1.componentes.m0_home_component import home_component
from almacen_reflex_1.componentes.m5_inventario_component import inventario_component
from almacen_reflex_1.componentes.m4_movimientos_component import movimientos_component
from almacen_reflex_1.componentes.m3_pedidos_component import pedidos_component
from almacen_reflex_1.componentes.m2_detalle_component import detalle_component
from almacen_reflex_1.componentes.m1_busqueda_component import busqueda_component
# Área principal dinámica


def main_area():
    return rx.container(


        rx.cond(
            State.current_component == "home",
            home_component(),
            rx.cond(
                State.current_component == "busqueda",
                busqueda_component(),
                rx.cond(
                    State.current_component == "detalle",
                    detalle_component(),
                    rx.cond(
                        State.current_component == "pedidos",
                        pedidos_component(),
                        rx.cond(
                            State.current_component == "movimientos",
                            movimientos_component(),
                            rx.cond(
                                State.current_component == "inventario",
                                inventario_component(),
                                home_component()
                            )
                        )
                    )
                ),
            ),
        ),
        id="Mi-Contenedor_principal",
        bg=rx.color("tomato", 4),
        padding="auto",
        margin="auto",
        max_width="fix-content",
    )
