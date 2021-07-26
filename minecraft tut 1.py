#Modules
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

#surface (ground) Entity

myGround = Entity(
    model = "plane",
    texture = "grass",
    collider = "mesh",
    scale = (100,100,100)
    )


player = FirstPersonController()
app.run()
