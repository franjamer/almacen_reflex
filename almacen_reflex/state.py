import reflex as rx

class State(rx.State):
    current_component: str = "home"

    def set_component(self, component: str):
        self.current_component = component
