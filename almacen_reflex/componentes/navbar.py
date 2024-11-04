import reflex as rx

def navbar() -> rx.Component:
    return rx.hstack(
        rx.text(
            "Almacén",
            height="40px"
        ),
        position="stycky",
        bg="blue",
        padding_x="16px",
        padding_y = "8px",
        z_index="999",
        witdh= "100%"
    )
