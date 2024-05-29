from cmath import pi
from manim import *
from scipy import signal

class anim(Scene):
    def construct(self):
        template = TexTemplate()
        template.add_to_preamble(r"\usepackage[siunitx, RPvoltages, american, europeanresistors]{circuitikz} \ctikzset{multipoles/dipchip/width=1.5} \ctikzset{multipoles/dipchip/pin spacing=0.2}")
        
        vgs = ValueTracker(0)
        cap = ValueTracker(0)

        a = MathTex(
        r"""\draw (0,0) node[ground]{} to[vsource] (0,2) {};""",#0
        r"""\draw (0,2) to[short] (1,2) node[njfet, anchor=G](Q1){} (0,0) to[short](2,0) to [short](Q1.S)
        (Q1.D) to[R] ++(0,2) node[vcc](vcc){} (Q1.D)++(0,0.25) to[short] ++(1,0) to[C] ++(0,-2) to[short]++(-1,0);""",#1
        stroke_width=2,
        fill_opacity=0,
        stroke_opacity=1,
        tex_environment="circuitikz",
        tex_template=template,
        ).scale(0.8).shift(LEFT*2.5)

        b1 = MathTex(
        r"""\draw (0,0) node[ground]{} to[short] (0,1.75) to[ccsw] (0,3) to[R] ++(0,2) node[vcc](vcc){};""",#1
        r"""\draw (0,3.25) to[short] ++(1,0) to[C] ++(0,-2) to[short]++(-1,0){};""",
        stroke_width=2,
        fill_opacity=0,
        stroke_opacity=1,
        tex_environment="circuitikz",
        tex_template=template,
        ).scale(0.8).next_to(a, RIGHT, 2.225)

        b = MathTex(
        r"""\draw (0,0) node[ground]{} to[short] (0,1.75) to[cosw] (0,3) to[R] ++(0,2) node[vcc](vcc){};""",#1
        r"""\draw (0,3.25) to[short] ++(1,0) to[C] ++(0,-2) to[short]++(-1,0){};""",
        stroke_width=2,
        fill_opacity=0,
        stroke_opacity=1,
        tex_environment="circuitikz",
        tex_template=template,
        ).scale(0.8).next_to(a, RIGHT, 2)

        c = MathTex(
        r"""\draw (0,0) node[ground]{} to[short] (0,1.75) to[ccsw] (0,3) to[R] ++(0,2) node[vcc](vcc){};""",#1
        r"""\draw (0,3.25) to[short] ++(1,0) to[C] ++(0,-2) to[short]++(-1,0){};""",
        stroke_width=2,
        fill_opacity=0,
        stroke_opacity=1,
        tex_environment="circuitikz",
        tex_template=template,
        ).scale(0.8).next_to(a, RIGHT, 2.225)

        v_gs = always_redraw(lambda: DecimalNumber(vgs.get_value(), 0).next_to(a[0], LEFT, buff = 0.75))
        lab = always_redraw(lambda: Tex("V").scale(0.8).next_to(v_gs,RIGHT,0.05))

        c1 = always_redraw(lambda: DecimalNumber(cap.get_value(), 0).next_to(a[1], RIGHT, buff = 0.25).shift(UP*0.5))
        c1l = always_redraw(lambda: Tex("V").scale(0.8).next_to(c1,RIGHT,0.05))

        c2= always_redraw(lambda: DecimalNumber(cap.get_value(), 0).next_to(c[1], RIGHT, buff = 0.25).shift(UP*0.5))
        c2l = always_redraw(lambda: Tex("V").scale(0.8).next_to(c2,RIGHT,0.05))

        self.play(FadeIn(a, b1, v_gs, lab, c1, c2, c1l, c2l))
        self.wait(0.2)#1
        self.play(LaggedStart(ReplacementTransform(b1, b), vgs.animate.set_value(-15)), run_time = 3)
        self.wait(0.2)#3
        self.play(cap.animate.set_value(5), run_time = 1)
        self.wait(0.2)#5
        self.play(LaggedStart(ReplacementTransform(b, c), vgs.animate.set_value(0)), run_time = 3)
        self.wait(0.2)#7
        self.play(cap.animate.set_value(0), run_time = 1)
        self.wait(0.2)#9