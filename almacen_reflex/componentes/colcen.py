import reflex as rx
from almacen_reflex.componentes.componente_condicional import mostrar_login
from almacen_reflex.componentes.sidebar import sidebar_item

# Define los botones en la pantalla principal


# def colcen()-> rx.Component:
#     return rx.vstack(
#         rx.button("About", 
#                   onClick=rx.redirect(about)),
#         rx.button("Custom", 
#                   onClick=rx.redirect(custom))
#     )



def colcen() -> rx.Component:
    return rx.stack(
        
        rx.vstack("columna 1"),
        # rx.vstack(sidebar_items()),
        rx.box(
            # MyObjectComponent("pepe",22),
            mostrar_login(),
            bg="gold",
            color="black"
            ),
        # rx.box(
        #     "caja al 50'%' de ancho en fila",
        #     bg="orange",
        #     border_radius="3px",
        #     width="50%",
        # ),
        # rx.box(
        #     "caja al 50'%' de ancho en fila",
        #     bg="lightblue",
        #     border_radius="3px",
        #     width="50%",
        # ),
        flex_direction="row",
        width="100%",
        height="95vh",
        bg="green",
        justify="between",
        align="center",
        padding_x="1em"
    )


