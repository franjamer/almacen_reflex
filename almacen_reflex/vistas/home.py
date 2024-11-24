import reflex as rx

from almacen_reflex.componentes.sidebar import sidebar
from almacen_reflex.componentes.footer import footer

# class State(rx.State):
#     actual_componente: str= "home"
#     def sel_componente(self,componente: str):
#         self.actual_componente =  componente   


# # Área principal dinámica



def home() -> rx.Component:
    return rx.flex(
    # rx.hstack(
        sidebar(),
    #     justify="start",
    #     align="start",
    # ),  
        rx.box(
            main_area(),
            rx.text("MAIN AREA", color="red"),
            width="80%",
            padding="2em"
        ),
        rx.hstack(
            footer(),
            align="end",
            justify="center",
        ),    
    width="100%",
    height="100vh",
    align_content="start",
    justify="between",
    background_color="yellow",
)
