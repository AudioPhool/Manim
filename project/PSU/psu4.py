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

def vd22(sine):
    global resultd22
    if(sine + 0.7 >= resultd22):
        resultd22 = resultd22
    else:
        if(sine > 0.7):
            resultd22 = 0
        else:
            resultd22 = sine + 0.7
    return resultd22

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
        stroke_width=2,
        fill_opacity=0,
        stroke_opacity=1,
        tex_environment="circuitikz",
        tex_template=template,
        ).scale(0.7)

        b = MathTex(
        r"""\draw (0,-3) to[sV, v=$$, voltage shift=1]  (0,0) (0,0) to[short] (1,0) (0,-3) to[short] (4,-3);""",
        r"""\draw (1,0)  to[short, o-o, v = $0.7v$]  (4,0); """,
        r"""\draw (4,0)  to[C, o-o , v^=$$, voltage shift=1]  (4,-3); """,
        r"""\draw (4,-6) to[diode, o-o]  (1,-6); """,
        r"""\draw (4,-3) to[C, o-o , v^=$$, voltage shift=1]  (4,-6); """,
        r"""\draw (1,-6) to[short, o-o] (1,0); """,
        stroke_width=2,
        fill_opacity=0,
        stroke_opacity=1,
        tex_environment="circuitikz",
        tex_template=template,
        ).scale(0.7).shift(DOWN*0.15)

        d = MathTex(
        r"""\draw (0,-3) to[sV, v=$$, voltage shift=1]  (0,0) (0,0) to[short] (1,0) (0,-3) to[short] (4,-3);""",
        r"""\draw (1,0)  to[short, o-o, v = $0.7v$]  (4,0); """,
        r"""\draw (4,0)  to[C, o-o , v^=$$, voltage shift=1]  (4,-3); """,
        r"""\draw (4,-6) to[open, o-o]  (1,-6); """,
        r"""\draw (4,-3) to[C, o-o , v^=$$, voltage shift=1]  (4,-6); """,
        r"""\draw (1,-6) to[short, o-o] (1,0); """,
        stroke_width=2,
        fill_opacity=0,
        stroke_opacity=1,
        tex_environment="circuitikz",
        tex_template=template,
        ).scale(0.7)

        c = MathTex(
        r"""\draw (0,-3) to[sV, v=$$, voltage shift=1]  (0,0) (0,0) to[short] (1,0) (0,-3) to[short] (4,-3);""",
        r"""\draw (1,0)  to[short, o-o, v = $0.7v$]  (4,0); """,
        r"""\draw (4,0)  to[C, o-o , v^=$$, voltage shift=1]  (4,-3); """,
        stroke_width=2,
        fill_opacity=0,
        stroke_opacity=1,
        tex_environment="circuitikz",
        tex_template=template,
        ).scale(1).shift(RIGHT*0.5)

        self.play(FadeIn(a))
        self.wait(0.2)
        self.play(LaggedStart(Indicate(a[1], color = RED_C),Indicate(a[3], color = RED_C), lag_ratio = 0.25))
        self.wait(0.2)
        self.play(LaggedStart(Indicate(a[2], color = GOLD_C),Indicate(a[4], color = GOLD_C), lag_ratio = 0.25))
        self.wait(0.2)

        draw = ValueTracker(0.001)

        ax1 = (
            NumberPlane(x_range=[0, 4.29, 1], x_length=2.5, y_range=[-1, 1, 1], y_length=1)
        ).next_to(a[0], LEFT, buff = 1)
        sine = always_redraw(lambda: 
                 ax1.plot(lambda x: 
                    np.sin((3 * x) + np.deg2rad(0)), 
                    x_range = [0,draw.get_value()], 
                    color = YELLOW))
        dot1 = always_redraw(lambda: 
                    Dot(point = sine.get_end())
                 )
        b1 = RoundedRectangle(corner_radius=0.2,width=2.5, height = 1.25).move_to(ax1)
        l1 = Line(start=b1.get_critical_point(LEFT), end=b1.get_critical_point(RIGHT),color = BLUE_C, stroke_width = 2, stroke_opacity = 1)
        sine1 = VGroup(sine,b1,l1,dot1)

        ax2 = (
            NumberPlane(x_range=[0, 4.29, 1], x_length=2.5, y_range=[-1, 1, 1], y_length=1)
        ).next_to(c[0], LEFT, buff = 0.5)
        sin2 = always_redraw(lambda: 
                 ax2.plot(lambda x: 
                    np.sin((3 * x) + np.deg2rad(0)), 
                    x_range = [0,draw.get_value()], 
                    color = YELLOW))
        dot2 = always_redraw(lambda: 
                    Dot(point = sin2.get_end())
                 )
        b2 = RoundedRectangle(corner_radius=0.2,width=2.5, height = 1.25).move_to(ax2)
        l2 = Line(start=b2.get_critical_point(LEFT), end=b2.get_critical_point(RIGHT),color = BLUE_C, stroke_width = 2, stroke_opacity = 1) 
        sine2 = VGroup(sin2,b2,l2,dot2)

        self.play(FadeIn(sine1))
        self.wait(0.2)
        self.play(draw.animate.set_value(4/3*PI), run_time = 3)
        self.wait(0.2)
        self.play(draw.animate.set_value(0.0001), run_time = 3)
        self.wait(0.2)

        a1 = always_redraw(lambda:DecimalNumber(
                 np.sin((3 * draw.get_value()) + np.deg2rad(0)), 
                 show_ellipsis=False, 
                 num_decimal_places=1,
                 include_sign = False
                 ).next_to(ax1, UP))
        a1_lab = MathTex("V").next_to(a1, RIGHT).shift(LEFT*0.15)

        a2 = always_redraw(lambda:DecimalNumber(
                 21.2*np.sin((3 * draw.get_value()) + np.deg2rad(0)), 
                 show_ellipsis=False, 
                 num_decimal_places=1,
                 include_sign = False
                 ).next_to(ax2, UP))
        a2_lab = MathTex("V").next_to(a2, RIGHT)

        c1 = always_redraw(lambda:DecimalNumber(
                 0, 
                 show_ellipsis=False, 
                 num_decimal_places=1,
                 include_sign = False
                 ).next_to(a[2], RIGHT))
        c1_lab = MathTex("V").next_to(c1, RIGHT).shift(LEFT*0.15)
        c2 = always_redraw(lambda:DecimalNumber(
                 0, 
                 show_ellipsis=False, 
                 num_decimal_places=1,
                 include_sign = False
                 ).next_to(a[4], RIGHT))
        c2_lab = MathTex("V").next_to(c2, RIGHT)
        

        self.play(FadeIn(c1,c1_lab,a1,a1_lab,c2,c2_lab), run_time = 2)
        self.wait(0.2)
        self.play(draw.animate.set_value(0.28), run_time = 3)
        self.wait(0.2)
        self.play(Indicate(a[1], color = TEAL))
        self.wait(0.2)
        self.play(Transform(a,b), run_time = 2)
        self.wait(0.2)
        self.play(Indicate(a[3], color = TEAL))
        self.wait(0.2)
        self.play(Transform(a,d),draw.animate.set_value(0.0001), run_time = 2)
        self.wait(0.2)
        c12 = always_redraw(lambda:DecimalNumber(
                 vd1(21.2*np.sin((3 * draw.get_value()) + np.deg2rad(0))), 
                 show_ellipsis=False, 
                 num_decimal_places=1,
                 include_sign = False
                 ).next_to(c[2], RIGHT))
        c12_lab = MathTex("V").next_to(c12, RIGHT)

        
        self.play(FadeTransform(a,c),
                  FadeTransform(c1,c12),FadeTransform(c1_lab,c12_lab),
                  FadeTransform(a1,a2),FadeTransform(a1_lab,a2_lab),
                  FadeTransform(sine1, sine2),FadeOut(c2_lab, c2), 
                  run_time = 2)
        self.wait(0.2)

        d1 = Dot(point = UP*2.125+RIGHT*3.6)

        aniline1 = Line(start= UP*2.125+LEFT*2.05,
        end = UP*2.125+RIGHT*3.6,
        stroke_width=0
            )
        aniline2 = Line(start= UP*2.125+RIGHT*3.6,
        end = DOWN*2.15+RIGHT*3.6,
        stroke_width=0
            )
        aniline3 = Line(start= DOWN*2.15+RIGHT*3.6,
        end = DOWN*2.15+LEFT*2.05,
        stroke_width=0
            )
        aniline4 = Line(DOWN*2.15+LEFT*2.05,
        end = UP*2.125+LEFT*2.05,
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
        self.play(draw.animate.set_value(PI/3), rate_func = linear)
        self.wait(0.2)
        
        e = MathTex(
        r"""\draw (0,-3) to[sV, v=$$, voltage shift=1]  (0,0) (0,0) to[short] (1,0) (0,-3) to[short] (4,-3);""",
        r"""\draw (1,0)  to[diode, o-o]  (4,0); """,
        r"""\draw (4,0)  to[C, o-o , v^=$$, voltage shift=1]  (4,-3); """,
        r"""\draw (4,-6) to[diode, o-o]  (1,-6); """,
        r"""\draw (4,-3) to[C, o-o , v^=$$, voltage shift=1]  (4,-6); """,
        r"""\draw (1,-6) to[short, o-o] (1,0); """,
        stroke_width=2,
        fill_opacity=0,
        stroke_opacity=1,
        tex_environment="circuitikz",
        tex_template=template,
        ).scale(0.7)

        f = MathTex(
        r"""\draw (0,-3) to[sV, v=$$, voltage shift=1]  (0,0) (0,0) to[short] (1,0) (0,-3) to[short] (4,-3);""",
        r"""\draw (1,0)  to[open, o-o]  (4,0); """,
        r"""\draw (4,0)  to[C, o-o , v^=$$, voltage shift=1]  (4,-3); """,
        r"""\draw (4,-6) to[short, o-o]  (1,-6); """,
        r"""\draw (4,-3) to[C, o-o , v^=$$, voltage shift=1]  (4,-6); """,
        r"""\draw (1,-6) to[short, o-o] (1,0); """,
        stroke_width=2,
        fill_opacity=0,
        stroke_opacity=1,
        tex_environment="circuitikz",
        tex_template=template,
        ).scale(0.7)

        ax3 = (
            NumberPlane(x_range=[0, 4.29, 1], x_length=2.5, y_range=[-1, 1, 1], y_length=1)
        ).next_to(c[0], LEFT, buff = 0.5)
        sin3 = always_redraw(lambda: 
                 ax3.plot(lambda x: 
                    np.sin((3 * x) + np.deg2rad(0)), 
                    x_range = [0,draw.get_value()], 
                    color = YELLOW))
        dot3 = always_redraw(lambda: 
                    Dot(point = sin3.get_end())
                 )
        b3 = RoundedRectangle(corner_radius=0.2,width=2.5, height = 1.25).move_to(ax3)
        l3 = Line(start=b3.get_critical_point(LEFT), end=b3.get_critical_point(RIGHT),color = BLUE_C, stroke_width = 2, stroke_opacity = 1) 
        sine3 = VGroup(sin3,b3,l3,dot3)

        a3 = always_redraw(lambda:DecimalNumber(
                 np.sin((3 * draw.get_value()) + np.deg2rad(0)), 
                 show_ellipsis=False, 
                 num_decimal_places=1,
                 include_sign = False
                 ).next_to(ax3, UP))
        a3_lab = MathTex("V").next_to(a3, RIGHT)

        c13 = always_redraw(lambda:DecimalNumber(
                 vd1(21.2*np.sin((3 * draw.get_value()) + np.deg2rad(0))), 
                 show_ellipsis=False, 
                 num_decimal_places=1,
                 include_sign = False
                 ).next_to(f[2], RIGHT))
        c13_lab = always_redraw(lambda :MathTex("V").next_to(c13, RIGHT))

        c22 = always_redraw(lambda:DecimalNumber(
                 vd2(np.sin((3 * draw.get_value()) + np.deg2rad(0))), 
                 show_ellipsis=False, 
                 num_decimal_places=1,
                 include_sign = False
                 ).next_to(f[4], RIGHT))
        c22_lab = always_redraw(lambda :MathTex("V").next_to(c22, RIGHT))


        self.play(FadeTransform(c,e), FadeTransform(c12,c13), FadeTransform(c12_lab,c13_lab),FadeIn(c22,c22_lab), 
                  FadeTransform(a2,a3), FadeTransform(a2_lab,a3_lab),FadeTransform(sine2,sine3),run_time = 2)
        self.wait(0.2)
        self.play(draw.animate.set_value(PI/3+0.28))
        self.wait(0.2)
        self.play(Transform(e,f),draw.animate.set_value(PI/3))
        c23 = always_redraw(lambda:DecimalNumber(
                 vd2(21.2*np.sin((3 * draw.get_value()) + np.deg2rad(0))), 
                 show_ellipsis=False, 
                 num_decimal_places=1,
                 include_sign = False
                 ).next_to(f[4], RIGHT))
        c23_lab = always_redraw(lambda :MathTex("V").next_to(c23, RIGHT))
        
        self.play(FadeTransform(c22,c23), FadeTransform(c22_lab,c23_lab),
                  FadeTransform(a3,a2), FadeTransform(a3_lab,a2_lab),FadeTransform(sine3,sine2), run_time = 2)
        self.wait(0.2)
                
        d1 = Dot(point = DOWN*0+RIGHT*2.2)

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

        g = MathTex(
        r"""\draw (0,-3) node[ground]{} (0,-3)  to[sV, v=$$, voltage shift=1]  (0,0) (0,0) to[short] (1,0) (0,-3) to[short] (4,-3);""",
        r"""\draw (1,0)  to[open, o-o]  (4,0); """,
        r"""\draw (4,0)  to[C, o-o , v^=$$, voltage shift=1]  (4,-3); """,
        r"""\draw (4,-6) to[short, o-o]  (1,-6); """,
        r"""\draw (4,-3) to[C, o-o , v^=$$, voltage shift=1]  (4,-6); """,
        r"""\draw (0,-3) node[ground]{}; """,
        stroke_width=2,
        fill_opacity=0,
        stroke_opacity=1,
        tex_environment="circuitikz",
        tex_template=template,
        ).scale(0.7)

        self.play(FadeTransform(f,g),draw.animate.set_value(2*PI/6))
        self.wait(0.2)
        
        c24 = always_redraw(lambda:DecimalNumber(
                 vd22(21.2*np.sin((3 * draw.get_value()) + np.deg2rad(0))), 
                 show_ellipsis=False, 
                 num_decimal_places=1,
                 include_sign = False
                 ).next_to(f[4], RIGHT))
        c24_lab = always_redraw(lambda :MathTex("V").next_to(c24, RIGHT))
        
        self.play(Indicate(g[5]), FadeTransform(c23,c24), FadeTransform(c23_lab,c24_lab))
        self.wait(0.2)

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

        



