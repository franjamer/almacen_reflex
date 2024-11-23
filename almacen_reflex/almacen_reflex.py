import reflex as rx
from almacen_reflex.vistas.home import home


class State(rx.State):
    pass


def index() -> rx.Component:
    return rx.box(
        rx.vstack(

            home(),

        ),
        padding_x="1%",
        padding_y="0.5%",
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


app = rx.App()

app.add_page(index)
