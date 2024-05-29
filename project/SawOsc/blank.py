from manim import *

class anim(Scene):
    def construct(self):
        template = TexTemplate()
        template.add_to_preamble(r"\usepackage[siunitx, RPvoltages, american, europeanresistors]{circuitikz}")

        a = MathTex(
        r"""\draw (0.5,1) to[short] ++(0.5,0)
        node[op amp, noinv input down, anchor=-] (OA){}
        (OA.-) to[short] ++(-0.5,0) to[short] (0.5, 2.25)
        (OA.out) to[short] ++(0.12, 0) coordinate(OAo) to[short] (3.5,2.25)
        (OA.+) to[short] ++(-0.5,0);""",#0
        r"""\draw (0.5, 2.25) to[C] (3.5,2.25) ;""",#1
        r"""\draw (0.5, 2.25) to[short](0.5, 3.25) to[short] (1.25,3.25) node[njfet, rotate=-90, anchor=S](Q1){} (Q1.D)to[short](3.5,3.25) to[short] (3.5,2.25) (Q1.G)to[short] ++(5.65,0);""",#1
        r"""\draw (0.5,0.025) to[short] (0.5,-0.5) node[ground]{} ;""",#2
        r"""\draw (-1.5,-0.5) node[ground]{} to[vsource](-1.5,1) to[R] (0.5, 1);""",#3
        r"""\draw (3.5,0.51) to[R] (5,0.51) node[op amp, noinv input down, anchor=-] (OA){} (OA.+) node[vcc]{} (OA.out) to[short] ++(0,4.19) (OA.out) to[R] ++(1.5,0) node[ground]{};""",#0
        stroke_width=8,
        fill_opacity=0,
        stroke_opacity=1,
        tex_environment="circuitikz",
        tex_template=template,
        ).scale(0.8).shift(RIGHT*0.15)

        self.play(FadeIn(a))