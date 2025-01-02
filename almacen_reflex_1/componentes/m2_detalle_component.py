import reflex as rx
from almacen_reflex_1.componentes.formularios.d1_formulario_detalle import detalle_Elemento


def detalle_component():
    return rx.container(
        detalle_Elemento(),
        id="contenedor-componente-detalle",
        padding="2em",
        bg="lightcoral",
        justify="center",
        align="start",
        width="90hvw",
    )
