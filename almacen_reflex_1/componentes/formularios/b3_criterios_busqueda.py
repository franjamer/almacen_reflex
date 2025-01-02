import reflex as rx

def criterios_busqueda():
    return(

        rx.hstack(
                    rx.checkbox("Checked", name="check"),
                    rx.switch("Switched", name="switch"),
                ),
    )