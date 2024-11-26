import reflex as rx
from almacen_reflex.componentes.formularios.b1_tabla_busqueda import tablaResultadoBusqueda
from almacen_reflex.componentes.formularios.b2_formulario_busqueda import formulario_busqueda
from almacen_reflex.componentes.formularios.b3_criterios_busqueda import criterios_busqueda
def busqueda_component():
    return rx.box(
                rx.vstack(
                    rx.center(
                    rx.heading(
                        "Menú Búsqueda ",
                        size="8",weight="medium"),
                    ),
                    rx.hstack(
                        rx.vstack(
                            rx.heading("Formulario de Busqueda",size="7",),
                            formulario_busqueda(),
                            bg="sky",
                            padding="0.3em"
                        ),
                        rx.vstack(
                            rx.heading("Criterios de Busqueda",size="7",),
                            criterios_busqueda(),
                            bg="green",
                            padding="0.3em"
                        ),
                    ),
                    rx.hstack(

                        tablaResultadoBusqueda(),
                        bg="brown"
                    ),
                    padding="0.1em", 
                    bg="grey",
                    width="90vw",
                    heidth="100vh",
                    align="center"
                    ),
                heidth="100vh"
                )
