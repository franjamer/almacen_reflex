import reflex as rx
from almacen_reflex.vistas.home import home
from almacen_reflex.componentes.footer import footer


class State(rx.State):
    pass


def index() -> rx.Component:
    return rx.box(
        rx.vstack(

            home(),
            # footer(),

        ),
        # padding_x="0.25%",
        # padding_y="0.5%",
        max_heigth="100vh",
        height="100vh",
        align_content="center",
        bg="grey",
    )


# app = rx.App()
# app.add_page(index)


# def index():
#     return rx.stack(
#         home(),
#     rx.text("Root Page"),
#     rx.button("Custom",on_click=rx.redirect("/custom")),
#     rx.button("About",on_click=rx.redirect("/about"))
#     )
def custom() -> rx.Component:
    return rx.stack(
        rx.box(
            rx.button("regreso a principal", on_click=rx.redirect("/")),
            rx.text("Custom Route")
        )
    )

app = rx.App()
app.add_page(index)
app.add_page(custom)
