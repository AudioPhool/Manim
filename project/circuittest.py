from manim import *

class anim(Scene):
    def construct(self):
        template = TexTemplate()
        template.add_to_preamble(r"\usepackage[siunitx, RPvoltages, american, europeanresistors]{circuitikz}\ctikzset{tripoles/mos style/arrows}")
        
        f = MathTex(
        r"""\draw (-2,0) to[short] ++(3,0)
        node[op amp, noinv input down, anchor=-] (OA){\texttt{}}
        (OA.-) to[short] (0,0) to[short] (0, 1.5) 
        (OA.out) to[short] ++(0.12, 0) coordinate(OAo) to[short] (3.5,1.5)
        (OA.+) to[short] ++(-0.5,0) to[short] (0.5,-2);""",
        r"""\draw (-2,-1.5) node[nmos](nmos){}
                  (-2,0) to [short](nmos.D)
                  (nmos.S) to [short](-2,-2.5)  ;""",
        r"""\draw (-2,-2.5) to[R=$R_1$] (-2,-4) node[ground]{};""",
        r"""\draw (0,1.5) to[R=$R_2$] (3.5,1.5);""",
        r"""\draw (0.5,-2) to [short] (-0.5,-2) to[short] (1.5,-2)
                  (-0.5,-2) to[C=$C_2$] (-0.5,-4)
                  (1.5,-2) to[R=$R_4$] (1.5,-4) 
                  (-0.5,-4) to[short] (0.5,-4) 
                  node[ground]{} to(1.5,-4);""",
        r"""\draw (3.5,-0.5) to[R=$R_3$] (3.5,-2) 
                  (3.5,-2) to[C=$C_1$] (1.5,-2);""",
        stroke_width=2,
        fill_opacity=0,
        stroke_opacity=1,
        tex_environment="circuitikz",
        tex_template=template,
        ).scale(0.75).shift(RIGHT*2)

        self.play(FadeIn(f))