import reflex as rx
from almacen_reflex.state import State

from almacen_reflex.componentes.m0_home_component import home_component
from almacen_reflex.componentes.m5_inventario_component import inventario_component
from almacen_reflex.componentes.m4_movimientos_component import movimientos_component
from almacen_reflex.componentes.m3_pedidos_component import pedidos_component
from almacen_reflex.componentes.m2_detalle_component import detalle_component
from almacen_reflex.componentes.m1_busqueda_component import busqueda_component
# Área principal dinámica
def main_area():
    return rx.cond(
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
    )