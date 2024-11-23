import reflex as rx

class LoginState(rx.State):
    logged_in: int = 0

    def suma_valor(self):        
            self.logged_in = self.logged_in + 1
    def resta_valor(self):
            self.logged_in= self.logged_in-1

def mostrar_login():
    return rx.box(
            rx.cond(
            LoginState.logged_in%2,            
            rx.stack(                
                rx.heading("Apagado",bg="red"),
                flex_direction="row"
            ),
            rx.stack(
                rx.heading("Encendido",bg="green"),
                flex_direction="column"
            ),
                ),
            rx.hstack(
                rx.button("Suma Valor", on_click=LoginState.suma_valor),
                rx.button("Resta Valor", on_click=LoginState.resta_valor),
                rx.text(LoginState.logged_in),
            )

        ),
        
    
