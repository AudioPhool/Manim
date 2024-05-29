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
        (OA.+) to[short] ++(-0.5,0) to[short] (0.5,-2);""",
        r"""\draw (-2,0) to[R=$R_1$] (-2,-3) node[ground]{};""",
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
        ).scale(0.75)  
        
        d = MathTex(
        r"""\draw (-2,0) to[short] ++(3,0)
        node[op amp, noinv input down, anchor=-] (OA){\texttt{}}
        (OA.-) to[short] (0,0) to[short] (0, 1.5) 
        (OA.out) to[short] ++(0.12, 0) coordinate(OAo) to[short] (3.5,1.5)
        (OA.+) to[short] ++(-0.5,0) to[short] (0.5,-2);""",
        r"""\draw (-2,0) to[R=$R_1$] (-2,-3) node[ground]{};""",
        r"""\draw (0,1.5) to[R=$R_2$] (3.5,1.5);""",
        r"""\draw (0.5,-2) to [short] (-0.5,-2) to[short] (1.5,-2)
                  (-0.5,-2) to[C=$0.1uF$] (-0.5,-4)
                  (1.5,-2) to[R=$20k$] (1.5,-4) 
                  (-0.5,-4) to[short] (0.5,-4) 
                  node[ground]{} to(1.5,-4);""",
        r"""\draw (3.5,-0.5) to[R=$20k$] (3.5,-2) 
                  (3.5,-2) to[C=$0.1uF$] (1.5,-2);""",
        stroke_width=2,
        fill_opacity=0,
        stroke_opacity=1,
        tex_environment="circuitikz",
        tex_template=template,
        ).scale(0.75) 

        
        e = MathTex(
        r"""\draw (-2,0) to[short] ++(3,0)
        node[op amp, noinv input down, anchor=-] (OA){\texttt{}}
        (OA.-) to[short] (0,0) to[short] (0, 1.5) 
        (OA.out) to[short] ++(0.12, 0) coordinate(OAo) to[short] (3.5,1.5)
        (OA.+) to[short] ++(-0.5,0) to[short] (0.5,-2);""",
        r"""\draw (-2,0) to[R=$R_1$] (-2,-3) node[ground]{};""",
        r"""\draw (0,1.5) to[R=$R_2$] (3.5,1.5);""",
        r"""\draw (0.5,-2) to[R=$Z_2$] (0.5,-4) 
                  node[ground]{};""",
        r"""\draw (3.5,-0.5) to[short] (3.5,-2) 
                  (3.5,-2) to[R=$Z_1$] (1.5,-2) 
                  to [short] (0.5,-2);""",
        stroke_width=2,
        fill_opacity=0,
        stroke_opacity=1,
        tex_environment="circuitikz",
        tex_template=template,
        ).scale(0.75).shift(LEFT*2)
        
        f = MathTex(
        r"""\draw (-2,0) to[short] ++(3,0)
        node[op amp, noinv input down, anchor=-] (OA){\texttt{}}
        (OA.-) to[short] (0,0) to[short] (0, 1.5) 
        (OA.out) to[short] ++(0.12, 0) coordinate(OAo) to[short] (3.5,1.5)
        (OA.+) to[short] ++(-0.5,0) to[short] (0.5,-2);""",
        r"""\draw (-2,0) to[R=$R_1$] (-2,-3) node[ground]{};""",
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
        ).scale(0.75).shift(LEFT*2)

        #c.set_color_by_tex_to_color_map({"R_1":RED, "R_2":RED, "C1": BLUE, "R3": BLUE, "C2": YELLOW, "R4": YELLOW, })

        freq = ValueTracker(2)
        filt = ValueTracker(0)

        out_plane = (
            NumberPlane(x_range=[0, 4, 1], x_length=2.5, y_range=[-1, 1, 1], y_length=1)
        ).to_edge(RIGHT,buff=1).shift(UP*1)
        
        sine = always_redraw(lambda: 
                 out_plane.plot(lambda x: 
                    np.sin((freq.get_value() * x) + np.deg2rad(0)), 
                    x_range = [0,4], 
                    color = YELLOW))

        hpf_plane = (
            NumberPlane(x_range=[0, 4, 1], x_length=2.5, y_range=[-1, 1, 1], y_length=1)
        ).shift(DOWN*1+RIGHT*4).scale(0.75)
        
        sine1 = always_redraw(lambda: 
                 hpf_plane.plot(lambda x: 
                    filt.get_value() * 
                    np.sin((freq.get_value() * x) + np.deg2rad(freq.get_value()*9)), 
                    x_range = [0,4], 
                    color = YELLOW))            
        
        lpf_plane = (
            NumberPlane(x_range=[0, 4, 1], x_length=2.5, y_range=[-1, 1, 1], y_length=1)
        ).shift(DOWN*0.8+LEFT*0.5).scale(0.75)
        
        sine2 = always_redraw(lambda: 
                 lpf_plane.plot(lambda x: 
                    (1-filt.get_value()) *
                    np.sin((freq.get_value() * x) + np.deg2rad(freq.get_value()*-9)), 
                    x_range = [0,4], 
                    color = YELLOW)) 

        noninv_plane = (
            NumberPlane(x_range=[0, 4, 1], x_length=2.5, y_range=[-1, 1, 1], y_length=1)
        ).shift(LEFT*1.5+UP*0.25).scale(0.75)
        
        sine3 = always_redraw(lambda: 
                 noninv_plane.plot(lambda x: 
                    (1-(abs((2*filt.get_value())-1))) *
                    np.sin((freq.get_value() * x) + np.deg2rad(0)), 
                    x_range = [0,4], 
                    color = YELLOW))

        z1_1 = MathTex(r"Z_1 = \sqrt{X_{C1}^2 + R_3^2}").to_corner(UR, buff = 1)
        z2_1 = MathTex(r"Z_2 = \frac{1}{\sqrt{X_{C2}^2 + R_4^2}}").to_edge(RIGHT, buff = 1)
        
        z1_2 = MathTex(r"Z_1 = \sqrt{20k^2 + 20k^2}").to_corner(UR, buff = 1)
        z2_2 = MathTex(r"Z_2 = \frac{1}{\sqrt{20k^2 + 20k^2}").to_edge(RIGHT, buff = 1)
        z3_2 = MathTex(r"@ f_{3dB}, X_C = R").to_corner(DR, buff = 1)

        z1_3 = MathTex(r"Z_1 = 28280").to_corner(UR, buff = 1)
        z2_3 = MathTex(r"Z_2 = 14140").to_edge(RIGHT, buff = 1)

        z_4 = MathTex(r"Z_1 = 2Z_2").to_corner(UR, buff = 1)

        z1 = MathTex("2Z")
        z2 = MathTex("Z").shift(DOWN*1.2+LEFT*2.5)

        z1_rect = Rectangle(height=3, width=3, color=BLUE_C, stroke_width=3).move_to(z1).shift(RIGHT*0.5)
        z2_rect = Rectangle(height=3, width=3, color=RED_C, stroke_width=3).move_to(z2).shift(DOWN)

        self.play(FadeIn(c, shift=UP, target_position=ORIGIN), run_time=1)
        self.play(ApplyWave(c))
        self.wait(1)
        self.play(LaggedStart(Indicate(c[3], color=RED_A, run_time=2), Indicate(c[4], color=RED_A, run_time=2)))
        self.play(Create(out_plane), Write(sine))
        self.wait(1)
        self.play(FadeIn(hpf_plane), FadeIn(sine1),FadeIn(lpf_plane), FadeIn(sine2),FadeIn(noninv_plane), FadeIn(sine3))
        self.wait(1)
        self.play(freq.animate.set_value(10),filt.animate.set_value(1), run_time = 3)
        self.play(freq.animate.set_value(2),filt.animate.set_value(0), run_time = 3)
        self.play(freq.animate.set_value(6),filt.animate.set_value(0.5), run_time = 3)
        self.wait(1)
        self.play(FadeOut(hpf_plane), FadeOut(sine1),FadeOut(lpf_plane), FadeOut(sine2),FadeOut(noninv_plane), FadeOut(sine3))
        self.wait(1)
        self.play(Indicate(c[4], color=BLUE), run_time=1) 
        self.wait(1)
        self.play(Indicate(c[3], color=RED), run_time=1) 
        self.wait(1)
        self.play(FadeIn(hpf_plane), FadeIn(sine1),FadeIn(lpf_plane), FadeIn(sine2),FadeIn(noninv_plane), FadeIn(sine3))
        self.wait(1)
        self.play(freq.animate.set_value(10),filt.animate.set_value(1), run_time = 3)
        self.play(freq.animate.set_value(2),filt.animate.set_value(0), run_time = 3)
        self.play(freq.animate.set_value(6),filt.animate.set_value(0.5), run_time = 3)
        self.wait(1)
        self.play(Indicate(sine1, color=WHITE), run_time=1) 
        self.wait(1)
        self.play(Indicate(sine2, color=WHITE), run_time=1) 
        self.wait(1)
        self.play(Indicate(sine3, color=WHITE), run_time=1) 
        self.wait(1)
        self.play(FadeOut(out_plane), FadeOut(sine), FadeOut(hpf_plane), FadeOut(sine1),FadeOut(lpf_plane), FadeOut(sine2),FadeOut(noninv_plane), FadeOut(sine3))
        self.wait(1)
        self.play(ReplacementTransform(c, d))
        self.wait(1)
        self.play(d.animate.shift(LEFT*2), FadeIn(z1_1), FadeIn(z2_1))
        self.wait(1)
        self.play(TransformFromCopy(d[4],z1_2), FadeOut(z1_1), TransformFromCopy(d[3],z2_2), FadeOut(z2_1), FadeIn(z3_2))
        self.wait(1)
        self.play(ReplacementTransform(z1_2, z1_3), ReplacementTransform(z2_2, z2_3), FadeOut(z3_2))
        self.wait(1)
        self.play(ReplacementTransform(z2_3, z_4), FadeOut(z1_3))
        self.wait(1)
        self.play(TransformFromCopy(z_4, z1), TransformFromCopy(z_4, z2), FadeOut(z_4), FadeIn(z1_rect),FadeIn(z2_rect) )
        self.wait(1)
        self.play(ReplacementTransform(d, e), FadeOut(z1_rect), FadeOut(z2_rect), z2.animate.shift(LEFT*0.5+DOWN*0.5), z1.animate.shift(DOWN*0.25))
        self.wait(1)
        self.play(ReplacementTransform(e, f), z2.animate.shift(RIGHT*0.5+UP*0.5), z1.animate.shift(UP*0.25+LEFT*0.25))
        self.wait(2)
