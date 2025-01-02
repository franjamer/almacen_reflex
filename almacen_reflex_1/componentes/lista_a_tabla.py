import reflex as rx


class State(rx.State):
    data: list = [
        ["Lionel", "Messi", "PSG"],
        ["Christiano", "Ronaldo", "Al-Nasir"],
    ]
    columns: list[str] = ["First Name", "Last Name"]


def index():
    return rx.data_table(
        data=State.data,
        columns=State.columns,
    )
