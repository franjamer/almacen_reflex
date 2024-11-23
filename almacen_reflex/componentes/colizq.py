import reflex as rx
from almacen_reflex.componentes.menu_boton import menu_boton
from almacen_reflex.componentes.paginaPrincipal import paginaPrincipal
from almacen_reflex.componentes.sidebar import sidebar,sidebar_item,sidebar_items


def colizq() -> rx.Component:
    return rx.stack(    
    #     rx.vstack(
    #     sidebar_item("Pagina1", "layout-dashboard", "/Pagina1"),
    #     sidebar_item("Projects", "square-library", "/About"),
    #     sidebar_item("Analytics", "bar-chart-4", "/Custom"),
    #     sidebar_item("Messages", "mail", "/#"),
    #     spacing="10",
    #     width="100%",
    # ),
    sidebar(),
)

def Pagina1()-> rx.Component:
    return rx.stack(
        rx.text("Estoy en la Página 1"),
        rx.button(
            "Volver a Principal",
            on_click=rx.redirect("/")),
    )

def About()-> rx.Component:
    return rx.stack(
    rx.text(
        "About Page"),
    rx.button(
        "regreso a principal", on_click=rx.redirect("/")),
    rx.button(
        "Custom", on_click=rx.redirect("/custom")),
)

def Custom():
    return rx.stack(
        rx.box(
            rx.button("regreso a principal", on_click=rx.redirect("/")),
            rx.text("Custom Route")
            )        
        )

app = rx.App()
app.add_page(Pagina1)
app.add_page(About)
app.add_page(Custom)