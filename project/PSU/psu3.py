from cmath import pi
from manim import *

class anim(Scene):
    def construct(self):
        template = TexTemplate()
        template.add_to_preamble(r"\usepackage[siunitx, RPvoltages, american, europeanresistors]{circuitikz}")

        a = MathTex(
        r"""\draw(0,0) to[sV, v=$$, voltage shift=1]  (0,2) (0,0) to[R] (3,0)  (0,2) to[short] (3,2);""",
        r"""\draw(3,2) to[diode, v^< = $$, voltage shift=1] (3,0); """,
        
        stroke_width=2,
        fill_opacity=0,
        stroke_opacity=1,
        tex_environment="circuitikz",
        tex_template=template,
        )
        
        b = MathTex(
        r"""\draw(0,0) to[sV, v=$$, voltage shift=1]  (0,2) (0,0) to[R, v_> = $$, voltage shift=1] (3,0)  (0,2) to[short] (3,2);""",
        r"""\draw(3,2) to[diode, v^< = $$, voltage shift=1] (3,0); """,
        
        stroke_width=2,
        fill_opacity=0,
        stroke_opacity=1,
        tex_environment="circuitikz",
        tex_template=template,
        ).shift(UP*1.65)
        
        c = MathTex(
        r"""\draw (4,0) to[diode, v_< = $$, voltage shift=1] (0,0);""",
        
        stroke_width=2,
        fill_opacity=0,
        stroke_opacity=0.3,
        tex_environment="circuitikz",
        tex_template=template,
        ).shift(DOWN*1.75).scale(3).set_z(-1)
        
        d = MathTex(
        r"""\draw(0,0) to[sV, v=$$, voltage shift=1]  (0,2) (0,0) to[R, v_> = $$, voltage shift=1] (3,0)  (0,2) to[short] (3,2);""",
        r"""\draw(3,2) to[diode, v^< = $0.7V$, voltage shift=1] (3,0); """,
        
        stroke_width=2,
        fill_opacity=0,
        stroke_opacity=1,
        tex_environment="circuitikz",
        tex_template=template,
        ).shift(RIGHT*1.65).scale(1.35)
        
        f = MathTex(
        r"""\draw(0,0) to[sV, v=$$, voltage shift=1]  (0,2) (0,0) to[R, v_> = $$, voltage shift=1] (3,0)  (0,2) to[short] (3,2);""",
        r"""\draw(3,2) to[short, v^< = $0.7V$, voltage shift=1] (3,0); """,
        
        stroke_width=2,
        fill_opacity=0,
        stroke_opacity=1,
        tex_environment="circuitikz",
        tex_template=template,
        ).shift(RIGHT*1.65).scale(1.35)
        
        g = MathTex(
        r"""\draw(0,0) to[sV, v=$$, voltage shift=1]  (0,2) (0,0) to[R, v_> = $$, voltage shift=1] (3,0)  (0,2) to[short] (3,2);""",
        r"""\draw(3,2) to[open,o-o] (3,0); """,
        
        stroke_width=2,
        fill_opacity=0,
        stroke_opacity=1,
        tex_environment="circuitikz",
        tex_template=template,
        ).shift(RIGHT*0.6).scale(1.35)

        self.play(FadeIn(a))
        self.wait(0.2)
        
        P = Rectangle(height=2, width=4, color=WHITE, fill_color = BLUE_A, fill_opacity = 0.9).shift(LEFT*2)
        N = Rectangle(height=2, width=4, color=WHITE, fill_color = RED_A, fill_opacity = 0.9).shift(RIGHT*2)
        P_l = MathTex("P").scale(0.75).shift(RIGHT*3.5+UP*0.5)
        N_l = MathTex("N").scale(0.75).shift(LEFT*3.5+UP*0.5)
        
        
        dep_width = ValueTracker(1.5)
        dep = always_redraw(lambda: 
            Rectangle(width=dep_width.get_value(),
                      height = 2,
                      fill_color = GRAY_C,
                      fill_opacity = 0.8,
                      stroke_color=BLACK,
                      stroke_width=0.5  
            ))
        #self.play(a.animate.set_opacity(0.15), FadeIn(dep2))
        self.wait(0.2)
                        
        e = ValueTracker(0.01)

        dep2 = always_redraw(lambda: 
            Rectangle(width=(dep_width.get_value())-(np.sin(3*e.get_value())),
                      height = 2,
                      fill_color = GRAY_C,
                      fill_opacity = 0.8,
                      stroke_color=BLACK,
                      stroke_width=0.5  
            ).move_to(P.get_critical_point(RIGHT)))
        
        PN = VGroup(P, N,P_l,N_l)
        self.play(a.animate.set_opacity(0.15), FadeIn(P), FadeIn(N), FadeIn(P_l), FadeIn(N_l),FadeIn(dep2), 
                  PN.animate.shift(DOWN*2),dep2.animate.shift(DOWN*2), FadeTransform(a,b), TransformFromCopy(a[1], c))
        
        l1 = always_redraw(lambda:
        MathTex("+",color=GOLD).shift(LEFT*((dep_width.get_value()/2.0-(np.sin(3*e.get_value()))/2.0)+0.1)+UP*-0.75))
        l2 = always_redraw(lambda:
        MathTex("-",color=GOLD).shift(RIGHT*((dep_width.get_value()/2.0-(np.sin(3*e.get_value()))/2.0)+0.1)+UP*-0.75))
        a1 = always_redraw(lambda:
        Arrow(start=LEFT*((dep_width.get_value()/2.0)-(np.sin(3*e.get_value()))/2.0-0.1)+UP*-0.75,end=RIGHT*((dep_width.get_value()/2.0-(np.sin(3*e.get_value()))/2.0)-0.1)+UP*-0.75, 
              buff=3, color=GOLD, stroke_width=2))
        l3 = always_redraw(lambda:
            MathTex("E",color=GOLD).shift(UP*-0.45).set_opacity(0.90-(((np.sin(3*e.get_value()))*0.10))
            ).scale(0.75-(((np.sin(3*e.get_value()))*0.25))))
        
        self.play(FadeIn(l1,l2,l3,a1))
        self.wait(0.2)
        
        axes = Axes(x_range = [0, 5, 1], x_length=3, y_range=[-1,1,1], y_length=2,tips=False).shift(LEFT*5+UP*1.75)
        graph2 = always_redraw(lambda : 
        axes.plot(lambda x : np.sin(3*x), x_range = [0, e.get_value()], color = YELLOW)
        )
        dot2 = always_redraw(lambda : Dot(fill_color = YELLOW, fill_opacity = 0.8).scale(0.5).move_to(graph2.get_end())
        )
        
        i_arr = always_redraw(lambda:
           Arrow( start = UP*(1),#+np.sin(3*e.get_value())),
                  end = DOWN*(1),#+np.sin(3*e.get_value())),
                  color = YELLOW,
                  stroke_width=5
               
           ).set_opacity(0.5+(0.5*np.sin(3*e.get_value())+0.5)).scale(0.5+(0.3*np.sin(3*e.get_value())+0.3)).shift(RIGHT*5+UP*1.75)
           ) 
        i_label = MathTex("I = ").shift(RIGHT*4.5+UP*1.75)
        self.play(FadeIn(axes,graph2,dot2,i_arr,i_label))
        self.play(e.animate.set_value(PI/6), run_time=3, rate_func = linear)
        self.wait(1)
        self.play(e.animate.set_value(3*PI/6), run_time=5, rate_func = linear)
        self.wait(1)
        self.play(e.animate.set_value(4*PI/3+PI/6), run_time=10, rate_func = linear)
        self.wait(0.2)
        self.play(axes.animate.shift(DOWN*1.65+LEFT*0.55), b.animate.shift(DOWN*1.65+RIGHT*1.1).scale(1.35), e.animate.set_value(0.001),
                  FadeOut(i_arr), FadeOut(P), FadeOut(N), FadeOut(P_l), FadeOut(N_l),FadeOut(dep2),FadeOut(l1,l2,l3,a1,c,i_label))
        v_lab = MathTex("V_{in} = ").shift(UP*2+LEFT*4)
        number = always_redraw(lambda:DecimalNumber(
                 3*np.sin(3*e.get_value()), 
                 show_ellipsis=False, 
                 num_decimal_places=1
                 ).scale(1).next_to(v_lab, RIGHT))
        
        self.wait(0.2)
        self.play(FadeIn(v_lab, number))
        self.wait(0.2)
        self.play(e.animate.set_value(0.083), run_time=2, rate_func = linear)
        self.wait(1)
        
        vr_lab = MathTex("V_{R} = ").shift(DOWN*2.5+RIGHT)
        number_r1 = always_redraw(lambda:DecimalNumber(
                 3*np.sin(3*e.get_value())-0.7, 
                 show_ellipsis=False, 
                 num_decimal_places=1
                 ).scale(1).next_to(vr_lab, RIGHT))
        number_r2 = always_redraw(lambda:DecimalNumber(
                 0.0, 
                 show_ellipsis=False, 
                 num_decimal_places=1
                 ).scale(1).next_to(vr_lab, RIGHT))
        
        self.play(Transform(b,d), run_time = 1.5)
        self.wait(0.2)
        self.play(Transform(b,f), FadeIn(vr_lab, number_r1), run_time = 1.5)
        self.wait(0.2)
        self.play(e.animate.set_value(PI/3-0.083), run_time=5, rate_func = linear)
        self.play(FadeTransform(number_r1, number_r2),Transform(b,g))
        self.wait(0.2)
        self.play(e.animate.set_value(2*PI/3+0.083), run_time=5, rate_func = linear)
        self.play(Transform(b,f), FadeTransform(number_r2, number_r1))
        self.play(e.animate.set_value(3*PI/3-0.083), run_time=5, rate_func = linear)
        self.play(FadeTransform(number_r1, number_r2),Transform(b,g))
        self.play(e.animate.set_value(4*PI/3), run_time=5, rate_func = linear)
        self.wait(0.2)

        
        
        
        