from manim import *
import math
resultd1 = 0
resultd2 = 0
resultd12 = 0
resultd22 = 0
resultd13 = 0
resultd23 = 0
resultd14 = 0
resultd24 = 0

prev = 0
result = 0
peak = 0

# def charge(x,func):
#     global prev
#     global result
#     global peak
#     if (x >= PI/3):
#         func = func + 1
#     if func>prev:
#         result = func
#         t = 0
#         prev = result
#         peak = func
#     else:
#         result = peak
#         prev = result
#     return result

def charge(x, func):
    if(0 <= x < PI/6):
        return func/2
    elif(PI/6 <= x < 2*PI/6):
        return 0.5
    elif(2*PI/6 <= x < 3*PI/6):
        return 0.5 + func/2
    else:
        return 1

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
    return abs(resultd2)

def vd12(sine):
    global resultd12
    if(sine - 0.7 <= resultd12):
        resultd12 = resultd12
    else:
        if(sine<0.7):
            resultd12 = 0
        else:
            resultd12 = sine - 0.7
    return resultd12

def vd22(sine):
    global resultd22
    if(sine + 0.7 >= resultd22):
        resultd22 = resultd22
    else:
        if(sine > 0.7):
            resultd22 = 0
        else:
            resultd22 = sine + 0.7
    return abs(resultd22)

def vd13(sine):
    global resultd13
    if(sine - 0.7 <= resultd13):
        resultd13 = resultd13
    else:
        if(sine<0.7):
            resultd13 = 0
        else:
            resultd13 = sine - 0.7
    return resultd13

def vd23(sine):
    global resultd23
    if(sine + 0.7 >= resultd23):
        resultd23 = resultd23
    else:
        if(sine > 0.7):
            resultd23 = 0
        else:
            resultd23 = sine + 0.7
    return abs(resultd23)

def vd14(sine):
    global resultd14
    if(sine - 0.7 <= resultd14):
        resultd14 = resultd14
    else:
        if(sine<0.7):
            resultd14 = 0
        else:
            resultd14 = sine - 0.7
    return resultd14

def vd24(sine):
    global resultd24
    if(sine + 0.7 >= resultd24):
        resultd24 = resultd24
    else:
        if(sine > 0.7):
            resultd24 = 0
        else:
            resultd24 = sine + 0.7
    return abs(resultd24)    

def clrd1(val):
    global resultd1
    resultd1 = val

def clrd2(val):
    global resultd2
    resultd2 = val

def ch1(sine, x):
    if x < PI/6:
        return sine
    else:
        return 1

def ch2(sine, x):
    if x < 2*PI/6:
        return 0
    elif 2*PI/6 <= x < 3*PI/6:
        return sine
    else:
        return -1




