import reflex as rx 


def login_page():
          return rx.box(
                rx.vstack(
                rx.image(src="/b720bcb70932b26b5f48164e34da54f9.png", width="50px", height="50px"),
                rx.heading('INGRESE USUARIO'),
                rx.text('login'),
                spacing='10',
                align = 'center',
                background="3364b0",
                width="100%",
                height="auto",
            ),
            rx.box(
                rx.text('Email'),
            ),
            rx.box(
                rx.text('Password'),
                rx.input(),
            ),
            background=('green'),
          )
        
    