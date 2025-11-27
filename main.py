from ursina import *

app = Ursina()

cube = Entity(model='cube', color=hsv(300,1,1), scale=3, collider='box')

def spin():
    cube.animate('rotation_x', cube.rotation_y+180, duration=2, curve=curve.in_out_expo)

cube.on_click = spin
EditorCamera()  # add camera controls for orbiting and moving the camera

app.run()