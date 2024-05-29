from manim import *

resultd1 = 0
resultd2 = 0
resultd22 = 0

def vd1(sine):
    global resultd1
    if(sine - 0.7 <= resultd1):
        resultd1 = resultd1
    else:
        if(sine<0.7):
            resultd1 = 0
        else:
            resultd1 = sine - 0.7
    return resultd1

def vd2(sine):
    global resultd2
    if(sine + 0.7 >= resultd2):
        resultd2 = resultd2
    else:
        if(sine > 0.7):
            resultd2 = 0
        else:
            resultd2 = sine + 0.7
    return resultd2

class anim(Scene):
    def construct(self):
        template = TexTemplate()
        template.add_to_preamble(r"\usepackage[siunitx, RPvoltages, american, europeanresistors]{circuitikz}")

        a = MathTex(
        r"""\draw (0,-3) to[sV, v=$$, voltage shift=1]  (0,0) (0,0) to[short] (1,0) (0,-3) to[short] (4,-3);""",
        r"""\draw (1,0)  to[diode, o-o]  (4,0); """,
        r"""\draw (4,0)  to[C, o-o , v^=$$, voltage shift=1]  (4,-3); """,
        r"""\draw (4,-6) to[diode, o-o]  (1,-6); """,
        r"""\draw (4,-3) to[C, o-o , v^=$$, voltage shift=1]  (4,-6); """,
        r"""\draw (1,-6) to[short, o-o] (1,0); """,
        r"""\draw (0,-3) node[ground]{}; """,
        stroke_width=2,
        fill_opacity=0,
        stroke_opacity=1,
        tex_environment="circuitikz",
        tex_template=template,
        ).scale(0.7)

        a2 = MathTex(
        r"""\draw (0,-3) to[sV, v=$$, voltage shift=1]  (0,0) (0,0) to[short] (1,0) (0,-3) to[short] (4,-3);""",
        r"""\draw (1,0)  to[diode, o-o]  (4,0); """,
        r"""\draw (4,0)  to[C, o-o , v^=$$, voltage shift=1]  (4,-3); """,
        r"""\draw (4,-6) to[diode, o-o]  (1,-6); """,
        r"""\draw (4,-3) to[C, o-o , v^=$$, voltage shift=1]  (4,-6); """,
        r"""\draw (1,-6) to[short, o-o] (1,0); """,
        r"""\draw (0,-3) node[ground]{}; """,
        stroke_width=2,
        fill_opacity=0,
        stroke_opacity=1,
        tex_environment="circuitikz",
        tex_template=template,
        ).scale(0.7)

        a3 = MathTex(
        r"""\draw (0,-3) to[sV, v=$$, voltage shift=1]  (0,0) (0,0) to[short] (1,0) (0,-3) to[short] (4,-3);""",
        r"""\draw (1,0)  to[open, o-o]  (4,0); """,
        r"""\draw (4,0)  to[C, o-o , v^=$$, voltage shift=1]  (4,-3); """,
        r"""\draw (4,-6) to[diode, o-o]  (1,-6); """,
        r"""\draw (4,-3) to[C, o-o , v^=$$, voltage shift=1]  (4,-6); """,
        r"""\draw (1,-6) to[short, o-o] (1,0); """,
        r"""\draw (0,-3) node[ground]{}; """,
        stroke_width=2,
        fill_opacity=0,
        stroke_opacity=1,
        tex_environment="circuitikz",
        tex_template=template,
        ).scale(0.7)

        draw = ValueTracker(0.00001)

        c11 = always_redraw(lambda:DecimalNumber(
                 vd1(21.2*np.sin((3 * draw.get_value()) + np.deg2rad(0))), 
                 show_ellipsis=False, 
                 num_decimal_places=1,
                 include_sign = False
                 ).next_to(a[2], RIGHT))
        c11_lab = always_redraw(lambda :MathTex("V").next_to(c11, RIGHT))
        c21 = always_redraw(lambda:DecimalNumber(
                 vd2(21.2*np.sin((3 * draw.get_value()) + np.deg2rad(0))), 
                 show_ellipsis=False, 
                 num_decimal_places=1,
                 include_sign = False
                 ).next_to(a[4], RIGHT))
        c21_lab = always_redraw(lambda :MathTex("V").next_to(c21, RIGHT))


        ax1 = (
            NumberPlane(x_range=[0, 4.29, 1], x_length=2.5, y_range=[-1, 1, 1], y_length=1)
        ).next_to(a[0], LEFT, buff = 0.5)
        sin1 = always_redraw(lambda: 
                 ax1.plot(lambda x: 
                    np.sin((3 * x) + np.deg2rad(0)), 
                    x_range = [0,draw.get_value()], 
                    color = YELLOW))
        dot1 = always_redraw(lambda: 
                    Dot(point = sin1.get_end())
                 )
        b1 = RoundedRectangle(corner_radius=0.2,width=2.5, height = 1.25).move_to(ax1)
        l1 = Line(start=b1.get_critical_point(LEFT), end=b1.get_critical_point(RIGHT),color = BLUE_C, stroke_width = 2, stroke_opacity = 1)
        a1 = always_redraw(lambda:DecimalNumber(
                 21.2*(np.sin((3 * draw.get_value()) + np.deg2rad(0))), 
                 show_ellipsis=False, 
                 num_decimal_places=1,
                 include_sign = False
                 ).next_to(ax1, UP))
        a1_lab = always_redraw(lambda:MathTex("V").next_to(a1, RIGHT))
        sine1 = VGroup(sin1,b1,l1,dot1,a1,a1_lab)

        self.play(FadeIn(a,sine1,c11,c21,c11_lab,c21_lab))
        self.wait(0.2)

        b = MathTex(
        r"""\draw (0,-3) to[sV, v=$$, voltage shift=1]  (0,0) (0,0) to[short] (1,0) (0,-3) to[short] (4,-3);""",
        r"""\draw (1,0)  to[short, v = $0.7v$, o-o]  (4,0); """,
        r"""\draw (4,0)  to[C, o-o , v^=$$, voltage shift=1]  (4,-3); """,
        r"""\draw (4,-6) to[open, o-o]  (1,-6); """,
        r"""\draw (4,-3) to[C, o-o , v^=$$, voltage shift=1]  (4,-6); """,
        r"""\draw (1,-6) to[short, o-o] (1,0); """,
        r"""\draw (0,-3) node[ground]{}; """,
        stroke_width=2,
        fill_opacity=0,
        stroke_opacity=1,
        tex_environment="circuitikz",
        tex_template=template,
        ).scale(0.7)

        c1 = MathTex(
        r"""\draw (0,-3) to[sV, v=$$, voltage shift=1]  (0,0) (0,0) to[short] (1,0) (0,-3) to[short] (4,-3);""",
        r"""\draw (1,0)  to[open, o-o]  (4,0); """,
        r"""\draw (4,0)  to[C, o-o , v^=$$, voltage shift=1]  (4,-3); """,
        r"""\draw (4,-6) to[open, o-o]  (1,-6); """,
        r"""\draw (4,-3) to[C, o-o , v^=$$, voltage shift=1]  (4,-6); """,
        r"""\draw (1,-6) to[short, o-o] (1,0); """,
        r"""\draw (0,-3) node[ground]{}; """,
        stroke_width=2,
        fill_opacity=0,
        stroke_opacity=1,
        tex_environment="circuitikz",
        tex_template=template,
        ).scale(0.7)

        c2 = MathTex(
        r"""\draw (0,-3) to[sV, v=$$, voltage shift=1]  (0,0) (0,0) to[short] (1,0) (0,-3) to[short] (4,-3);""",
        r"""\draw (1,0)  to[open, o-o]  (4,0); """,
        r"""\draw (4,0)  to[C, o-o , v^=$$, voltage shift=1]  (4,-3); """,
        r"""\draw (4,-6) to[short, v = $0.7v$, o-o]  (1,-6); """,
        r"""\draw (4,-3) to[C, o-o , v^=$$, voltage shift=1]  (4,-6); """,
        r"""\draw (1,-6) to[short, o-o] (1,0); """,
        r"""\draw (0,-3) node[ground]{}; """,
        stroke_width=2,
        fill_opacity=0,
        stroke_opacity=1,
        tex_environment="circuitikz",
        tex_template=template,
        ).scale(0.7)

        self.play(draw.animate.set_value(0.0115))
        self.wait(0.2)
        self.play(Transform(a,b))
        self.wait(0.2)

        aniline1 = Line(start= UP*3+LEFT*1.775,
        end = UP*3+RIGHT*2.2,
        stroke_width=0
            )
        aniline2 = Line(start= UP*3+RIGHT*2.2,
        end = UP*0+RIGHT*2.2,
        stroke_width=0
            )
        aniline3 = Line(start= UP*0+RIGHT*2.2,
        end = UP*0+LEFT*1.775,
        stroke_width=0
            )
        aniline4 = Line(start = UP*0+LEFT*1.775,
        end = UP*3+LEFT*1.775,
        stroke_width=0
            )

        animdot=Dot(radius=0).move_to(aniline1.get_start()) 
        i_arr1 = always_redraw(lambda:
           Arrow(start = animdot.get_center()-[0.75,0,0],end = animdot.get_center()+[0.75,0,0],stroke_width=10, 
           max_stroke_width_to_length_ratio=100, max_tip_length_to_length_ratio=100, color = RED).move_to(animdot)
           )
        
        resultd1 = 0
        resultd2 = 0

        self.play(FadeIn(i_arr1, aniline1, animdot))
        self.wait(0.2)
        self.play(MoveAlongPath(animdot, aniline1), run_time=1)
        i_arr2 = always_redraw(lambda:
           Arrow(start = animdot.get_center()+[0,0.75,0],end = animdot.get_center()-[0,0.75,0],stroke_width=10, 
           max_stroke_width_to_length_ratio=100, max_tip_length_to_length_ratio=100, color = RED).move_to(animdot)
           )
        self.play(ReplacementTransform(i_arr1, i_arr2), run_time=0.25)
        self.play(MoveAlongPath(animdot, aniline2), draw.animate.set_value(PI/6), run_time=2)
        i_arr3 = always_redraw(lambda:
           Arrow(start = animdot.get_center()+[0.75,0,0],end = animdot.get_center()-[0.75,0,0],stroke_width=10, 
           max_stroke_width_to_length_ratio=100, max_tip_length_to_length_ratio=100, color = RED).move_to(animdot)
           )
        self.play(ReplacementTransform(i_arr2, i_arr3), run_time=0.25)
        self.play(MoveAlongPath(animdot, aniline3), run_time=1)
        i_arr4 = always_redraw(lambda:
           Arrow(start = animdot.get_center()-[0,0.75,0],end = animdot.get_center()+[0,0.75,0],stroke_width=10, 
           max_stroke_width_to_length_ratio=100, max_tip_length_to_length_ratio=100, color = RED).move_to(animdot)
           )
        self.play(ReplacementTransform(i_arr3, i_arr4), run_time=0.5)
        self.play(MoveAlongPath(animdot, aniline4), run_time=1)
        self.play(FadeOut(i_arr4))
        self.wait(0.2)

        self.play(draw.animate.set_value(PI/6), run_time = 3)
        self.wait(0.2)


        self.play(Transform(a,a2))
        self.wait(0.2)
        self.play(draw.animate.set_value((PI/6)+0.033), run_time = 1)
        self.wait(0.2)
        self.play(Transform(a, c1))
        self.wait(0.2)
        self.play(draw.animate.set_value(PI/3), run_time = 3)
        self.wait(0.2)

        self.play(Transform(a,a3))
        self.wait(0.2)

        self.play(draw.animate.set_value(PI/3+0.0115), run_time = 1.5)
        self.wait(0.2)
        self.play(Transform(a, c2))
        self.wait(0.2)

        aniline11 = Line(start= UP*2.975+LEFT*1.75,
        end = UP*2.975+LEFT*0.8,
        stroke_width=0
            )
        aniline12 = Line(start= UP*2.975+LEFT*0.8,
        end = DOWN*2.975+LEFT*0.8,
        stroke_width=0
            )
        aniline13 = Line(start= DOWN*2.975+LEFT*0.8,
        end = DOWN*2.975+RIGHT*2.2,
        stroke_width=0
            )
        aniline14 = Line(start= DOWN*2.975+RIGHT*2.2,
        end = RIGHT*2.2,
        stroke_width=0
            )
        aniline15 = Line(start= RIGHT*2.2,
        end = LEFT*1.75,
        stroke_width=0
            )
        aniline16 = Line(start= LEFT*1.75,
        end = UP*2.975+LEFT*1.75,
        stroke_width=0
            )

        animdot2=Dot(radius=0).move_to(aniline11.get_start()) 

        i_arr11 = always_redraw(lambda:
           Arrow(start = animdot2.get_center()-[0.75,0,0],end = animdot2.get_center()+[0.75,0,0],stroke_width=10, 
           max_stroke_width_to_length_ratio=100, max_tip_length_to_length_ratio=100, color = BLUE).move_to(animdot2)
           )
        self.play(FadeIn(i_arr11, aniline11, animdot2))
        self.wait(0.2)
        self.play(MoveAlongPath(animdot2, aniline11), run_time=1)

        i_arr12 = always_redraw(lambda:
           Arrow(start = animdot2.get_center()+[0,0.75,0],end = animdot2.get_center()-[0,0.75,0],stroke_width=10, 
           max_stroke_width_to_length_ratio=100, max_tip_length_to_length_ratio=100, color = BLUE).move_to(animdot2)
           )
        self.play(ReplacementTransform(i_arr11, i_arr12), run_time=0.25)
        self.play(MoveAlongPath(animdot2, aniline12), run_time=1)

        i_arr13 = always_redraw(lambda:
           Arrow(start = animdot2.get_center()-[0.75,0,0],end = animdot2.get_center()+[0.75,0,0],stroke_width=10, 
           max_stroke_width_to_length_ratio=100, max_tip_length_to_length_ratio=100, color = BLUE).move_to(animdot2)
           )
        self.play(ReplacementTransform(i_arr12, i_arr13), run_time=0.25)
        self.play(MoveAlongPath(animdot2, aniline13), run_time=1)

        i_arr14 = always_redraw(lambda:
           Arrow(start = animdot2.get_center()-[0,0.75,0],end = animdot2.get_center()+[0,0.75,0],stroke_width=10, 
           max_stroke_width_to_length_ratio=100, max_tip_length_to_length_ratio=100, color = BLUE).move_to(animdot2)
           )
        self.play(ReplacementTransform(i_arr13, i_arr14), run_time=0.25)
        self.play(MoveAlongPath(animdot2, aniline14),draw.animate.set_value(3*PI/6), run_time=2)

        i_arr15 = always_redraw(lambda:
           Arrow(start = animdot2.get_center()+[0.75,0,0],end = animdot2.get_center()-[0.75,0,0],stroke_width=10, 
           max_stroke_width_to_length_ratio=100, max_tip_length_to_length_ratio=100, color = BLUE).move_to(animdot2)
           )
        self.play(ReplacementTransform(i_arr14, i_arr15), run_time=0.25)
        self.play(MoveAlongPath(animdot2, aniline15), run_time=1)

        i_arr16 = always_redraw(lambda:
           Arrow(start = animdot2.get_center()-[0,0.75,0],end = animdot2.get_center()+[0,0.75,0],stroke_width=10, 
           max_stroke_width_to_length_ratio=100, max_tip_length_to_length_ratio=100, color = BLUE).move_to(animdot2)
           )
        self.play(ReplacementTransform(i_arr15, i_arr16), run_time=0.25)
        self.play(MoveAlongPath(animdot2, aniline16), run_time=1)
        self.wait(0.2)
        self.play(FadeOut(i_arr16))
        self.wait(0.2)

        