class anim(Scene):
    def construct(self):
        template = TexTemplate()
        template.add_to_preamble(r"\usepackage[siunitx, RPvoltages, american, europeanresistors]{circuitikz}")

        a = MathTex(
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

        draw = ValueTracker(0.0001)
        scale =ValueTracker(1)
        c11 = always_redraw(lambda:DecimalNumber(
                 20.5, 
                 show_ellipsis=False, 
                 num_decimal_places=1,
                 include_sign = False
                 ).next_to(a[2], RIGHT))
        c11_lab = always_redraw(lambda :MathTex("V").next_to(c11, RIGHT))
        c21 = always_redraw(lambda:DecimalNumber(
                 -20.5, 
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
                    x_range = [0,3*PI/6], 
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
        group1 = VGroup(c11,c21,c11_lab,c21_lab)
        group1_2 = VGroup(sin1,dot1,b1,l1,a1,a1_lab)
        self.play(FadeIn(group1,group1_2, a))
        self.wait(0.2)

        r1 = MathTex(
        r"""\draw (0,-4) to[sV, v=$$, voltage shift=1]  (0,0) (0,0) to[short] (1,0) (0,-4) to[short] (8,-4)(8,-4) to[short] (8,0)(8,0) to[short] (7,0);""",
        r"""\draw (1,0)  to[diode, o-o]  (4,3); """,
        r"""\draw (4,3)  to[C, o-o , v^=$$, voltage shift=1]  (7,0); """,
        r"""\draw (4,-3)  to[diode, o-o]  (1,0); """,
        r"""\draw (7,0)  to[C, o-o , v^=$$, voltage shift=1]  (4,-3); """,
        r"""\draw (4,-3) to[short, -o] (9,-3)  (4,3) to[short, -o] (9,3) ; """,
        r"""\draw (4,-3) node[ground]{}; """,
        stroke_width=2,
        fill_opacity=0,
        stroke_opacity=1,
        tex_environment="circuitikz",
        tex_template=template,
        ).scale(0.5)

        shift = ValueTracker(0)

        ax2 = always_redraw(lambda:NumberPlane(x_range=[0, 4.29, 1], x_length=2.5, y_range=[-1, 1, 1], y_length=1)
        .next_to(r1[0], LEFT, buff = 0.5).scale(scale.get_value()).shift(UP*shift.get_value()).set_opacity(0)
        )
        sin2 = always_redraw(lambda: 
                 ax2.plot(lambda x: 
                    np.sin((3 * x) + np.deg2rad(0)), 
                    x_range = [0,draw.get_value()], 
                    color = YELLOW).scale(scale.get_value()))
        dot2 = always_redraw(lambda: 
                    Dot(point = sin2.get_end()).scale(scale.get_value())
                 )
        b2 = always_redraw(lambda:RoundedRectangle(corner_radius=0.2,width=2.5, height = 1.25).move_to(ax2).scale(scale.get_value()))
        l2 = always_redraw(lambda:Line(start=b2.get_critical_point(LEFT), end=b2.get_critical_point(RIGHT),color = BLUE_C, stroke_width = 2, stroke_opacity = 1))
        a2 = always_redraw(lambda:DecimalNumber(
                 21.2*(np.sin((3 * draw.get_value()) + np.deg2rad(0))), 
                 show_ellipsis=False, 
                 num_decimal_places=1,
                 include_sign = False
                 ).next_to(ax2, UP).scale(scale.get_value()))
        a2_lab = always_redraw(lambda:MathTex("V").next_to(a2, RIGHT).scale(scale.get_value()))
        c12 = always_redraw(lambda:DecimalNumber(
                 vd1(21.2*np.sin((3 * draw.get_value()) + np.deg2rad(0))), 
                 show_ellipsis=False, 
                 num_decimal_places=1,
                 include_sign = False
                 ).next_to(r1[2], UR, buff = -0.7*scale.get_value()).scale(scale.get_value()))
        c12_lab = always_redraw(lambda :MathTex("V").next_to(c12, RIGHT).scale(scale.get_value()))
        c22 = always_redraw(lambda:DecimalNumber(
                 vd2(21.2*np.sin((3 * draw.get_value()) + np.deg2rad(0))), 
                 show_ellipsis=False, 
                 num_decimal_places=1,
                 include_sign = False
                 ).next_to(r1[4], DR,buff = -0.7*scale.get_value()).scale(scale.get_value()))
        c22_lab = always_redraw(lambda :MathTex("V").next_to(c22, RIGHT).scale(scale.get_value()))
        group2 = VGroup(c12,c22,c12_lab,c22_lab)
        group2_2 = VGroup(sin2,dot2,b2,l2,a2,a2_lab)

        ax0 = always_redraw(lambda:NumberPlane(x_range=[0, 4.29, 1], x_length=2.5, y_range=[-1, 1, 1], y_length=1)
        .scale(1).move_to(r1, RIGHT).shift(RIGHT*2+UP*0.4).set_opacity(0)
        )
        sin0 = always_redraw(lambda: 
                 ax0.plot(lambda x:
                    1.4*charge(x,abs(np.sin(3*x))),
                    x_range = [0,draw.get_value()], 
                    color = YELLOW,
                    use_smoothing = False).scale(1))
        dot0 = always_redraw(lambda: 
                    Dot(point = sin0.get_end()).scale(1)
                 )
        b0 = always_redraw(lambda:RoundedRectangle(corner_radius=0.2,width=2.5, height = 1.5).move_to(ax0).scale(1))
        l0 = always_redraw(lambda:Line(start=b0.get_critical_point(LEFT), end=b0.get_critical_point(RIGHT),color = BLUE_C, stroke_width = 2, stroke_opacity = 1))
        a0 = always_redraw(lambda:DecimalNumber(
                 (vd1(21.2*np.sin((3 * draw.get_value()) + np.deg2rad(0))))+(vd2(21.2*np.sin((3 * draw.get_value()) + np.deg2rad(0)))), 
                 show_ellipsis=False, 
                 num_decimal_places=1,
                 include_sign = False
                 ).next_to(ax0, UP, buff = 0.35).scale(1))
        a0_lab = always_redraw(lambda:MathTex("V").scale(1).next_to(a0, RIGHT, buff = 0.1))
        group0 = VGroup(sin0,dot0,b0,l0,a0,a0_lab)


        self.play(ReplacementTransform(a, r1), ReplacementTransform(group1,group2), ReplacementTransform(group1_2,group2_2), FadeIn(group0))    #0
        self.wait(0.2)  #2
        self.play(Indicate(r1[6], color = TEAL)) #3
        self.wait(0.2) #4
        self.play(draw.animate.set_value(4*PI/3), run_time = 5) #5
        self.wait(0.2) #6
        self.play(draw.animate.set_value(0.0001), run_time = 1) #5
        
        r12 = MathTex(
        r"""\draw (0,-4) to[sV, v=$$, voltage shift=1]  (0,0) (0,0) to[short] (1,0) (0,-4) to[short] (8,-4)(8,-4) to[short] (8,0)(8,0) to[short] (7,0);""",
        r"""\draw (1,0)  to[diode, o-o]  (4,3); """,
        r"""\draw (4,3)  to[C, o-o , v^=$$, voltage shift=1]  (7,0); """,
        r"""\draw (4,-3)  to[diode, o-o]  (1,0); """,
        r"""\draw (7,0)  to[C, o-o , v^=$$, voltage shift=1]  (4,-3); """,
        r"""\draw (4,-3) to[short, -o] (9,-3)  (4,3) to[short, -o] (9,3) ; """,
        r"""\draw (4,-3) node[ground]{}; """,
        stroke_width=2,
        fill_opacity=0,
        stroke_opacity=1,
        tex_environment="circuitikz",
        tex_template=template,
        ).scale(0.5).scale(0.75).shift(LEFT*4.25+UP)
        r2 = MathTex(
        r"""\draw (0,-4) to[sV, v=$$, voltage shift=1]  (0,0) (0,0) to[short] (1,0) (0,-4) to[short] (8,-4)(8,-4) to[short] (8,0)(8,0) to[short] (7,0);""",
        r"""\draw (1,0)  to[diode, o-o]  (4,3); """,
        r"""\draw (7,0)  to[diode, o-o]  (4,3); """,
        r"""\draw (4,-3)  to[diode, o-o]  (1,0); """,
        r"""\draw (4,-3)  to[diode, o-o ]  (7,0); """,
        r"""\draw (4,-3) to[short, -o] (9,-3)  (4,3) to[short, -o] (9,3) ; """,
        r"""\draw (4,-3) node[ground]{}; """,
        stroke_width=2,
        fill_opacity=0,
        stroke_opacity=1,
        tex_environment="circuitikz",
        tex_template=template,
        ).scale(0.375).shift(RIGHT*2.75+UP)
        
        ax3 = always_redraw(lambda:NumberPlane(x_range=[0, 4.29, 1], x_length=2.5, y_range=[-1, 1, 1], y_length=1)
        .scale(0.75).shift(DOWN*2+LEFT*5.5).set_opacity(0)
        )
        sin3 = always_redraw(lambda: 
                 ax3.plot(lambda x: 
                    np.sin((3 * x) + np.deg2rad(0)), 
                    x_range = [0,draw.get_value()], 
                    color = YELLOW).scale(0.75))
        dot3 = always_redraw(lambda: 
                    Dot(point = sin3.get_end()).scale(0.75)
                 )
        b3 = always_redraw(lambda:RoundedRectangle(corner_radius=0.2,width=2.5, height = 1.25).move_to(ax3).scale(0.75))
        l3 = always_redraw(lambda:Line(start=b3.get_critical_point(LEFT), end=b3.get_critical_point(RIGHT),color = BLUE_C, stroke_width = 2, stroke_opacity = 1))
        a3 = always_redraw(lambda:DecimalNumber(
                 21.2*(np.sin((3 * draw.get_value()) + np.deg2rad(0))), 
                 show_ellipsis=False, 
                 num_decimal_places=1,
                 include_sign = False
                 ).next_to(ax3, UP).scale(0.75))
        a3_lab = always_redraw(lambda:MathTex("V").scale(0.75).next_to(a3, RIGHT, buff = 0.1))
        c13 = always_redraw(lambda:DecimalNumber(
                 vd13(21.2*np.sin((3 * draw.get_value()) + np.deg2rad(0))), 
                 show_ellipsis=False, 
                 num_decimal_places=1,
                 include_sign = False
                 ).next_to(r12[2], UR, buff = -0.7*scale.get_value()).scale(0.5))
        c13_lab = always_redraw(lambda :MathTex("V").scale(0.5).next_to(c13, RIGHT, buff = 0.1))
        c23 = always_redraw(lambda:DecimalNumber(
                 vd23(21.2*np.sin((3 * draw.get_value()) + np.deg2rad(0))), 
                 show_ellipsis=False, 
                 num_decimal_places=1,
                 include_sign = False
                 ).next_to(r12[4], DR,buff = -0.7*scale.get_value()).scale(0.5))
        c23_lab = always_redraw(lambda :MathTex("V").scale(0.5).next_to(c23, RIGHT, buff = 0.1))
        group3 = VGroup(c13,c23,c13_lab,c23_lab)
        group2_3 = VGroup(sin3,dot3,b3,l3,a3,a3_lab)

        ax4 = always_redraw(lambda:NumberPlane(x_range=[0, 4.29, 1], x_length=2.5, y_range=[-1, 1, 1], y_length=1)
        .scale(0.75).shift(DOWN*2+RIGHT).set_opacity(0)
        )
        sin4 = always_redraw(lambda: 
                 ax4.plot(lambda x: 
                    np.sin((3 * x) + np.deg2rad(0)), 
                    x_range = [0,draw.get_value()], 
                    color = YELLOW).scale(0.75))
        dot4 = always_redraw(lambda: 
                    Dot(point = sin4.get_end()).scale(0.75)
                 )
        b4 = always_redraw(lambda:RoundedRectangle(corner_radius=0.2,width=2.5, height = 1.25).move_to(ax4).scale(0.75))
        l4 = always_redraw(lambda:Line(start=b4.get_critical_point(LEFT), end=b4.get_critical_point(RIGHT),color = BLUE_C, stroke_width = 2, stroke_opacity = 1))
        a4 = always_redraw(lambda:DecimalNumber(
                 21.2*(np.sin((3 * draw.get_value()) + np.deg2rad(0))), 
                 show_ellipsis=False, 
                 num_decimal_places=1,
                 include_sign = False
                 ).next_to(ax4, UP).scale(0.75))
        a4_lab = always_redraw(lambda:MathTex("V").scale(0.75).next_to(a4, RIGHT, buff = 0.1))
        group4 = VGroup(sin4,dot4,b4,l4,a4,a4_lab)

        ax5 = always_redraw(lambda:NumberPlane(x_range=[0, 4.29, 1], x_length=2.5, y_range=[-1, 1, 1], y_length=1)
        .scale(0.75).move_to(r12, RIGHT).shift(RIGHT*1.5+UP*0.25).set_opacity(0)
        )
        sin5 = always_redraw(lambda: 
                 ax5.plot(lambda x:
                    1.4*charge(x,abs(np.sin(3*x))),
                    x_range = [0,draw.get_value()], 
                    color = YELLOW,
                    use_smoothing = False).scale(0.75))
        dot5 = always_redraw(lambda: 
                    Dot(point = sin5.get_end()).scale(0.75)
                 )
        b5 = always_redraw(lambda:RoundedRectangle(corner_radius=0.2,width=2.5, height = 1.5).move_to(ax5).scale(0.75))
        l5 = always_redraw(lambda:Line(start=b5.get_critical_point(LEFT), end=b5.get_critical_point(RIGHT),color = BLUE_C, stroke_width = 2, stroke_opacity = 1))
        a5 = always_redraw(lambda:DecimalNumber(
                 vd13(21.2*np.sin((3 * draw.get_value()) + np.deg2rad(0)))+vd23(21.2*np.sin((3 * draw.get_value()) + np.deg2rad(0))), 
                 show_ellipsis=False, 
                 num_decimal_places=1,
                 include_sign = False
                 ).next_to(ax5, UP).scale(0.75))
        a5_lab = always_redraw(lambda:MathTex("V").scale(0.75).next_to(a5, RIGHT, buff = 0.1))
        group5 = VGroup(sin5,dot5,b5,l5,a5,a5_lab)

        ax6 = always_redraw(lambda:NumberPlane(x_range=[0, 4.29, 1], x_length=2.5, y_range=[-1, 1, 1], y_length=1)
        .scale(0.75).move_to(r2, RIGHT).shift(RIGHT*1.5+UP*0.25).set_opacity(0)
        )
        sin6 = always_redraw(lambda: 
                 ax6.plot(lambda x: 
                    0.7*abs(np.sin((3 * x) + np.deg2rad(0))), 
                    x_range = [0,draw.get_value()], 
                    color = YELLOW).scale(0.75))
        dot6 = always_redraw(lambda: 
                    Dot(point = sin6.get_end()).scale(0.75)
                 )
        b6 = always_redraw(lambda:RoundedRectangle(corner_radius=0.2,width=2.5, height = 1.5).move_to(ax6).scale(0.75))
        l6 = always_redraw(lambda:Line(start=b6.get_critical_point(LEFT), end=b6.get_critical_point(RIGHT),color = BLUE_C, stroke_width = 2, stroke_opacity = 1))
        a6 = always_redraw(lambda:DecimalNumber(
                 21.2*abs(np.sin((3 * draw.get_value()) + np.deg2rad(0))), 
                 show_ellipsis=False, 
                 num_decimal_places=1,
                 include_sign = False
                 ).next_to(ax6, UP).scale(0.75))
        a6_lab = always_redraw(lambda:MathTex("V").scale(0.75).next_to(a6, RIGHT, buff = 0.1))
        group6 = VGroup(sin6,dot6,b6,l6,a6,a6_lab)

        self.play(FadeOut(group0),FadeIn(ax3, group5, group6),scale.animate.set_value(0.75), group2.animate.scale(0.5).shift(LEFT*2),
                  ReplacementTransform(group2_2,group2_3),ReplacementTransform(group2,group3),ReplacementTransform(group2.copy(),group4), ReplacementTransform(r1,r12), FadeIn(r2),  run_time=1.5)
        clrd1(0)
        clrd2(0)
        self.play(draw.animate.set_value(4*PI/3), run_time = 5)     #12
        self.wait(0.2)
        self.play(draw.animate.set_value(0.0001), run_time = 1)     #14
        self.wait(0.2)
        
        r13 = MathTex(
        r"""\draw (0,-4) to[sV, v=$$, voltage shift=1]  (0,0) (0,0) to[short] (1,0) (0,-4) to[short] (8,-4)(8,-4) to[short] (8,0)(8,0) to[short] (7,0);""",
        r"""\draw (1,0)  to[diode, o-o]  (4,3); """,
        r"""\draw (4,3)  to[C, o-o , v^=$$, voltage shift=1]  (7,0); """,
        r"""\draw (4,-3)  to[diode, o-o]  (1,0); """,
        r"""\draw (7,0)  to[C, o-o , v^=$$, voltage shift=1]  (4,-3); """,
        r"""\draw (4,-3) to[short, -o] (9,-3)  (4,3) to[short, -o] (9,3) ; """,
        r"""\draw (8,0) to[short, -o] (9,0) to [short] (10,0) node[ground]{}; """,
        stroke_width=2,
        fill_opacity=0,
        stroke_opacity=1,
        tex_environment="circuitikz",
        tex_template=template,
        ).scale(0.5).scale(0.65).shift(LEFT*4.35+UP)

        c14 = always_redraw(lambda:DecimalNumber(
                 vd14(21.2*np.sin((3 * draw.get_value()) + np.deg2rad(0))), 
                 show_ellipsis=False, 
                 num_decimal_places=1,
                 include_sign = False
                 ).next_to(r13[2], UR, buff = -0.7*scale.get_value()).scale(0.5))
        c14_lab = always_redraw(lambda :MathTex("V").scale(0.5).next_to(c14, RIGHT, buff = 0.1))
        c24 = always_redraw(lambda:DecimalNumber(
                 vd24(21.2*np.sin((3 * draw.get_value()) + np.deg2rad(0))), 
                 show_ellipsis=False, 
                 num_decimal_places=1,
                 include_sign = False
                 ).next_to(r13[4], DR,buff = -0.7*scale.get_value()).scale(0.5))
        c24_lab = always_redraw(lambda :MathTex("V").scale(0.5).next_to(c24, RIGHT, buff = 0.1))
        group2_4 = VGroup(c14,c24,c14_lab,c24_lab)

        ax7 = always_redraw(lambda:NumberPlane(x_range=[0, 4.29, 1], x_length=2.5, y_range=[-1, 1, 1], y_length=1)
        .scale(0.75).move_to(r13, RIGHT).shift(RIGHT*1.5+UP*1).set_opacity(0)
        )
        sin7 = always_redraw(lambda: 
                 ax7.plot(lambda x: 
                    ch1(np.sin(3 * x),x), 
                    x_range = [0,draw.get_value()], 
                    color = YELLOW).scale(0.75))
        dot7 = always_redraw(lambda: 
                    Dot(point = sin7.get_end()).scale(0.75)
                 )
        b7 = always_redraw(lambda:RoundedRectangle(corner_radius=0.2,width=2.5, height = 1.5).move_to(ax7).scale(0.75))
        l7 = always_redraw(lambda:Line(start=b7.get_critical_point(LEFT), end=b7.get_critical_point(RIGHT),color = BLUE_C, stroke_width = 2, stroke_opacity = 1))
        a7 = always_redraw(lambda:DecimalNumber(
                 vd14(21.2*np.sin((3 * draw.get_value()) + np.deg2rad(0))), 
                 show_ellipsis=False, 
                 num_decimal_places=1,
                 include_sign = False
                 ).next_to(ax7, UP).scale(0.75))
        a7_lab = always_redraw(lambda:MathTex("V").scale(0.75).next_to(a7, RIGHT, buff = 0.1))
        group7 = VGroup(sin7,dot7,b7,l7,a7,a7_lab)
        
        ax8 = always_redraw(lambda:NumberPlane(x_range=[0, 4.29, 1], x_length=2.5, y_range=[-1, 1, 1], y_length=1)
        .scale(0.75).move_to(r13, RIGHT).shift(RIGHT*1.5+UP*-0.75).set_opacity(0)
        )
        sin8 = always_redraw(lambda: 
                 ax8.plot(lambda x: 
                    ch2(np.sin(3 * x),x), 
                    x_range = [0,draw.get_value()], 
                    color = YELLOW).scale(0.75))
        dot8 = always_redraw(lambda: 
                    Dot(point = sin8.get_end()).scale(0.75)
                 )
        b8 = always_redraw(lambda:RoundedRectangle(corner_radius=0.2,width=2.5, height = 1.5).move_to(ax8).scale(0.75))
        l8 = always_redraw(lambda:Line(start=b8.get_critical_point(LEFT), end=b8.get_critical_point(RIGHT),color = BLUE_C, stroke_width = 2, stroke_opacity = 1))
        a8 = always_redraw(lambda:DecimalNumber(
                 -1*vd24(21.2*np.sin((3 * draw.get_value()) + np.deg2rad(0))), 
                 show_ellipsis=False, 
                 num_decimal_places=1,
                 include_sign = False
                 ).next_to(ax8, UP).scale(0.75))
        a8_lab = always_redraw(lambda:MathTex("V").scale(0.75).next_to(a8, RIGHT, buff = 0.1))
        group8 = VGroup(sin8,dot8,b8,l8,a8,a8_lab)

        

        self.play(ReplacementTransform(r12,r13),ReplacementTransform(group3, group2_4),ReplacementTransform(group5.copy(), group7),ReplacementTransform(group5.copy(), group8), FadeOut(group5))
        self.wait(0.2)
        self.play(Indicate(r13[6], color = RED)) #18
        self.wait(0.2)
        #draw = 0.0001
        self.play(draw.animate.set_value(4*PI/3), run_time = 5)
        self.wait(0.2)



