from turtle import circle, dot, fillcolor
from manim import *

class anim(Scene):
    def construct(self):
        template = TexTemplate()
        template.add_to_preamble(r"\usepackage[siunitx, RPvoltages, american, europeanresistors]{circuitikz}")

        a = MathTex(
        r"""\draw(0,0) to[sV, v=$$, voltage shift=1]  (0,2) (0,0) to[diode, v = $$] (3,0)
        (3,2) to[R] (3,0)  (0,2) to[short] (3,2);""",
        
        stroke_width=2,
        fill_opacity=0,
        stroke_opacity=1,
        tex_environment="circuitikz",
        tex_template=template,
        )
        
        b = MathTex(
        r"""\draw(0,0) to[sV, v=$$, voltage shift=1]  (0,2) (0,0) to[diode, v = $$] (3,0)
        (3,2) to[R] (3,0)  (0,2) to[short] (3,2);""",
        
        stroke_width=2,
        fill_opacity=0,
        stroke_opacity=1,
        tex_environment="circuitikz",
        tex_template=template,
        ).shift(UP*1.65)

        self.play(FadeIn(a))
        self.wait(0.2)
        self.play(a.animate.scale(5).shift(UP*6, LEFT*2.5), run_time = 5)
        self.wait(0.2)

        P = Rectangle(height=2, width=4, color=WHITE, fill_color = RED_A, fill_opacity = 0.85).shift(LEFT*2)
        N = Rectangle(height=2, width=4, color=WHITE, fill_color = BLUE_A, fill_opacity = 0.85).shift(RIGHT*2)
        P_l = MathTex("P").scale(0.75).shift(LEFT*3.5+UP*0.5)
        N_l = MathTex("N").scale(0.75).shift(RIGHT*3.5+UP*0.5)
        
        e1 = VGroup(
            Circle(radius = 0.5,
                   color = WHITE, 
                   fill_color = BLUE_C,
                   fill_opacity = 1,
                   stroke_width = 0.5),
            MathTex("e^-",
                    stroke_color = BLACK,
                    stroke_width = 0.75,
                    stroke_opacity=0.75).scale(1.35)
            ).shift(RIGHT*2+DOWN*0.5).scale(0.5)
        
        e2 = VGroup(
            Circle(radius = 0.5,
                   color = WHITE, 
                   fill_color = BLUE_C,
                   fill_opacity = 1,
                   stroke_width = 0.5),
            MathTex("e^-",
                    stroke_color = BLACK,
                    stroke_width = 0.75,
                    stroke_opacity=0.75).scale(1.35)
            ).shift(RIGHT*3+UP*0.5).scale(0.5)
        
        e3 = VGroup(
            Circle(radius = 0.5,
                   color = WHITE, 
                   fill_color = BLUE_C,
                   fill_opacity = 1,
                   stroke_width = 0.5),
            MathTex("e^-",
                    stroke_color = BLACK,
                    stroke_width = 0.75,
                    stroke_opacity=0.75).scale(1.35)
            ).shift(RIGHT*2.65+DOWN*0.1).scale(0.5)
        
        h1 = VGroup(
            Circle(radius = 0.5,
                   color = WHITE, 
                   fill_color = RED_C,
                   fill_opacity = 1,
                   stroke_width = 0.5),
            MathTex("h^+",
                    stroke_color = BLACK,
                    stroke_width = 0.75,
                    stroke_opacity=0.75).scale(1.35)
            ).shift(LEFT*2.3+UP*0.35).scale(0.5)
        h2 = VGroup(
            Circle(radius = 0.5,
                   color = WHITE, 
                   fill_color = RED_C,
                   fill_opacity = 1,
                   stroke_width = 0.5),
            MathTex("h^+",
                    stroke_color = BLACK,
                    stroke_width = 0.75,
                    stroke_opacity=0.75).scale(1.35)
            ).shift(LEFT*1.65+DOWN*0.35).scale(0.5)
        h3 = VGroup(
            Circle(radius = 0.5,
                   color = WHITE, 
                   fill_color = RED_C,
                   fill_opacity = 1,
                   stroke_width = 0.5),
            MathTex("h^+",
                    stroke_color = BLACK,
                    stroke_width = 0.75,
                    stroke_opacity=0.75).scale(1.35)
            ).shift(LEFT*2.5+DOWN*0.25).scale(0.5)
        
        dep_width = ValueTracker(0)
        dep = always_redraw(lambda: 
            Rectangle(width=dep_width.get_value(),
                      height = 2,
                      fill_color = GRAY_C,
                      fill_opacity = 0.8,
                      stroke_color=BLACK,
                      stroke_width=0.5  
            ))
        self.play(a.animate.set_opacity(0.15), FadeIn(P), FadeIn(N), FadeIn(P_l), FadeIn(N_l), FadeIn(dep))
        self.wait(0.2)
        self.play(DrawBorderThenFill(e1),DrawBorderThenFill(e2),DrawBorderThenFill(e3))
        self.wait(0.2)
        self.play(DrawBorderThenFill(h1),DrawBorderThenFill(h2),DrawBorderThenFill(h3))
        self.wait(0.2)
        self.play(FadeTransform(e1, Dot(radius=0).shift(DOWN*0.43)),FadeTransform(h2, Dot(radius=0).shift(DOWN*0.43)),dep_width.animate.set_value(0.5) )
        self.remove(e1, h2)
        self.wait(0.2)
        self.play(FadeTransform(e2, Dot(radius=0).shift(UP*0.43)),FadeTransform(h1, Dot(radius=0).shift(UP*0.43)),dep_width.animate.set_value(1) )
        self.remove(e2, h1)
        self.wait(0.2)
        self.play(FadeTransform(e3, Dot(radius=0).shift(DOWN*0.18)),FadeTransform(h3, Dot(radius=0).shift(DOWN*0.18)),dep_width.animate.set_value(1.5) )
        self.remove(e3, h3)
        self.wait(0.2)
        
        e = ValueTracker(0.01)

        dep2 = always_redraw(lambda: 
            Rectangle(width=(dep_width.get_value())+(np.sin(3*e.get_value())),
                      height = 2,
                      fill_color = GRAY_C,
                      fill_opacity = 0.8,
                      stroke_color=BLACK,
                      stroke_width=0.5  
            ).shift(DOWN*2))
        
        PN = VGroup(P, N,P_l,N_l)
        self.play(PN.animate.shift(DOWN*2), FadeTransform(a,b),
                  FadeTransform(dep,dep2))
        
        l1 = always_redraw(lambda:
        MathTex("+",color=GOLD).shift(RIGHT*((dep_width.get_value()/2.0)+0.1)+UP*-0.75))
        l2 = always_redraw(lambda:
        MathTex("-",color=GOLD).shift(LEFT*((dep_width.get_value()/2.0)+0.1)+UP*-0.75))
        a1 = always_redraw(lambda:
        Arrow(start=RIGHT*((dep_width.get_value()/2.0)-0.1)+UP*-0.75,end=LEFT*((dep_width.get_value()/2.0)-0.1)+UP*-0.75, 
              buff=3, color=GOLD, stroke_width=2))
        l3 = MathTex("E",color=GOLD).shift(UP*-0.45)
        
        self.play(FadeIn(l1,l2,l3,a1))
        self.wait(0.2)
        
        axes = Axes(x_range = [0, 4, 1], x_length=3, y_range=[-1,1,1], y_length=2,tips=False).shift(LEFT*4.5+UP*2)
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
               
           ).scale(1.2-(0.5*np.sin(3*e.get_value())+0.5)).shift(RIGHT*4.25+UP*2)
           ) 
        i_label = MathTex("I = ").shift(RIGHT*3.5+UP*2)
        self.play(FadeIn(axes,graph2,dot2,i_arr,i_label))
        self.play(e.animate.set_value(PI), run_time=10, rate_func = linear)
        self.wait(0.2)

        

        