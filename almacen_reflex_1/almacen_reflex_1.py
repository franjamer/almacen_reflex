"""Welcome to Reflex! This file outlines the steps to create a basic app."""
import reflex as rx
from rxconfig import config
from almacen_reflex_1.componentes.sidebar_component import sidebar
from almacen_reflex_1.main_area import main_area
from almacen_reflex_1.componentes.sidebar_menu import sidebar_menu


class State(rx.State):
    """The app state."""
    current_component: str = "home"

    def set_component(self, component: str):
        self.current_component = component


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        # rx.heading("Página Principal"),
        rx.hstack(
            sidebar(),
            main_area(),
            # sidebar_menu(),
            # justify="start",
            # align="center",
        ),
        max_width="100vw",
        max_height="100vh",
        margin="0",
        padding="0",
        # justify="start",
        # align="center",
        bg=rx.color("sky", 4),
        # rx.color_mode.button(position="top-right"),
    )


app = rx.App()
app.add_page(index)
