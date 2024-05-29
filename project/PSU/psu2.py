from manim import *
import math
prev = 0
result = 0
peak = 0
t = 0
def ripple(func = 0):
    global prev
    global result
    global peak
    global t
    if func>prev:
        result = func
        t = 0
        prev = result
        peak = func
    else:
        result = peak*math.exp(-t/0.55)
        t = t + 0.0165 
        prev = result
    return result

class anim(Scene):
    def construct(self):
        template = TexTemplate()
        template.add_to_preamble(r"\usepackage[siunitx, RPvoltages, american, europeanresistors]{circuitikz}")
        
        phi = ValueTracker(0)
        
        ax1 = (
            NumberPlane(x_range=[0, 4, 1], x_length=2.5, y_range=[-1, 1, 1], y_length=1)
        ).shift(LEFT*5 + UP*1.5)
        sine = always_redraw(lambda: 
                 ax1.plot(lambda x: 
                    np.sin((3 * x) + np.deg2rad(phi.get_value())), 
                    x_range = [0,4], 
                    color = YELLOW))
        b1 = RoundedRectangle(corner_radius=0.2,width=2.5, height = 1.25).move_to(ax1)
        l1 = Line(start=b1.get_critical_point(LEFT), end=b1.get_critical_point(RIGHT),color = BLUE_C, stroke_width = 2, stroke_opacity = 1)
        sine1 = VGroup(sine,b1,l1)
        
        ax2 = (
            NumberPlane(x_range=[0, 4, 1], x_length=2.5, y_range=[-1, 1, 1], y_length=1)
        ).shift(LEFT*1.75 + UP*1.5)
        sin2 = always_redraw(lambda: 
                 ax2.plot(lambda x: 
                    abs(np.sin((3 * x) + np.deg2rad(phi.get_value()))), 
                    x_range = [0,4], 
                    color = PURPLE))
        b2 = RoundedRectangle(corner_radius=0.2,width=2.5, height = 1.25).move_to(ax2)
        l2 = Line(start=b2.get_critical_point(LEFT), end=b2.get_critical_point(RIGHT),color = BLUE_C, stroke_width = 2, stroke_opacity = 1)
        sine2 = VGroup(sin2,b2,l2)
        
        ax3 = (
            NumberPlane(x_range=[0, 4, 1], x_length=2.5, y_range=[-1, 1, 1], y_length=1)
        ).shift(RIGHT*1.75 + UP*1.5)
        sin3 = always_redraw(lambda: 
                 ax3.plot(lambda x: 
                    ripple(abs(np.sin((3 * x) + np.deg2rad(phi.get_value())))), 
                    x_range = [0,4], 
                    color = RED))
        b3 = RoundedRectangle(corner_radius=0.2,width=2.5, height = 1.25).move_to(ax3)
        l3 = Line(start=b3.get_critical_point(LEFT), end=b3.get_critical_point(RIGHT),color = BLUE_C, stroke_width = 2, stroke_opacity = 1)
        sine3 = VGroup(sin3,b3,l3)
        
       
        ax4 = (
            NumberPlane(x_range=[0, 4, 1], x_length=2.5, y_range=[-1, 1, 1], y_length=1)
        ).shift(RIGHT*5 + UP*1.5)
        sin4 = always_redraw(lambda: 
                 ax4.plot(lambda x: 
                   0.9, 
                    x_range = [0,4], 
                    color = MAROON))
        b4 = RoundedRectangle(corner_radius=0.2,width=2.5, height = 1.25).move_to(ax4)
        l4 = Line(start=b4.get_critical_point(LEFT), end=b4.get_critical_point(RIGHT),color = BLUE_C, stroke_width = 2, stroke_opacity = 1)
        sine4 = VGroup(sin4,b4,l4)
        
        rect_box = RoundedRectangle(
            corner_radius=0.2,
            width=3, height = 2,
            fill_color = PURPLE_B,
            fill_opacity = (0.7)
            ).shift(LEFT*3.5+DOWN)
        rect_l = Tex("Rectify").move_to(rect_box).shift(UP*0.5)
        rect_l2 = MathTex(r"""\draw (-2,0) to[diode] (0,0);""",
        stroke_width=2,
        fill_opacity=0.4,
        stroke_opacity=0.4,
        tex_environment="circuitikz",
        tex_template=template
        ).move_to(rect_box).shift(DOWN*0.4).scale(0.7)
        rectify = VGroup(rect_box, rect_l, rect_l2)

        filt_box = RoundedRectangle(
            corner_radius=0.2,
            width=3, height = 2,
            fill_color = RED_B,
            fill_opacity = (0.7)
            ).shift(DOWN)
        filt_l = Tex("Filter").move_to(filt_box).shift(UP*0.5)
        filt_l2 = MathTex(r"""\draw (-2,0) to[C] (0,0);""",
        stroke_width=2,
        fill_opacity=0.4,
        stroke_opacity=0.4,
        tex_environment="circuitikz",
        tex_template=template
        ).move_to(filt_box).shift(DOWN*0.4).scale(0.7)
        filter = VGroup(filt_box, filt_l, filt_l2)

        reg_box = RoundedRectangle(
            corner_radius=0.2,
            width=3, height = 2,
            fill_color = MAROON_B,
            fill_opacity = (0.7)
            ).shift(RIGHT*3.5+DOWN)
        reg_l = Tex("Regulate").move_to(reg_box).shift(UP*0.5)
        reg_l2 = MathTex(r"""\draw (-2,0) to[short] ++(0.25,0) node[op amp, noinv input down, anchor=-] (OA){\texttt{}}
                                   (OA.+) to[short] ++(-0.25,0);""",
        stroke_width=2,
        fill_opacity=0.4,
        stroke_opacity=0.4,
        tex_environment="circuitikz",
        tex_template=template
        ).move_to(reg_box).shift(DOWN*0.4).scale(0.35)
        regulate = VGroup(reg_box, reg_l, reg_l2)
        
        a1 = Arrow(start = ax1.get_critical_point(DOWN)+[0,-0.25,0], end = rect_box.get_critical_point(UP)+[0,0.1,0],
                   fill_color = YELLOW,
                   stroke_color = YELLOW,
                   stroke_width = 3)

        a2 = Arrow(start = rect_box.get_critical_point(UP)+[0,0.1,0], end = ax2.get_critical_point(DOWN)+[0,-0.25,0],
                   fill_color = PURPLE,
                   stroke_color = PURPLE,
                   stroke_width = 3)

        a3 = Arrow(start = ax2.get_critical_point(DOWN)+[0,-0.25,0], end = filt_box.get_critical_point(UP)+[0,0.1,0],
                   fill_color = PURPLE,
                   stroke_color = PURPLE,
                   stroke_width = 3)

        a4 = Arrow(start = filt_box.get_critical_point(UP)+[0,0.1,0], end = ax3.get_critical_point(DOWN)+[0,-0.25,0],
                   fill_color = RED,
                   stroke_color = RED,
                   stroke_width = 3)

        a5 = Arrow(start = ax3.get_critical_point(DOWN)+[0,-0.25,0], end = reg_box.get_critical_point(UP)+[0,0.1,0],
                   fill_color = RED,
                   stroke_color = RED,
                   stroke_width = 3)

        a6 = Arrow(start = reg_box.get_critical_point(UP)+[0,0.1,0], end = ax4.get_critical_point(DOWN)+[0,-0.25,0],
                   fill_color = MAROON,
                   stroke_color = MAROON,
                   stroke_width = 3)

        self.play(FadeIn(sine1), run_time = 0.01)
        self.play(phi.animate.set_value(360*2), run_time = 3, rate_func = linear)
        self.play(LaggedStart(FadeIn(a1),FadeIn(rectify),lag_ratio=0.6), phi.animate.set_value(360*3), run_time = 1.5, rate_func = linear)
        self.play(FadeIn(a2), phi.animate.set_value(360*3.5), run_time = 0.75, rate_func = linear)
        self.play(phi.animate.set_value(360*4), run_time = 0.75, rate_func = linear)
        self.play(FadeIn(sine2), run_time = 0.01)
        self.play(phi.animate.set_value(360*5), run_time = 1.5, rate_func = linear)
        self.play(LaggedStart(FadeIn(a3),FadeIn(filter),lag_ratio=0.6), phi.animate.set_value(360*6), run_time = 1.5, rate_func = linear)
        self.play(FadeIn(a4), phi.animate.set_value(360*6.5), run_time = 0.75, rate_func = linear)
        self.play(phi.animate.set_value(360*7), run_time = 0.75, rate_func = linear)
        self.play(FadeIn(sine3), run_time = 0.01)
        self.play(phi.animate.set_value(360*8), run_time = 1.5, rate_func = linear)
        self.play(LaggedStart(FadeIn(a5),FadeIn(regulate),lag_ratio=0.6), phi.animate.set_value(360*9), run_time = 1.5, rate_func = linear)
        self.play(FadeIn(a6), phi.animate.set_value(360*9.5), run_time = 0.75, rate_func = linear)
        self.play(phi.animate.set_value(360*10), run_time = 0.75, rate_func = linear)
        self.play(FadeIn(sine4), run_time = 0.01)
        self.play(phi.animate.set_value(360*11), run_time = 1.5, rate_func = linear)
        self.play(phi.animate.set_value(360*13), run_time = 3, rate_func = linear)
        self.wait(0.2)
        
