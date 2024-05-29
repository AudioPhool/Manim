import math
from manim import *
import numpy as np

class parabola(Scene):
    def construct(self):

        t = ValueTracker(-3)

        plane = NumberPlane(
            x_range = [-5,5,1], 
            x_length = 5, 
            y_range = [-10,10,5], 
            y_length = 5, 
            x_axis_config = {
                "line_to_number_buff": 0.1, 
                "label_direction": DOWN}
        ).add_coordinates().to_edge(RIGHT)
 
        axes=Axes(x_range = [-4,4,1], x_length = 5, y_range = [0,20,5], y_length = 5).add_coordinates()
        axes.to_edge(LEFT)

        parab = always_redraw(lambda: axes.plot(lambda x : (2*x**2)+(3*x)+1, x_range = [-3.01,t.get_value()], color = YELLOW)) #(2x+1)(x+1)
        dot = always_redraw(lambda: Dot(fill_color = WHITE, fill_opacity = 0.8).scale(0.5).move_to(parab.get_end()))

        box2 = always_redraw(lambda : Polygon(plane.get_origin(),plane.coords_to_point(t.get_value()+1,0),plane.coords_to_point(t.get_value()+1,2*t.get_value()+1),plane.coords_to_point(0,2*t.get_value()+1),color=RED,fill_opacity=0.5))

        self.play(Write(plane), DrawBorderThenFill(axes))
        self.add(parab, dot, box2)
        self.play(t.animate.set_value(1.5), run_time = 5, rate_func = linear) 