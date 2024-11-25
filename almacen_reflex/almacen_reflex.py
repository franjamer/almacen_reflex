import reflex as rx
from almacen_reflex.state import State
from almacen_reflex.main_area import main_area
from almacen_reflex.componentes.sidebar_component import sidebar

# Página principal
def main_page():
    return rx.flex(
        sidebar(),
        rx.box(
            main_area(),
            width="100vw",
            padding="0.1em",
            bg="black"
        ),
        direction="row",
    )

app = rx.App()
app.add_page(main_page, route="/")

