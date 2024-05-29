import math
from os import remove
from manim import *
import numpy as np
from numpy.lib.function_base import copy

class anim2(Scene):
    def construct(self):

        Phi1 = ValueTracker(-45.0)
        A1   = ValueTracker(0.707)
        Phi2 = ValueTracker(-135.0)
        A2   = ValueTracker(0.707)

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



        #sig1
        vect1 = always_redraw(lambda:
            Line(
            start = axis1.coords_to_point(0,0), 
            end   = axis1.polar_to_point(
                    A1.get_value(),
                    np.deg2rad(Phi1.get_value())
                    ),
            color = YELLOW        
            ).add_tip()
        )
        
        #sig2
        vect2 = always_redraw(lambda:
            Line(
            start = axis1.coords_to_point(0,0), 
            end = axis1.polar_to_point(
                    A2.get_value(),
                    np.deg2rad(Phi2.get_value())
                    ),
            color = BLUE        
            ).add_tip()
        )

        vect4 = always_redraw(lambda:
            Line(
            start = axis1.coords_to_point(0,0), 
            end = axis1.coords_to_point(
                (A1.get_value()*np.cos(np.deg2rad(Phi1.get_value()))) + (A2.get_value()*np.cos(np.deg2rad(Phi2.get_value()))),
                (A1.get_value()*np.sin(np.deg2rad(Phi1.get_value()))) + (A2.get_value()*np.sin(np.deg2rad(Phi2.get_value())))
                ),
            color = PURPLE       
            ).add_tip()
        )

        #sig2 transformed to the end of sig1 to add
        vect3 = always_redraw(lambda:
            Line(
            start = vect1.get_end(), 
            end =   axis1.coords_to_point(
                (A1.get_value()*np.cos(np.deg2rad(Phi1.get_value()))) + (A2.get_value()*np.cos(np.deg2rad(Phi2.get_value()))),
                (A1.get_value()*np.sin(np.deg2rad(Phi1.get_value()))) + (A2.get_value()*np.sin(np.deg2rad(Phi2.get_value())))
                ),
            color = WHITE        
            ).add_tip()
        )

        self.add(axis1, axis2, axis3)
        self.play(Write(sine1), GrowFromPoint(vect1, point = vect1.get_start()))
        self.wait()
        self.play(Write(sine2), GrowFromPoint(vect2, point = vect2.get_start()))
        self.wait()
        self.play(FadeTransform(vect2.copy(), vect3))
        self.wait()
        self.play(Write(vect4))
        self.wait()

        self.play(FadeOut(vect3), FadeOut(vect4))
        self.wait()
        self.play(Phi1.animate.set_value(20), Phi2.animate.set_value(110), run_time = 3)
        self.wait()

        vect6 = always_redraw(lambda:
            Line(
            start = axis1.coords_to_point(0,0), 
            end = axis1.coords_to_point(-1*
                (A1.get_value()*np.cos(np.deg2rad(Phi1.get_value()))) - (A2.get_value()*np.cos(np.deg2rad(Phi2.get_value()))),
                (A1.get_value()*np.sin(np.deg2rad(Phi1.get_value()))) - (A2.get_value()*np.sin(np.deg2rad(Phi2.get_value())))
                ),
            color = PURPLE       
            ).add_tip()
        )

        #sig2 transformed to the end of sig1 to add
        vect5 = always_redraw(lambda:
            Line(
            start = vect1.get_end(), 
            end =   axis1.coords_to_point(-1*
                (A1.get_value()*np.cos(np.deg2rad(Phi1.get_value()))) - (A2.get_value()*np.cos(np.deg2rad(Phi2.get_value()))),
                (A1.get_value()*np.sin(np.deg2rad(Phi1.get_value()))) - (A2.get_value()*np.sin(np.deg2rad(Phi2.get_value())))
                ),
            color = WHITE        
            ).add_tip()
        )

        self.play(FadeTransform(vect2.copy(), vect5))
        self.wait()
        self.play(Write(vect6))
        self.wait()
        self.play(Indicate(vect6, color=WHITE))
        self.wait()
        
        axis4 = Axes(
            x_range = [0,4,1], 
            x_length = 4, 
            y_range = [-1,1,1], 
            y_length = 1.5, 
            tips=False
            ).add_coordinates()
        axis4.to_corner(UR, buff = 1)

        axis5 = Axes(
            x_range = [0,4,1], 
            x_length = 4, 
            y_range = [-1,1,1], 
            y_length = 1.5, 
            tips=False
            ).add_coordinates()
        axis5.to_edge(RIGHT, buff = 1)

        axis6 = Axes(
            x_range = [0,4,1], 
            x_length = 4, 
            y_range = [-1,1,1], 
            y_length = 1.5, 
            tips=False
            ).add_coordinates()
        axis6.to_corner(DR, buff = 1)

        sine4 = always_redraw(lambda: 
                 axis4.plot(lambda x: 
                    A1.get_value() * (np.sin((2*x) + np.deg2rad(Phi1.get_value()))), 
                    x_range = [0,4], 
                    color = YELLOW))

        sine5 = always_redraw(lambda: 
                 axis5.plot(lambda x: 
                    A2.get_value() * (np.sin((2*x) + np.deg2rad(Phi2.get_value()))), 
                    x_range = [0,4], 
                    color = BLUE))
        sine6 = always_redraw(lambda: 
                 axis6.plot(lambda x: 
                    axis1.point_to_polar(vect6.get_end())[0]
                    * (np.sin((2*x) + (axis1.point_to_polar(vect6.get_end())[1]))
                    ), 
                    x_range = [0,4], 
                    color = PURPLE))
        
        self.play(FadeTransform(vect6.copy(), sine6),FadeTransform(sine1, sine4),FadeTransform(sine2, sine5), FadeTransform(axis2, axis4), FadeTransform(axis3, axis5), FadeIn(axis6))
        self.wait()
        self.play(Indicate(sine4, color=WHITE), Indicate(vect1, color=WHITE))
        self.wait(0.5)
        self.play(Indicate(sine5, color=WHITE), Indicate(vect2, color=WHITE))
        self.wait(0.5)
        self.play(Indicate(sine6, color=WHITE), Indicate(vect6, color=WHITE))

        self.play(A2.animate.set_value(0.1), run_time = 1)
        self.wait()
        self.play(A2.animate.set_value(0.707), run_time = 1)
        self.wait()
        self.play(A1.animate.set_value(1), Phi1.animate.set_value(0), A2.animate.set_value(0), Phi2.animate.set_value(-90), run_time = 1)
        self.wait()
        self.play(A2.animate.set_value(1), Phi2.animate.set_value(0), run_time = 5)
        self.play(A2.animate.set_value(0), Phi2.animate.set_value(-90), run_time = 5)
        