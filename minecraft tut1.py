from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
app = Ursina()

#w p
window.fullscreen = False
#window.title = 'minecraft'

#ground or u can say it surface but in urrsina we say it Entity
#so Ground Entity =

ground = Entity(
    model = "plane",
    texture = "grass",
    collider = "mesh",
    scale = (100,100,100)
    )




#Our player
player = FirstPersonController()
app.run()

#if no ground is there ur screen is always gonna be blank
#minecraft is 1 person game
#it is part 1
#Source code provided by me on github (github link in the description)
#Let's Go
#Amazing
#ursina has in-built keyboard controller use w,a,s,d for movement and space for a jump
#Now let's add some ursina window properties 

#Thank u
