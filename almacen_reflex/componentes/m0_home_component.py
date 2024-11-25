import reflex as rx


def home_component():
    return rx.center(        
            rx.stack(
                rx.heading(
                    "Almacén de Repuestos",
                    size="9",
                    color="black",
                    weight="bold"
                ),
                rx.image(
                    src="/logo_Apis_personalizado.svg",
                    width="300px",
                    height="280px",                    
                ),
                rx.heading(
                    "Fábrica de Montijo",
                    size="9",
                    color="black",
                    weight="bold"
                ),
                space="9",
                align="center",
                justify="center",
                direction="column",      
                    # align="center",
                    width="90vw",
                    height="99vh",
        ),
        padding="0.1em",
        color="black",
        bg="white",
        heigth="100vh",
        justify="center",
        align="center",

    )

