import reflex as rx  # Usa reflex como alias en lugar de importar rx directamente.
# from almacen_reflex.vistas.home import home
# from almacen_reflex.state import state
# from almacen_reflex.vistas.main_area import main_area
# from almacen_reflex.vistas.home import main_area

""" 
CÓDIGO VALIDO

El siguiente código funciona perfectamente, pero quiero aprovechar los 
componentes que ya tengo yo hechos.
"""
# # Definir el estado
class State(rx.State):
    current_component: str = "home"

    def set_component(self, component: str):
        self.current_component = component

# Componentes principales
def home_component():
    return rx.box("Bienvenido al componente Home", padding="2em", bg="lightblue")

def about_component():
    return rx.box("Información sobre nosotros", padding="2em", bg="lightgreen")

def contact_component():
    return rx.box("Contáctanos aquí", padding="2em", bg="lightcoral")

def busqueda_component():
    return rx.box("Opción Búsqueda aquí", padding="2em",bg="lightred")

# Sidebar
def sidebar():
    return rx.vstack(
        rx.button("Home", on_click=lambda: State.set_component("home")),
        rx.button("About", on_click=lambda: State.set_component("about")),
        rx.button("Contact", on_click=lambda: State.set_component("contact")),
        rx.button("Busqueda",on_click=lambda: State.set_component("busqueda")),
        width="20%",
        height="100vh",
        bg="gray",
        padding="1em",
        justify="between",
        align="center"
        # spacing="1em",
    )

# Área principal dinámica
# def main_area():
#     return rx.cond(
#         State.current_component == "home",
#         home_component(),
#         rx.cond(
#             State.current_component == "about",
#             about_component(),
#             rx.cond(
#                 State.current_component == "contact",
#                 contact_component(),
#                 rx.cond(
#                     State.current_component == "busqueda",
#                     busqueda_component(),
#                     home_component()
#                 )
#             ),
#         ),
#     )


def main_area():
    return rx.switch(
        State.current_component,
        {
            "home": home_component(),
            "about": about_component(),
            "contact": contact_component(),
            "busqueda": busqueda_component(),
        },
        home_component(),  # Valor por defecto si no coincide ninguna opción
    )


# Página principal
def main_page():
    return rx.flex(
        sidebar(),
        rx.box(
            main_area(),
            width="80%",
            padding="2em",
        ),
        direction="row",
    )

app = rx.App()
app.add_page(main_page, route="/")

"""Fin del CÓDIGO VÁLIDO"""
# class State(rx.State):
#     actual_componente: str= "index"
#     def sel_componente(self,componente: str):
#         self.actual_componente =  componente   


# # 
# def index() -> rx.Component:
#     return rx.flex(
#         main_area(),
#         # max_heigth="100vh",
#         # height="100vh",
#         # align_content="center",
#         # bg="grey",
#         # rx.text("este es el componente home")
#     )


# # import reflex as rx

# # Estado para almacenar el componente activo
# class MatchState(BaseModel):
#     active_component: str = Field(default="component1")

# # Componente de la sidebar
# class Sidebar(rx.Component):
#     def render(self):
#         return rx.box(
#             rx.button("Mostrar Componente 1", on_click=lambda: state.set("active_component", "component1")),
#             rx.button("Mostrar Componente 2", on_click=lambda: state.set("active_component", "component2")),
#             # ... más botones
#         )

# # Componentes que se mostrarán en el lienzo
# class Component1(rx.Component):
#     def render(self):
#         return rx.text("Contenido del Componente 1")

# class Component2(rx.Component):
#     def render(self):
#         return rx.text("Contenido del Componente 2")

# # Componente del lienzo
# class Canvas(rx.Component):
#     def render(self):
#         if state.active_component == "component1":
#             return Component1()
#         elif state.active_component == "component2":
#             return Component2()
#         # ... más casos

# Aplicación principal
# app = rx.App()
# app.add_page(index)
# app.add(Sidebar)

# app.add(Canvas)
# app.run()
