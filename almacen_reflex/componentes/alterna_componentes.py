import reflex as rx
from typing import List
from almacen_reflex.componentes.footer import footer_items_1
# from reflex import event


# class CondSimpleState(rx.State):
#     show: bool = True

#     # @rx.event
#     def change(self):
#         # index=index+1
#         self.show = not self.show
#         show: bool = True

#     # @rx.event
#     # def change(self):
#     #     self.show = not (self.show)

# def alternar_componentes():
#     return rx.vstack(
#         rx.button(
#             "Toggle", on_click=CondSimpleState.change
#         ),
#         rx.cond(
#             CondSimpleState.show,
#             rx.text(CondSimpleState.change, color="blue"),
#             # rx.text("Text 2", color="red"),
#             footer_items_1()
#         ),
#     )



# import reflex as rx

class MatchState(rx.State):
    cat_breed: str = ""
    animal_options: List[str] = [
        "persian",
        "siamese",
        "maine coon",
        "ragdoll",
        "pug",
        "corgi",
    ]

def match_demo():
    return rx.flex(
        rx.match(
            MatchState.cat_breed,
            ("persian", rx.text("Persian cat selected.")),
            ("siamese", rx.text("Siamese cat selected.")),
            ("maine coon", rx.text("Maine Coon cat selected.")),
            ("ragdoll", rx.text("Ragdoll cat selected.")),
            rx.text("Unknown cat breed selected."),
        ),
        rx.select.root(
            rx.select.trigger(),
            rx.select.content(
                rx.select.group(
                    rx.foreach(
                        MatchState.animal_options,
                        lambda x: rx.select.item(
                            x, value=x
                        ),
                    )
                ),
            ),
            value=MatchState.cat_breed,
            on_change=MatchState.set_cat_breed,
        ),
        direction="column",
        gap="2",
    )
