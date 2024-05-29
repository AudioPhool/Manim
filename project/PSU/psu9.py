from manim import *

class anim(Scene):
    def construct(self):
        template = TexTemplate()
        template.add_to_preamble(r"\usepackage[siunitx, RPvoltages, american, europeanresistors]{circuitikz}")

        
        a = MathTex(
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
        ).scale(0.5).shift(LEFT*2.8+DOWN*0.1)

        b = MathTex(
        r"""\draw (0,-4) to[sV, v=$$, voltage shift=1]  (0,0) (0,0) to[short] (1,0) (0,-4) to[short] (8,-4)(8,-4) to[short] (8,0)(8,0) to[short] (7,0);""",
        r"""\draw (1,0)  to[diode, o-o]  (4,3); """,
        r"""\draw (4,3)  to[C, o-o , v^=$1000uF$, voltage shift=1]  (7,0); """,
        r"""\draw (4,-3)  to[diode, o-o]  (1,0); """,
        r"""\draw (7,0)  to[C, o-o , v^=$1000uF$, voltage shift=1]  (4,-3); """,
        r"""\draw (4,-3) to[short, -o] (9,-3)  (4,3) to[short, -o] (9,3) ; """,
        r"""\draw (8,0) to[short, -o] (9,0) to [short] (10,0) node[ground]{}; """,
        stroke_width=2,
        fill_opacity=0,
        stroke_opacity=1,
        tex_environment="circuitikz",
        tex_template=template,
        ).scale(0.5).shift(LEFT*2.8+DOWN*0.7)
        

        c = MathTex(
        r"""\draw (0,-4) to[sV, v=$$, voltage shift=1]  (0,0) (0,0) to[short] (1,0) (0,-4) to[short] (8,-4)(8,-4) to[short] (8,0)(8,0) to[short] (7,0);""",
        r"""\draw (1,0)  to[diode, o-o]  (4,3); """,
        r"""\draw (4,3)  to[C, o-o , v^=$1000uF$, voltage shift=1]  (7,0); """,
        r"""\draw (4,-3)  to[diode, o-o]  (1,0); """,
        r"""\draw (7,0)  to[C, o-o , v^=$1000uF$, voltage shift=1]  (4,-3); """,
        r"""\draw (4,-3) to[R, l_=$R2$, -o] (9,-3)  (4,3) to[R, l^=$R1$, -o] (9,3) ; """,
        r"""\draw (8,0) to[short, -o] (9,0) to [short] (10,0) node[ground]{}; """,
        stroke_width=2,
        fill_opacity=0,
        stroke_opacity=1,
        tex_environment="circuitikz",
        tex_template=template,
        ).scale(0.5).shift(LEFT*2.8+DOWN*0.5)

        d = MathTex(
        r"""\draw (0,-4) to[sV, v=$$, voltage shift=1]  (0,0) (0,0) to[short] (1,0) (0,-4) to[short] (8,-4)(8,-4) to[short] (8,0)(8,0) to[short] (7,0);""",
        r"""\draw (1,0)  to[diode, o-o]  (4,3); """,
        r"""\draw (4,3)  to[C, o-o , v^=$1000uF$, voltage shift=1]  (7,0); """,
        r"""\draw (4,-3)  to[diode, o-o]  (1,0); """,
        r"""\draw (7,0)  to[C, o-o , v^=$1000uF$, voltage shift=1]  (4,-3); """,
        r"""\draw (4,-3) to[R, l_=$1\Omega$, -o] (9,-3)  (4,3) to[R, l^=$1\Omega$, -o] (9,3) ; """,
        r"""\draw (9,0) to[C, v^=$1000uF$, voltage shift=1] (9,-3)  (9,3) to[C, v^=$1000uF$, voltage shift=1] (9,0) ; """,
        r"""\draw (8,0) to[short, -o] (9,0) to [short] (10,0) node[ground]{}; """,
        stroke_width=2,
        fill_opacity=0,
        stroke_opacity=1,
        tex_environment="circuitikz",
        tex_template=template,
        ).scale(0.5).shift(LEFT*2.55+DOWN*0.5)
                
        eq1   = MathTex(r"V_{Ripple} = \frac{I_{dc}}{fC}", color = YELLOW ).scale(1.25).shift(RIGHT*4+UP*2)
        eq2   = MathTex(r"C = \frac{I_{dc}}{f*V_{Ripple}}", color = PURPLE ).scale(1.25).shift(RIGHT*4+UP*0)
        eq3   = MathTex(r"C = \frac{0.2A}{50Hz*2V_{p-p}}", color = BLUE ).scale(0.8).shift(RIGHT*3+UP*-2)
        eq4   = always_redraw(lambda: MathTex(r"= 2000uF", color = BLUE ).scale(0.8).next_to(eq3,RIGHT,buff=0.1))
        eq5   = MathTex(r".", color = BLUE ).set_opacity(0).next_to(a[2], RIGHT, buff = 0.1)
        eq6   = MathTex(r".", color = BLUE ).set_opacity(0).next_to(a[4], DR, buff = 0.1)


        self.play(FadeIn(eq1,a))
        self.wait(0.2)
        self.play(ReplacementTransform(eq1.copy(),eq2))
        self.wait(0.2)
        self.play(ReplacementTransform(eq2.copy(),eq3), FadeIn(eq4, eq5, eq6))
        self.wait(0.2)
        self.play(eq3.animate.shift(UP*5),a.animate.shift(DOWN*0.6), FadeOut(eq2,eq1))
        self.wait(0.2)
        self.play(FadeIn(eq5, eq6))
        self.play(ReplacementTransform(eq4.copy(),eq5),ReplacementTransform(eq4.copy(),eq6),FadeTransform(a,b))
        self.wait(0.2)
        self.play(ReplacementTransform(b,c))
        self.wait(0.2)
        self.play(LaggedStart(FadeIn(d), FadeOut(c), lag_ratio=0.2))
        self.wait(0.2)


