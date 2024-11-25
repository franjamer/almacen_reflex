import reflex as rx


def home_component():
    return rx.box(
        rx.center(
            rx.vstack(
                rx.heading(
                    "Centro de Producción de Montijo",
                    size="9",
                ),
                rx.image(
                    src="/logo_Apis_personalizado.svg",
                    width="300px",
                    height="280px",
                    # bg="grey"
                ),
            ),
            justify="center",
            align="center",
        ),
        padding="0.1em",
        color="black",
        bg="yellow",
        heigth="100vh",
        justify="center",
        align="center",

    )
