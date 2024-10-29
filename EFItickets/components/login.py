import reflex as rx 

class inputs(rx.State):
        us : str = "Usuario"
        pw : str = "Contrasena"

#class matchIcon(rx.State):  
 #       icon_default=rx.icon("user")
        

def set_us(self, value):
        self.us = value


def login_page():
          return rx.box(
                rx.vstack(
                    rx.image(  
                            src="/b720bcb70932b26b5f48164e34da54f9.png", 
                            width="150px", 
                            height="auto",
                            ),
                    rx.box(
                        rx.input(
                            rx.input.slot(
                                    rx.icon(
                                        rx.flex(
                                   #     matchIcon.icon_default,         
                                         rx.icon("user",stroke_width=1.5, width="120px"),
                                      #  value=matchIcon.icon_default,
                                     #   on_change=matchIcon.set_icon_default,
                                        ),
             
                                    ),
                            ), 
                                placeholder="Email",
                                width="90%",
                                stroke_width_color="white", 
                                on_blur=inputs.set_us,
                                border_radius="10px",
                                color="white",
                                #width="12% 250px",
                        ),
                    ),
                    rx.divider(
                            decorative=True,
                            width="255px",
                            color_scheme="grass",
                    ),
                    rx.box(
                        rx.input(
                            rx.input.slot(
                                    rx.icon("key-round", stroke_width=1.5, width="120px"), 
                            ),
                                        rx.flex(
                                            rx.icon("eye-off", stroke_width=1, size=18, color="green"),                                            
                                           # rx.icon("eye", stroke_width=1, size=18, color="green"),
                                            align = 'center',
                                            margin="5px",                             
                                        ),
                            placeholder="Contraseña",
                            width="90%",
                            border_radius="10px",
                            stroke_width_color="white", 
                            on_blur=inputs.set_pw,
                            ), 
                            #rx.icon(tag="eye-off", stroke_width=1, width="80px"),
                            border_radius="10px",
                            color="white",
                            width="12% 300px",
                        ),
                    
                     rx.divider(
                       decorative=True,
                       width="255px",
                       color_scheme="grass",
                     
                    ),

                    rx.box(
                        rx.text(
                            "¿Se te olvido la contrasena?",
                            size='1',
                            color = "green",
                            text_align="left",
                         ),
                         text_align="start",
                         spacing="2",
                         color_scheme="grass",
                    ),
                    rx.flex(
                        rx.card(
                                'Iniciar sesion',
                                background_color="#02d402",
                                ),      
                         spacing="2",
                       
                    ),
                align = 'center',
                width="100%",
                height="auto",
                flex_direction="column",
                ),
            #border_size="1px",
            border="1px solid var(--gray-10)",     
            border_radius="10px",
            border_color="green" ,  
            spacing="1",
         #   background_color=rx.color("tomato", 3),
             
  #  background_image="linear-gradient(271.68deg, #EE756A 0.75%, #756AEE 88.52%)",
            #background_image(src="/assets/Fondo Login IMG.png"),
            #background=('3364b0'),
   
        )