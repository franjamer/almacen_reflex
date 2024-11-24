import reflex as rx
class State(rx.State):
    def algun_metodo(self):
        ruta_actual_dela_pagina=self.router.page.path
        url_actual_dela_pagina=self.router.page.raw_path

def sidebar_item(text: str, icon: str, href: str) -> rx.Component:
    return rx.link(
        rx.hstack(
            rx.icon(icon),
            rx.text(text, size="4"),
            width="100%",
            padding_x="0.5rem",
            padding_y="0.75rem",
            align="center",
            style={
                "bg": "red",
                "color": "white",
                "_hover": {
                    "bg": rx.color("white", 4),
                    "color": rx.color("red", 11),
                },
                "border-radius": "0.5em",
            },
        ),
        href=href,
        underline="none",
        weight="medium",
        width="100%",
    )


def sidebar_items() -> rx.Component:
    return rx.vstack(
        sidebar_item("Busqueda", "layout-dashboard", "pagina1"),
        sidebar_item("Detalle", "square-library", "About"),
        sidebar_item("Pedidos", "bar-chart-4", "Custom"),
        sidebar_item("Movimientos de Almacén", "layout-dashboard", "pagina1"),
        sidebar_item("Inventario General", "square-library", "About"),
        spacing="3",
        width="100%",
    )


def sidebar() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.vstack(
                rx.hstack(
                    rx.image(
                        src="/logo_apis_personalizado.png",
                        width="2.25em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading(
                        "Apis", size="7", weight="bold", color="white"
                    ),
                    align="center",
                    justify="start",
                    padding_x="0.5rem",
                    width="100%",
                ),
                sidebar_items(),
                spacing="1",
                # position="fixed",
                # left="0px",
                # top="0px",
                # z_index="5",
                padding_x="1em",
                # padding_y="1em",
                bg=rx.color("red", 6),
                # bg="red",
                # color="white",
                align="align-justify",
                justify="center",
                height="100vh",
                # height="650px",
                width="12em",
                # margin_y="0",

            ),
        ),
        rx.mobile_and_tablet(
            rx.drawer.root(
                rx.drawer.trigger(
                    rx.icon("align-justify", size=30)
                ),
                rx.drawer.overlay(z_index="5"),
                rx.drawer.portal(
                    rx.drawer.content(
                        rx.vstack(
                            rx.box(
                                rx.drawer.close(
                                    rx.icon("x", size=30)
                                ),
                                width="100%",
                            ),
                            sidebar_items(),
                            spacing="5",
                            width="100%",
                        ),
                        top="auto",
                        right="auto",
                        height="100%",
                        width="20em",
                        padding="1.5em",
                        bg=rx.color("accent", 2),
                    ),
                    width="100%",
                ),
                direction="left",
            ),
            # padding="1em",
        ),
        height="90vh"
    )


    @rx.page(route="/pagina1", title="Página 1")
    def pagina1() -> rx.Component:
        return rx.fragment(
        rx.text("Estoy en la Página 1"),
        rx.button(
            "Volver a Principal",
            on_click=rx.redirect("/")
        ),
    )


def about() -> rx.Component:
    return rx.stack(
        rx.text(
            "About Page"),
        rx.button(
            "regreso a principal", on_click=rx.redirect("/")),
        rx.button(
            "Custom", on_click=rx.redirect("/custom")),
    )

