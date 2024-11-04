import reflex as rx

def menu_boton (text:str, url:str) -> rx.Component:
    return rx.link(
    rx.button(text),
    href=(url),
    color="white",    
    )
