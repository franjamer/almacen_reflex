def main_area():
    return rx.cond(
        State.current_component == "home",
        home(),
        rx.cond(
            State.current_component == "about",
            about_component(),
            rx.cond(
                State.current_component == "contact",
                contact_component(),
                rx.cond(
                    State.current_component == "busqueda",
                    busqueda_component(),
                    home_component()
                )
            ),
        ),
    )