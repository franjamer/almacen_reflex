import reflex as rx


class DetalleState(rx.State):
    detalle_data: dict = {}

    @rx.event
    def handle_submit_detalle(self, detalle_data: dict):
        """Manipulacion del formulario enviado"""
        self.detalle_data = detalle_data


def detalle_Elemento():
    return rx.vstack(
        rx.form(
            rx.vstack(
                rx.input(
                    placeholder="First Name",
                    name="first_name",
                ),
                rx.input(
                    placeholder="Last Name",
                    name="last_name",
                ),

                rx.button("Submit", type="submit"),
            ),
            on_submit=DetalleState.handle_submit_detalle,
            reset_on_submit=True,
        ),
        rx.divider(),
        rx.heading("Results"),
        rx.text(DetalleState.detalle_data.to_string()),
    )
