import reflex as rx


def inventario_component():
    return rx.box(
        rx.form(
            rx.text("Inventario de todos los repuestos", color="black")
        ),
        padding="0.5em",
        bg="lightgreen")
