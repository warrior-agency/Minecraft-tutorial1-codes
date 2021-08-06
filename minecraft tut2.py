from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
app = Ursina()

#w p
window.fullscreen = False
#window.title = 'minecraft'

#ground or u can say it surface but in urrsina we say it Entity
#so Ground Entity =

# If u wanna use keystrokes in ursina u have to make a voxel ground instead of entity
#for that delete ground entity and follow my steps

class Voxel(Button):
    def __init__(self , position = (0,0,0)):
        super().__init__(
            parent = scene,
            model = "cube",
            texture = "white_cube",
            color = color.white,
            highlight_color = color.lime,
            collider = "box",
            position = position,
            origin_y = 0.5
            )


#   KEYSTROKES FOR PUTTING AND REMOVING BLOCKS
    def input(self,key):
        if self.hovered:
            if key == "left mouse down":
                voxel = Voxel(position = self.position + mouse.normal)
            if key == "right mouse down":
                destroy(self)







for z in range(20):
    for x in range(20):
        voxel = Voxel((x,0,z))


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

#Tutorial number 2

#IN this video i am gonaa show that how to use keystrokes for putting a block and removing it

#So let's go

#That's all for today

#bye bye
#stay home , stay safe..........
