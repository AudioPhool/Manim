import math
from os import remove
from manim import *
import math
import numpy as np
from numpy.lib.function_base import copy

class anim(Scene):
    def construct(self):

        axis1 = Axes(
            x_range = [-1,1,0.5], 
            x_length = 6, 
            y_range = [-1,1,0.5],
            y_length = 6, 
            tips=True,
            ).add_coordinates()
        axis1.to_edge(LEFT, buff = 0.5)

        axis2 = Axes(
            x_range = [0,4,1], 
            x_length = 4, 
            y_range = [-1,1,1], 
            y_length = 2.5, 
            tips=False
            ).add_coordinates()
        axis2.to_corner(UR, buff = 1)

        axis3 = Axes(
            x_range = [0,4,1], 
            x_length = 4, 
            y_range = [-1,1,1], 
            y_length = 2.5, 
            tips=False
            ).add_coordinates()
        axis3.to_corner(DR, buff = 1)

        sine1 = always_redraw(lambda: 
                 axis2.plot(lambda x: 
                    A1.get_value() * (np.sin((2*x) + np.deg2rad(Phi1.get_value()))), 
                    x_range = [0,4], 
                    color = YELLOW))

        sine2 = always_redraw(lambda: 
                 axis3.plot(lambda x: 
                    A2.get_value() * (np.sin((2*x) + np.deg2rad(Phi2.get_value()))), 
                    x_range = [0,4], 
                    color = BLUE))

        sine3 = always_redraw(lambda: 
                 axis3.plot(lambda x: 
                    A2.get_value() * (np.sin((2*x) + np.deg2rad(Phi2.get_value()))), 
                    x_range = [0,4], 
                    color = BLUE))