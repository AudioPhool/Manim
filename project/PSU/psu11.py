from manim import *

class anim(Scene):
    def construct(self):
        template = TexTemplate()
        template.add_to_preamble(r"\usepackage[siunitx, RPvoltages, american, europeanresistors]{circuitikz} \ctikzset{multipoles/dipchip/width=1.5} \ctikzset{multipoles/dipchip/pin spacing=0.2}")

        a = MathTex(
        r"""\draw (0,-4) to[sV, v=$$, voltage shift=1]  (0,0) (0,0) to[short] (1,0) (0,-4) to[short] (8,-4)(8,-4) to[short, -o] (8,0)(8,0) to[short] (7,0);""",
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
        ).scale(0.45).shift(LEFT*3+DOWN*0)

        b = MathTex(
        r"""\draw (0,-4) to[sV, v=$$, voltage shift=1]  (0,0) (0,0) to[short] (1,0) (0,-4) to[short] (8,-4)(8,-4) to[short, -o] (8,0)(8,0) to[short] (7,0);""",
        r"""\draw (1,0)  to[diode, o-o]  (4,3); """,
        r"""\draw (4,3)  to[C, o-o , v^=$1000uF$, voltage shift=1]  (7,0); """,
        r"""\draw (4,-3)  to[diode, o-o]  (1,0); """,
        r"""\draw (7,0)  to[C, o-o , v^=$1000uF$, voltage shift=1]  (4,-3); """,
        r"""\draw (4,-3) to[R, l_=$1\Omega$, -o] (9,-3)  (4,3) to[R, l^=$1\Omega$, -o] (9,3) ; """,
        r"""\draw (9,0) to[C, v^=$1000uF$, voltage shift=1] (9,-3)  (9,3) to[C, v^=$1000uF$, voltage shift=1] (9,0) ; """,
        r"""\draw (8,0) to[short, -o] (9,0) to [short] (14,0) (14,0) to [short] (15,0) node[ground]{}; """,
        r"""\draw (9,3) to[short] (12,3) (9,-3) to[short] (12,-3) ; """,
        stroke_width=2,
        fill_opacity=0,
        stroke_opacity=1,
        tex_environment="circuitikz",
        tex_template=template,
        ).scale(0.45).shift(LEFT*1.65+DOWN*0)

        c = MathTex(
        r"""\draw (0,-4) to[sV, v=$$, voltage shift=1]  (0,0) (0,0) to[short] (1,0) (0,-4) to[short] (8,-4)(8,-4) to[short, -o] (8,0)(8,0) to[short] (7,0);""",
        r"""\draw (1,0)  to[diode, o-o]  (4,3); """,
        r"""\draw (4,3)  to[C, o-o , v^=$1000uF$, voltage shift=1]  (7,0); """,
        r"""\draw (4,-3)  to[diode, o-o]  (1,0); """,
        r"""\draw (7,0)  to[C, o-o , v^=$1000uF$, voltage shift=1]  (4,-3); """,
        r"""\draw (4,-3) to[R, l_=$1\Omega$, -o] (9,-3)  (4,3) to[R, l^=$1\Omega$, -o] (9,3) ; """,
        r"""\draw (9,0) to[C, v^=$1000uF$, voltage shift=1] (9,-3)  (9,3) to[C, v^=$1000uF$, voltage shift=1] (9,0) ; """,
        r"""\draw (8,0) to[short, -o] (9,0) to [short] (14,0) (14,0) to [short] (15,0) node[ground]{}; """,
        r"""\draw (9,3) to[short] (12.95,3) (9,-3) to[short] (12.95,-3) ; """,
        r"""\draw (14,2.7) node[dipchip, num pins = 10, hide numbers, no topmark, external pins width = 0] (C){7815};
            \node [right, font =\tiny] at (C.bpin 2){Vin};
            \node [left, font =\tiny] at (C.bpin 9){Vout};
            \node [above, font =\tiny] at (C.s){Gnd};
            \draw (C.s) to [short, -o] (14,0);""",
        r"""\draw (14,-2.7) node[dipchip, num pins = 10, hide numbers, no topmark, external pins width = 0] (C){7915};
            \node [right, font =\tiny] at (C.bpin 4){Vin};
            \node [left, font =\tiny] at (C.bpin 7){Vout};
            \node [below, font =\tiny] at (C.n){Gnd};
            \draw (C.n) to [short, -o] (14,0);""",
        stroke_width=2,
        fill_opacity=0,
        stroke_opacity=1,
        tex_environment="circuitikz",
        tex_template=template,
        ).scale(0.45).shift(LEFT*1.65+DOWN*0)

        d = MathTex(
        r"""\draw (0,-4) to[sV, v=$$, voltage shift=1]  (0,0) (0,0) to[short] (1,0) (0,-4) to[short] (8,-4)(8,-4) to[short, -o] (8,0)(8,0) to[short] (7,0);""",
        r"""\draw (1,0)  to[diode, o-o]  (4,3); """,
        r"""\draw (4,3)  to[C, o-o , v^=$1000uF$, voltage shift=1]  (7,0); """,
        r"""\draw (4,-3)  to[diode, o-o]  (1,0); """,
        r"""\draw (7,0)  to[C, o-o , v^=$1000uF$, voltage shift=1]  (4,-3); """,
        r"""\draw (4,-3) to[R, l_=$1\Omega$, -o] (9,-3)  (4,3) to[R, l^=$1\Omega$, -o] (9,3) ; """,
        r"""\draw (9,0) to[C, v^=$1000uF$, voltage shift=1] (9,-3)  (9,3) to[C, v^=$1000uF$, voltage shift=1] (9,0) ; """,
        r"""\draw (8,0) to[short, -o] (9,0) to [short] (14,0) (14,0) to [short] (15,0) node[ground]{}; """,
        r"""\draw (9,3) to[short] (12.95,3) (9,-3) to[short] (12.95,-3) ; """,
        r"""\draw (14,2.7) node[dipchip, num pins = 10, hide numbers, no topmark, external pins width = 0] (C){7815};
            \node [right, font =\tiny] at (C.bpin 2){Vin};
            \node [left, font =\tiny] at (C.bpin 9){Vout};
            \node [above, font =\tiny] at (C.s){Gnd};
            \draw (C.s) to [short, -o] (14,0);""",
        r"""\draw (14,-2.7) node[dipchip, num pins = 10, hide numbers, no topmark, external pins width = 0] (C){7915};
            \node [right, font =\tiny] at (C.bpin 4){Vin};
            \node [left, font =\tiny] at (C.bpin 7){Vout};
            \node [below, font =\tiny] at (C.n){Gnd};
            \draw (C.n) to [short, -o] (14,0);""",
        r"""\draw (12,0) to[C, voltage shift=1] (12,-3)  (12,3) to[C, voltage shift=1] (12,0) ; """,
        stroke_width=2,
        fill_opacity=0,
        stroke_opacity=1,
        tex_environment="circuitikz",
        tex_template=template,
        ).scale(0.45).shift(LEFT*1.65+DOWN*0)

        e = MathTex(
        r"""\draw (0,-4) to[sV, v=$$, voltage shift=1]  (0,0) (0,0) to[short] (1,0) (0,-4) to[short] (8,-4)(8,-4) to[short, -o] (8,0)(8,0) to[short] (7,0);""",
        r"""\draw (1,0)  to[diode, o-o]  (4,3); """,
        r"""\draw (4,3)  to[C, o-o , v^=$1000uF$, voltage shift=1]  (7,0); """,
        r"""\draw (4,-3)  to[diode, o-o]  (1,0); """,
        r"""\draw (7,0)  to[C, o-o , v^=$1000uF$, voltage shift=1]  (4,-3); """,
        r"""\draw (4,-3) to[R, l_=$1\Omega$, -o] (9,-3)  (4,3) to[R, l^=$1\Omega$, -o] (9,3) ; """,
        r"""\draw (9,0) to[C, v^=$1000uF$, voltage shift=1] (9,-3)  (9,3) to[C, v^=$1000uF$, voltage shift=1] (9,0) ; """,
        r"""\draw (8,0) to[short, -o] (9,0) to [short] (16,0) (16,0) to [short] (17,0) node[ground]{}; """,
        r"""\draw (9,3) to[short] (12.95,3) (9,-3) to[short] (12.95,-3) ; """,
        r"""\draw (14,2.7) node[dipchip, num pins = 10, hide numbers, no topmark, external pins width = 0] (C){7815};
            \node [right, font =\tiny] at (C.bpin 2){Vin};
            \node [left, font =\tiny] at (C.bpin 9){Vout};
            \node [above, font =\tiny] at (C.s){Gnd};
            \draw (C.s) to [short, -o] (14,0);""",
        r"""\draw (14,-2.7) node[dipchip, num pins = 10, hide numbers, no topmark, external pins width = 0] (C){7915};
            \node [right, font =\tiny] at (C.bpin 4){Vin};
            \node [left, font =\tiny] at (C.bpin 7){Vout};
            \node [below, font =\tiny] at (C.n){Gnd};
            \draw (C.n) to [short, -o] (14,0);""",
        r"""\draw (12,0) to[C, voltage shift=1, o-o] (12,-3)  (12,3) to[C, voltage shift=1, o-o] (12,0) ; """,
        r"""\draw (15.05,3) to[short] (16,3) (15.05,-3) to[short] (16,-3) ; """,
        r"""\draw (16,0) to[C, voltage shift=1, o-o] (16,-3)  (16,3) to[C, voltage shift=1, o-o] (16,0) ; """,
        stroke_width=2,
        fill_opacity=0,
        stroke_opacity=1,
        tex_environment="circuitikz",
        tex_template=template,
        ).scale(0.45).shift(LEFT*1+DOWN*0)

        f = MathTex(
        r"""\draw (0,-4) to[sV, v=$$, voltage shift=1]  (0,0) (0,0) to[short] (1,0) (0,-4) to[short] (8,-4)(8,-4) to[short, -o] (8,0)(8,0) to[short] (7,0);""",
        r"""\draw (1,0)  to[diode, o-o]  (4,3); """,
        r"""\draw (4,3)  to[C, o-o , v^=$1000uF$, voltage shift=1]  (7,0); """,
        r"""\draw (4,-3)  to[diode, o-o]  (1,0); """,
        r"""\draw (7,0)  to[C, o-o , v^=$1000uF$, voltage shift=1]  (4,-3); """,
        r"""\draw (4,-3) to[R, l_=$1\Omega$, -o] (9,-3)  (4,3) to[R, l^=$1\Omega$, -o] (9,3) ; """,
        r"""\draw (9,0) to[C, v^=$1000uF$, voltage shift=1] (9,-3)  (9,3) to[C, v^=$1000uF$, voltage shift=1] (9,0) ; """,
        r"""\draw (8,0) to[short, -o] (9,0) to [short] (16,0) (16,0) to [short] (17,0) node[ground]{}; """,
        r"""\draw (9,3) to[short] (12.95,3) (9,-3) to[short] (12.95,-3) ; """,
        r"""\draw (14,2.7) node[dipchip, num pins = 10, hide numbers, no topmark, external pins width = 0] (C){7815};
            \node [right, font =\tiny] at (C.bpin 2){Vin};
            \node [left, font =\tiny] at (C.bpin 9){Vout};
            \node [above, font =\tiny] at (C.s){Gnd};
            \draw (C.s) to [short, -o] (14,0);""",
        r"""\draw (14,-2.7) node[dipchip, num pins = 10, hide numbers, no topmark, external pins width = 0] (C){7915};
            \node [right, font =\tiny] at (C.bpin 4){Vin};
            \node [left, font =\tiny] at (C.bpin 7){Vout};
            \node [below, font =\tiny] at (C.n){Gnd};
            \draw (C.n) to [short, -o] (14,0);""",
        r"""\draw (12,0) to[C, l^=$0.1uF$, voltage shift=1, o-o] (12,-3)  (12,3) to[C,l^=$0.1uF$, voltage shift=1, o-o] (12,0) ; """,
        r"""\draw (15.05,3) to[short] (16,3) (15.05,-3) to[short] (16,-3) ; """,
        r"""\draw (16,0) to[C,l^=$0.1uF$, voltage shift=1, o-o] (16,-3)  (16,3) to[C, l^=$0.1uF$,voltage shift=1, o-o] (16,0) ; """,
        stroke_width=2,
        fill_opacity=0,
        stroke_opacity=1,
        tex_environment="circuitikz",
        tex_template=template,
        ).scale(0.45).shift(LEFT*0.95+DOWN*0)

        g = MathTex(
        r"""\draw (0,-4) to[sV, v=$$, voltage shift=1]  (0,0) (0,0) to[short] (1,0) (0,-4) to[short] (8,-4)(8,-4) to[short, -o] (8,0)(8,0) to[short] (7,0);""",
        r"""\draw (1,0)  to[diode, o-o]  (4,3); """,
        r"""\draw (4,3)  to[C, o-o , v^=$1000uF$, voltage shift=1]  (7,0); """,
        r"""\draw (4,-3)  to[diode, o-o]  (1,0); """,
        r"""\draw (7,0)  to[C, o-o , v^=$1000uF$, voltage shift=1]  (4,-3); """,
        r"""\draw (4,-3) to[R, l_=$1\Omega$, -o] (9,-3)  (4,3) to[R, l^=$1\Omega$, -o] (9,3) ; """,
        r"""\draw (9,0) to[C, v^=$1000uF$, voltage shift=1] (9,-3)  (9,3) to[C, v^=$1000uF$, voltage shift=1] (9,0) ; """,
        r"""\draw (8,0) to[short, -o] (9,0) to [short] (18,0) (18,0) to [short] (19,0) node[ground]{}; """,
        r"""\draw (9,3) to[short] (12.95,3) (9,-3) to[short] (12.95,-3) ; """,
        r"""\draw (14,2.7) node[dipchip, num pins = 10, hide numbers, no topmark, external pins width = 0] (C){7815};
            \node [right, font =\tiny] at (C.bpin 2){Vin};
            \node [left, font =\tiny] at (C.bpin 9){Vout};
            \node [above, font =\tiny] at (C.s){Gnd};
            \draw (C.s) to [short, -o] (14,0);""",
        r"""\draw (14,-2.7) node[dipchip, num pins = 10, hide numbers, no topmark, external pins width = 0] (C){7915};
            \node [right, font =\tiny] at (C.bpin 4){Vin};
            \node [left, font =\tiny] at (C.bpin 7){Vout};
            \node [below, font =\tiny] at (C.n){Gnd};
            \draw (C.n) to [short, -o] (14,0);""",
        r"""\draw (12,0) to[C, l^=$0.1uF$, voltage shift=1, o-o] (12,-3)  (12,3) to[C,l^=$0.1uF$, voltage shift=1, o-o] (12,0) ; """,
        r"""\draw (15.05,3) to[short] (18,3) (15.05,-3) to[short] (18,-3) ; """,
        r"""\draw (16,0) to[C,l^=$0.1uF$, voltage shift=1, o-o] (16,-3)  (16,3) to[C, l^=$0.1uF$,voltage shift=1, o-o] (16,0) ; """,
        r"""\draw (18,-3) to[diode, o-o] (18,0)  (18,0) to[diode, o-o] (18,3) ; """,
        stroke_width=2,
        fill_opacity=0,
        stroke_opacity=1,
        tex_environment="circuitikz",
        tex_template=template,
        ).scale(0.45).shift(LEFT*0.4+DOWN*0)

        h = MathTex(
        r"""\draw (0,-4) to[sV, v=$$, voltage shift=1]  (0,0) (0,0) to[short] (1,0) (0,-4) to[short] (8,-4)(8,-4) to[short, -o] (8,0)(8,0) to[short] (7,0);""",
        r"""\draw (1,0)  to[diode, o-o]  (4,3); """,
        r"""\draw (4,3)  to[C, o-o , v^=$$, voltage shift=1]  (7,0); """,
        r"""\draw (4,-3)  to[diode, o-o]  (1,0); """,
        r"""\draw (7,0)  to[C, o-o , v^=$$, voltage shift=1]  (4,-3); """,
        r"""\draw (4,-3) to[R, l_=$1\Omega$, -o] (9,-3)  (4,3) to[R, -o] (9,3) ; """,
        r"""\draw (9,0) to[C, v^=$$, voltage shift=1] (9,-3)  (9,3) to[C, v^=$$, voltage shift=1] (9,0) ; """,
        r"""\draw (8,0) to[short, -o] (9,0) to [short] (18,0) (18,0) to [short] (19,0) node[ground]{}; """,
        r"""\draw (9,3) to[short] (12.95,3) (9,-3) to[short] (12.95,-3) ; """,
        r"""\draw (14,2.7) node[dipchip, num pins = 10, hide numbers, no topmark, external pins width = 0] (C){7815};
            \node [right, font =\tiny] at (C.bpin 2){Vin};
            \node [left, font =\tiny] at (C.bpin 9){Vout};
            \node [above, font =\tiny] at (C.s){Gnd};
            \draw (C.s) to [short, -o] (14,0);""",
        r"""\draw (14,-2.7) node[dipchip, num pins = 10, hide numbers, no topmark, external pins width = 0] (C){7915};
            \node [right, font =\tiny] at (C.bpin 4){Vin};
            \node [left, font =\tiny] at (C.bpin 7){Vout};
            \node [below, font =\tiny] at (C.n){Gnd};
            \draw (C.n) to [short, -o] (14,0);""",
        r"""\draw (12,0) to[C, l^=$$, voltage shift=1, o-o] (12,-3)  (12,3) to[C,l^=$$, voltage shift=1, o-o] (12,0) ; """,
        r"""\draw (15.05,3) to[short] (18,3) (15.05,-3) to[short] (18,-3) ; """,
        r"""\draw (16,0) to[C,l^=$$, voltage shift=1, o-o] (16,-3)  (16,3) to[C, l^=$$,voltage shift=1, o-o] (16,0) ; """,
        r"""\draw (18,-3) to[diode, o-o] (18,0)  (18,0) to[diode, o-o] (18,3) ; """,
        r"""\draw (16,3) to[short] (16,4)(12,3) to[short] (12,4) (16,-3) to[short] (16,-4)(12,-3) to[short] (12,-4) ; """,
        r"""\draw (16,4) to[diode] (12,4) (12,-4) to[diode] (16,-4); """,
        stroke_width=3,
        fill_opacity=0,
        stroke_opacity=1,
        tex_environment="circuitikz",
        tex_template=template,
        ).scale(0.45).shift(LEFT*0.4+DOWN*-0.125)

        self.play(FadeIn(a))
        self.wait(0.2)#1
        self.play(LaggedStart(FadeIn(c), FadeOut(a), lag_ratio=0.2))
        self.wait(0.2)#5
        self.play(LaggedStart(FadeIn(d), FadeOut(c), lag_ratio=0.2))
        self.wait(0.2)#7
        self.play(LaggedStart(FadeIn(e), FadeOut(d), lag_ratio=0.2))
        self.wait(0.2)#9
        self.play(LaggedStart(FadeIn(f), FadeOut(e), lag_ratio=0.2))
        self.wait(0.2)#11
        self.play(LaggedStart(FadeIn(g), FadeOut(f), lag_ratio=0.2))
        self.wait(0.2)#13
        self.play(LaggedStart(FadeIn(h), FadeOut(g), lag_ratio=0.2))
        self.wait(0.2)#15