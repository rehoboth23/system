# solar driver.py
# Example for CS 1 Lab Assignment 2.
# db, thc; 2011-2016

from cs1lib import *
from system import System
from body import Body

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 700

TIME_SCALE = 2000000000     # real seconds per simulation second
PIXELS_PER_METER = 12 / 1e10  # distance scale for the simulation

FRAMERATE = 30000           # frames per second
TIMESTEP = 1.0 / FRAMERATE  # time between drawing each frame


def main():

    set_clear_color(0, 0, 0)    # black background

    clear()
    space = load_image("space.png")
    draw_image(space, 0, 0)
    # Draw the system in its current state.
    solar.draw(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, PIXELS_PER_METER)

    # Update the system for its next state.
    solar.update(TIMESTEP * TIME_SCALE)


sun = Body(1.98892e30, "sun.png", 0, 0, 0, 0, 30, 1, 1, 0, 40, 40)
mercury = Body(.0553 * 5.9736e24, "mercury.png", -.3871 * 1.49598e11, 0, 0, 47890, 6, 1, .4, 0)
venus = Body(.815 * 5.9736e24, "venus.png", -.7233 * 1.49598e11, 0, 0, 35040, 12, 0, .6, .2)
earth = Body(5.9736e24, "earth.png", -1.0 * 1.4598e11, 0, 0, 29790, 14, 0, .4, 1)
mars = Body(.107 * 5.9736e24, "mars.png", -1.524 * 1.49598e11, 0, 0, 24140, 8, .8, .2, 0)

solar = System([sun, mercury, venus, earth, mars])

start_graphics(main, framerate=FRAMERATE, width=1000, height=700)
