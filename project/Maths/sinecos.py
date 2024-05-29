import math
from os import remove
from manim import *
import numpy as np
from numpy.lib.function_base import copy

class anim(Scene):
    def construct(self):
        phi1 = ValueTracker(0.01)
        phi2 = ValueTracker(0.01)

        plane1 = (
            NumberPlane(x_range=[0, 4, 1], x_length=5, y_range=[-1, 1, 1], y_length=5)
            .add_coordinates()
            .shift(LEFT * 3.5)
        )

        plane2 = (
            NumberPlane(x_range=[0, 4, 1], x_length=5, y_range=[-1, 1, 1], y_length=5)
            .add_coordinates()
            .shift(RIGHT * 3.5)
        )

        label1 = MathTex("y=sin(x)").next_to(plane1, UP)
        label1T = MathTex("y=cos(x)").next_to(plane1, UP)
        label1TT = MathTex("y=sin(x)").next_to(plane1, UP)

        label2 = MathTex("y=cos(x)").next_to(plane2, UP)
        label2T = MathTex("y=sin(x)").next_to(plane2, UP)
        label2TT = MathTex("y=cos(x)").next_to(plane2, UP)

        sine = always_redraw(lambda: 
                 plane1.plot(lambda x: 
                    np.sin((2*x) + np.deg2rad(phi1.get_value())), 
                    x_range = [0,4], 
                    color = YELLOW))
        
        cos = always_redraw(lambda: 
                 plane2.plot(lambda x: 
                    np.cos((2*x) + np.deg2rad(phi2.get_value())), 
                    x_range = [0,4], 
                    color = YELLOW))

        self.play(
                LaggedStart(
                    DrawBorderThenFill(plane1), 
                    DrawBorderThenFill(plane2),
                       run_time = 1 )
                )

        self.play(Write(sine))
        self.play(Write(label1))
        self.wait()
        self.play(Write(cos))
        self.play(Write(label2))
        #self.play(phi1.animate.set_value(90), Transform(label1, label1T))
        #self.wait()
        #self.play(phi2.animate.set_value(90), Transform(label2, label2T))
        #self.wait()
        self.play(phi1.animate.set_value(0), ReplacementTransform(label1, label1TT), phi2.animate.set_value(0), ReplacementTransform(label2, label2TT)) 
        self.wait()


