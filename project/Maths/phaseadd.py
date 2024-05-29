import math
from os import remove
from manim import *
import numpy as np
from numpy.lib.function_base import copy

class anim2(Scene):
    def construct(self):

        phi1 = ValueTracker(0.01)
        phi2 = ValueTracker(0)

        a1 = Axes(
            x_range = [0,4,1], 
            x_length = 4, 
            y_range = [-1,1,1],
            y_length = 2, 
            tips=False,
            ).add_coordinates()
        a1.to_corner(UL, buff = 1)

        a2 = Axes(
            x_range = [0,4,1], 
            x_length = 4, 
            y_range = [-1,1,1], 
            y_length = 2, 
            tips=False
            ).add_coordinates()
        a2.to_corner(DL, buff = 1)

        a3 = Axes(
            x_range = [0,4,1], 
            x_length = 4, 
            y_range = [-2,2,1], 
            y_length = 3, 
            tips=False
            ).add_coordinates()
        a3.to_edge(RIGHT, buff = 1)

        label1 = MathTex("+").shift(LEFT*3.25)
        label2 = MathTex("=").shift(RIGHT*0)
        label3 = Text("Phase = ").shift(DOWN*2).scale(0.75)
        number = always_redraw(lambda:DecimalNumber(
                 phi2.get_value(), 
                 show_ellipsis=False, 
                 num_decimal_places=0
                 ))
        always(number.next_to, label3, RIGHT)

        l1 = always_redraw(lambda: 
                 a1.plot(lambda x: 
                    np.sin((2*x) + np.deg2rad(phi1.get_value())), 
                    x_range = [0,4], 
                    color = YELLOW)
                    )
        l2 = always_redraw(lambda: 
                 a2.plot(lambda x: 
                    np.sin((2*x) + np.deg2rad(phi2.get_value())), 
                    x_range = [0,4], 
                    color = YELLOW)
                    )

        l3 = always_redraw(lambda: 
                 a3.plot(lambda x: 
                    np.sin((2*x) + np.deg2rad(phi1.get_value())) + np.sin((2*x) + np.deg2rad(phi2.get_value())), 
                    x_range = [0,4], 
                    color = YELLOW)
                    )

        l4 = always_redraw(lambda: 
                 a3.plot(lambda x: 
                    np.sin((2*x) + np.deg2rad(phi1.get_value())) + np.sin((2*x) + np.deg2rad(phi2.get_value())), 
                    x_range = [0,4], 
                    color = YELLOW)
                    )
        l5 = always_redraw(lambda: 
                 a1.plot(lambda x: 
                    np.sin((2*x) + np.deg2rad(phi1.get_value())), 
                    x_range = [0,4], 
                    color = YELLOW)
                    )
        l6 = always_redraw(lambda: 
                 a2.plot(lambda x: 
                    np.sin((2*x) + np.pi + np.deg2rad(phi2.get_value())), 
                    x_range = [0,4], 
                    color = YELLOW)
                    )

        l7 = always_redraw(lambda: 
                 a3.plot(lambda x: 
                    np.sin((2*x) + np.deg2rad(phi1.get_value())) + np.sin((2*x) + np.pi +np.deg2rad(phi2.get_value())), 
                    x_range = [0,4], 
                    color = YELLOW)
                    )

        l8 = always_redraw(lambda: 
                 a3.plot(lambda x: 
                    np.sin((2*x) + np.deg2rad(phi1.get_value())) + np.sin((2*x) + np.pi + np.deg2rad(phi2.get_value())), 
                    x_range = [0,4], 
                    color = YELLOW)
                    )

        self.add(a1,a2)
        self.play(LaggedStart(Write(l1),Write(label1), Write(l2), lag_ratio=1))
        self.wait()
        self.add(a3,l3,l4)
        self.play(Write(label2), DrawBorderThenFill(a3), TransformFromCopy(l1,l3), TransformFromCopy(l2,l4))
        self.wait()
        self.play(phi2.animate.set_value(180), run_time = 2)
        self.clear()
        self.add(a1,a2)
        self.play(LaggedStart(Write(l1),Write(label1), Write(l2), lag_ratio=1))
        self.wait()
        self.add(a3,l3,l4)
        self.play(Write(label2), DrawBorderThenFill(a3), TransformFromCopy(l1,l3), TransformFromCopy(l2,l4))
        self.wait()
        self.play(phi2.animate.set_value(0), run_time = 2)
        self.wait()
        self.play(phi2.animate.set_value(360), run_time = 5)
        self.wait()


#self.clear()
        #self.play(phi2.animate.set_value(0), run_time = 1)
        #self.wait()
        #self.add(a1,a2, label3)
        #self.play(LaggedStart(Write(l5),Write(label1), Write(l6), lag_ratio = 0.1))
        #self.wait()
        #self.add(a3,l7,l8)
        #self.play(Write(label2), DrawBorderThenFill(a3), TransformFromCopy(l5,l7), TransformFromCopy(l6,l8))
        #self.wait()
       
