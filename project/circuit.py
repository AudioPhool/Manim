from manim import *

class anim(Scene):
    def construct(self):
        template = TexTemplate()
        template.add_to_preamble(r"\usepackage[siunitx, RPvoltages, american, europeanresistors]{circuitikz}")
        #example
        ex = MathTex(
              r"""\draw (0,0) to[isource = $I_0$, v=$V_0$] (0,3);""",  
              r"""\draw (0,3) to[short, -*, i=$I_0$] (2,3);""",
              r"""\draw (2,0) to[short, -*, i=$I_1$]  (0,0);""",
              r"""\draw (2,3) to[R = $R_1$, i=$i_1$] (2,0);""",
              r"""\draw (2,3) to[short, -*] (4,3);""",
              r"""\draw (4,0) to[short, -*]  (2,0);""",
              r"""\draw (4,3) to[R = $R_2$, i=$i_2$] (4,0);""",
              stroke_width=4
            , fill_opacity=0
            , stroke_opacity=1
            , tex_environment="circuitikz"
            , tex_template=template
            
            )
        #op amp
        c = MathTex(
        r"""\draw (0,0) node[above]{$v_i$} to[short, o-] ++(1,0)
        node[op amp, noinv input up, anchor=+] (OA){\texttt{OA1}}
        (OA.-) to[short] (1,-2) (OA.out) to[short] ++(0.1, 0) coordinate(OAo) to[short] (3.5,-2);""",
        r"""\draw (1,-2) to[R=$R_1$] (1,-4) node[ground]{};""",
        r"""\draw (1,-2) to[R=$R_2$] (3.5,-2);""",
        stroke_width=2,
        fill_opacity=0,
        stroke_opacity=1,
        tex_environment="circuitikz",
        tex_template=template,
        )    
        
        

        # for cir, clr in zip(c[0,4],[RED, GREEN, BLUE, YELLOW]):
        #     cir.set_color(clr)
        c.set_color_by_tex_to_color_map({"I_0":RED, "R_1":YELLOW, "R_2":BLUE})

        self.play(FadeIn(c, shift=UP, target_position=ORIGIN), run_time=3)
        self.play(ApplyWave(c[0]))
        # self.play(Indicate(c[2], color=TEAL), run_time=2) 
        #self.play(Circumscribe(c[3], fade_out=True, color=BLUE))
        self.wait(2)