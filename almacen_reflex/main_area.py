import reflex as rx
from almacen_reflex.state import State

from almacen_reflex.componentes.home_component import home_component
from almacen_reflex.componentes.about_component import about_component
from almacen_reflex.componentes.contact_component import contact_component
from almacen_reflex.componentes.service_component import service_component
from almacen_reflex.componentes.legal_component import legal_component
from almacen_reflex.componentes.busqueda_component import busqueda_component
# Área principal dinámica
def main_area():
    return rx.cond(
        State.current_component == "home",
        home_component(),
        rx.cond(
            State.current_component == "about",
            about_component(),
            rx.cond(
                State.current_component == "contact",
                contact_component(),
                rx.cond(
                    State.current_component == "services",
                    service_component(),
                    rx.cond(
                        State.current_component == "busqueda",
                        busqueda_component(),
                        rx.cond(
                            State.current_component == "legal",
                            legal_component(),
                            home_component()
                        )
                    )  
                )
            ),
        ),
    )