from manim import *

class anim(Scene):
    def construct(self):
        template = TexTemplate()
        template.add_to_preamble(r"\usepackage[siunitx, RPvoltages, american, europeanresistors]{circuitikz}")
        #example
        c = MathTex(
        r"""\draw (-2,0) to[short] ++(3,0)
        node[op amp, noinv input down, anchor=-] (OA){\texttt{}}
        (OA.-) to[short] (0,0) to[short] (0, 1.5) 
        (OA.out) to[short] ++(0.12, 0) coordinate(OAo) to[short] (3.5,1.5)
        (OA.+) to[short] ++(-0.5,0) to[short] (0.5,-2) to [short] (-0.5,-2) to[short] (1.5,-2);""",
        r"""\draw (-2,0) to[R=$R_1$] (-2,-3) node[ground]{};""",
        r"""\draw (0,1.5) to[R=$R_2$] (3.5,1.5);""",
        r"""\draw (-0.5,-2) to[C=$C_2$] (-0.5,-4);""",
        r"""\draw (1.5,-2) to[R=$R_4$] (1.5,-4);""",
        r"""\draw (-0.5,-4) to[short] (0.5,-4) node[ground]{} to(1.5,-4);""",
        r"""\draw (3.5,-0.5) to[R=$R_3$] (3.5,-2);""",
        r"""\draw (3.5,-2) to[C=$C_1$] (1.5,-2);""",


        stroke_width=2,
        fill_opacity=0,
        stroke_opacity=1,
        tex_environment="circuitikz",
        tex_template=template,
        ).scale(0.75)  

        #c.set_color_by_tex_to_color_map({"R_1":RED, "R_2":RED, "C1": BLUE, "R3": BLUE, "C2": YELLOW, "R4": YELLOW, })
        plane1 = (
            NumberPlane(x_range=[0, 4, 1], x_length=5, y_range=[-1, 1, 1], y_length=1)
            .shift(RIGHT * 3.5)
        )
        
        sine = always_redraw(lambda: 
                 plane1.plot(lambda x: 
                    np.sin((2*x) + np.deg2rad(0)), 
                    x_range = [0,4], 
                    color = YELLOW))
        
        self.play(FadeIn(c, shift=UP, target_position=ORIGIN), run_time=3)
        self.play(ApplyWave(c))
        self.play(FadeIn(sine))
        # self.play(Indicate(c[2], color=TEAL), run_time=2) 
        #self.play(Circumscribe(c[3], fade_out=True, color=BLUE))
        self.wait(2)