# Author: Rehoboth Okorie
# Date: Feb 9th 2020
# Purpose: Create a body class

from cs1lib import *


# initiate the class
class Body:
    # get the properties for the body object
    def __init__(self, mass, image, zx, zy, vx, vy, pixel_radius, r, g, b, d1=0, d2=0):
        self.x = zx
        self.y = zy
        self.vx = vx
        self.vy = vy
        self.mass = mass
        self.image = load_image(image)
        self.d1 = d1
        self.d2 = d2
        self.pixel_radius = pixel_radius
        self.r, self.g, self.b = r, g, b

    # update the position of the body using the velocity and timestep
    def update_position(self, timestep):
        self.x += self.vx * timestep
        self.y += self.vy * timestep

    # update the velocity of the body using the acceleration and timestep
    def update_velocity(self, ax, ay, timestep):
        self.vx += ax * timestep
        self.vy += ay * timestep

    # draw the ball object to the screen
    # d1 and d2 alter the draw point of the image to the center of gravity of the body
    def draw(self, cx, cy, pixels_per_meter):
        set_fill_color(self.r, self.g, self.b)
        draw_image(self.image, cx + (self.x * pixels_per_meter), cy + (self.y * pixels_per_meter), self.d1, self.d2)
