import reflex as rx

# class EstadoCondicionalSimple(rx.State):
#     muestra: bool = True
#     @rx.evento
#     def cambio(self):
#         self.muestra = not(self.muestra)
# def ejemplo_cond_simple():
#     return rx.vstack(
#         rx.button(
#             "Tooble", on_click=EstadoCondicionalSimple.change
#         ),
#         rx.cond(
#             EstadoCondicionalSimple.muestra,
#             rx.text("Texto1", color="blue")
#             rx.text("Texto2", color="red")
#         )
#         )
#     )

# def texto_boton(text:str)-> rx.Comonent:
#     if on_click() 


def menu_boton (text:str, url:str) -> rx.Component:
    
    return rx.box(
        rx.link(
            rx.card(text,bg="blue"),
        href=(url),
        ),
        bg="white",    
    )
