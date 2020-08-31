# Author: Rehoboth Okorie
# Date: Feb 9th 2020
# Purpose: Create a system class

from body import Body
import math


# initiate the system class
class System:
    # get the list of body objects in the system
    def __init__(self, body_list):
        self.body_list = body_list

    # update object for the body class
    def update(self, timestep):
        # iterate through body list and update the acceleration, position and velocity of the body objects
        for body in self.body_list:
            (ax, ay) = self.compute_acceleration(body)
            # update the velocity of the body using the new computed acceleration
            body.update_velocity(ax, ay, timestep)
            # update the position of the body using the new intantaneous velocity over a timestep
            body.update_position(timestep)

    # readjust the acceleration as the body moves
    def compute_acceleration(self, n):
        # set the initial acceleration to zero
        ax = 0
        ay = 0

        # gravitational constant
        G = 6.67 * (10 ** (-11))

        # calculate the vertical and horizontal components of the acceleration
        for x in self.body_list:
            if x != n:
                mass = x.mass
                # calculate the radius of using pythagoras theorem
                radius = math.sqrt(math.pow((x.x - n.x), 2) + math.pow((x.y - n.y), 2))

                # x and y distances
                dx = x.x - n.x
                dy = x.y - n.y

                # formula for acceleration due to gravity
                a = G * mass / (radius ** 2)

                # calculate the x and y components of acceleration
                ax += a * dx / radius
                ay += a * dy / radius

        # returns the current value of acceleration of the body.
        return ax, ay

    # draws a body from body list
    def draw(self, cx, cy, pixels_per_meter):
        for i in self.body_list:
            # call the draw method in body
            i.draw(cx, cy, pixels_per_meter)
