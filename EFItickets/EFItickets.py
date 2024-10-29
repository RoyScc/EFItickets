import reflex as rx 
from .components.login import login_page
#from .components.login import obtenerUsuarios
#import sqlite3

#backend
class inputs(rx.State):
        us : str = "Usuario"
        pw : str = "Contrasena"
#class Data(rx.State):
#    persons : list[list] = []  #atributos

    

# frontend

def index():
    page = rx.box(
            login_page(),  
            #rx.image(  
           #             src="/BackgroundLogin.png", 
           #             
                        #width="150px", 
                        #height="auto",
            #        ),
            background_image="url('file:// home/itec/web/reflex/EFItickets/assets/BackgroundLogin.png')",
            background_position= "center",
            background_repeat= "no-repeat",
            background_size= "cover",
            padding='30px',
            margin='10px',
            #background_image="src('assets/Background Login.png')",

            #background=(src="/assets/Fondo Login IMG.png"),
           # background_image="linear-gradient(271.68deg, #EE756A 0.75%, #756AEE 88.52%)",
           
    )
    
    return page

app = rx.App()
app.add_page(index)
