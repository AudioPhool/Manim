import math
from manim import *
import numpy as np
from numpy.lib.function_base import copy

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
        
        box2 = always_redraw(lambda : 
            Polygon(
                plane.get_origin(),
                plane.coords_to_point(t.get_value()+1,0),
                plane.coords_to_point(t.get_value()+1,2*t.get_value()+1),
                plane.coords_to_point(0,2*t.get_value()+1),
                color=RED,
                fill_opacity=0.5))

        label = MathTex("2x^2+3x+1").move_to(axes, UP).shift(UP)
        label2 = MathTex("2x^2+3x+1").move_to(plane, UP).shift(UP)

        self.play(Write(plane), DrawBorderThenFill(axes), Write(label), Write(label2) )
        self.add(parab, dot)
        self.play(DrawBorderThenFill(box2))
        self.play(t.animate.set_value(-1), run_time = 2, rate_func = linear)
        self.wait()
        self.play(t.animate.set_value(-0.5), run_time = 2, rate_func = linear)
        self.wait()
        self.play(t.animate.set_value(1.5), run_time = 2, rate_func = linear)
        self.wait()
