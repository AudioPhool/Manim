from cmath import pi
from manim import *
from scipy import signal

class SineScope():
    #draws an oscilloscope and can plot a function
    def __init__(self,to_plot,next_to, direction, buff, color, scale):
        #initialises the scope
        self.next_to = next_to
        self.direction = direction 
        self.buff = buff
        self.plot = to_plot
        self.color = color
        self.scale = scale
        self.x_range = [0,2*PI]
        self.y_range = [-1,1]

        #set up axis
        self.ax = NumberPlane(x_range=[0,4.29, 1], x_length=2.5, y_range=[-1,1, 1], y_length=1
                            ).next_to(self.next_to, self.direction, buff = self.buff).set_opacity(0).scale(self.scale)
                    
        #plot custom function from self.plot 
        #e.g "to_plot = lambda x: np.sin((3 * x) + (phi.get_value()))"
        # self.sin = always_redraw(lambda: 
        #             self.ax.plot(self.plot, 
        #             x_range = [0,4*PI/3, 0.01], 
        #             color = self.color,
        #             use_smoothing = False)
        #             )
        #put a dot at the end of the sine
        # self.dot = always_redraw(lambda: 
        #             Dot(point = self.sin.get_end()).scale(self.scale)
        #             )
        #draw a box & a line
        self.b = always_redraw(lambda:RoundedRectangle(corner_radius=0.2,width=2.5, height = 1.25).move_to(self.ax).scale(self.scale))
        self.l = always_redraw(lambda:Line(start=self.b.get_critical_point(LEFT), end=self.b.get_critical_point(RIGHT),color = BLUE_C, stroke_width = 2, stroke_opacity = 1))
        #vgroup for animation purposes eg: FadeIn(scope1.group)
        self.group = VGroup( self.b, self.l)

class anim(Scene):
    def construct(self):
        template = TexTemplate()
        template.add_to_preamble(r"\usepackage[siunitx, RPvoltages, american, europeanresistors]{circuitikz} \ctikzset{multipoles/dipchip/width=1.5} \ctikzset{multipoles/dipchip/pin spacing=0.2}")
        
        a = MathTex(
        r"""\draw (0.5,1) to[short] ++(0.5,0)
        node[op amp, noinv input down, anchor=-] (OA){\texttt{}}
        (OA.-) to[short] ++(-0.5,0) to[short] (0.5, 2.25)
        (OA.out) to[short] ++(0.12, 0) coordinate(OAo) to[short] (3.5,2.25)
        (OA.+) to[short] ++(-0.5,0);""",#0
        r"""\draw (0.5, 2.25) to[C] (3.5,2.25) ;""",#1
        r"""\draw (0.5,0.025) to[short] (0.5,-0.5) node[ground]{} ;""",#2
        r"""\draw (-1.5,1)node[ground]{} to[R] (0.5, 1);""",#3
        stroke_width=2,
        fill_opacity=0,
        stroke_opacity=1,
        tex_environment="circuitikz",
        tex_template=template,
        ).shift(LEFT*0.35)
        
        b = MathTex(
        r"""\draw (0.2,0) node[npn] (n1){}
                  (0.2,-2.2) node[npn] (n2){}
                  (-0.65,0) to[short] (-1,0) to[short] (-1,0.475) to[short] (-1.3, 0.475)
                  (-0.65,-2.2) to[short] (-1,-2.2)to[short] (-1,-2.8) to[short] (-1.3, -2.8) 
                  (0.2,-0.75) to[short] (0.2,-1.45);""",#1
        # r"""\draw (0.5,0.025) to[short] (0.5,-0.5) node[ground]{} ;""",#2
        # r"""\draw (-1.5,1) to[R] (0.5, 1);""",#3
        color = YELLOW_B,
        stroke_width=2,
        fill_opacity=0,
        stroke_opacity=1,
        tex_environment="circuitikz",
        tex_template=template,
        ).scale(0.00003).shift(RIGHT*0.55+DOWN*0.23)

        c = MathTex(
        r"""\draw (0, 0) node[pjfet] (j1){}
                  (0,-2.25) node[pjfet] (j2){}
                  (j1.G) to[short] ++(-0.25,0) to [short] ++(0,0.26) to[short] ++(-0.5,0)
                  (j2.G) to[short] ++(-0.25,0) to [short] ++(0,-0.75) to[short] ++(-0.5,0)
                  (j1.D) to[short] (j2.S);""",#1
        # (OA.-) to[short] ++(-0.5,0) to[short] (0.5, 2.25)
        # (OA.out) to[short] ++(0.12, 0) coordinate(OAo) to[short] (3.5,2.25)
        # (OA.+) to[short] ++(-0.5,0);""",#0
        # r"""\draw (0.5, 2.25) to[C] (3.5,2.25) ;""",#1
        # r"""\draw (0.5,0.025) to[short] (0.5,-0.5) node[ground]{} ;""",#2
        # r"""\draw (-1.5,1) to[R] (0.5, 1);""",#3
        color = YELLOW_B,
        stroke_width=2,
        fill_opacity=0,
        stroke_opacity=1,
        tex_environment="circuitikz",
        tex_template=template,
        ).scale(0.00003*25000).shift(RIGHT*1.05+DOWN*0.075)

        d = MathTex(
        r"""\draw (0.5,1) to[short] ++(0.5,0)
        node[op amp, noinv input down, anchor=-] (OA){\texttt{}}
        (OA.-) to[short] ++(-0.5,0) to[short] (0.5, 2.25)
        (OA.out) to[short] ++(0.12, 0) coordinate(OAo) to[short] (3.5,2.25)
        (OA.+) to[short] ++(-0.5,0);""",#0
        r"""\draw (0.5, 2.25) to[C] (3.5,2.25) ;""",#1
        r"""\draw (0.5,0.025) to [R] (-1,0.025) to[short] (-1,-0.5) node[ground]{} ;""",#2
        r"""\draw (-1.5,1)node[ground]{} to[R] (0.5, 1);""",#3
        stroke_width=2,
        fill_opacity=0,
        stroke_opacity=1,
        tex_environment="circuitikz",
        tex_template=template,
        ).shift(LEFT*1.2)

        e = MathTex(
        r"""\draw (0.5,1) to[short] ++(0.5,0)
        node[op amp, noinv input down, anchor=-] (OA){\texttt{}}
        (OA.-) to[short] ++(-0.5,0) to[short] (0.5, 2.25)
        (OA.out) to[short] ++(0.12, 0) coordinate(OAo) to[short] (3.5,2.25)
        (OA.+) to[short] ++(-0.5,0);""",#0
        r"""\draw (0.5, 2.25) to[C] (3.5,2.25) ;""",#1
        r"""\draw (0.5,0.025) to [R] (-1,0.025) to[short] (-1,-0.5) node[ground]{} ;""",#2
        r"""\draw (-1.5,1)node[ground]{}  to[R] (0.5, 1);""",#3
        stroke_width=2,
        fill_opacity=0,
        stroke_opacity=1,
        tex_environment="circuitikz",
        tex_template=template,
        ).shift(LEFT*1.2)

        f = MathTex(
        r"""\draw (0.5,1) to[short] ++(0.5,0)
        node[op amp, noinv input down, anchor=-] (OA){\texttt{}}
        (OA.-) to[short] ++(-0.5,0) to[short] (0.5, 2.25)
        (OA.out) to[short] ++(0.12, 0) coordinate(OAo) to[short] (3.5,2.25)
        (OA.+) to[short] ++(-0.5,0);""",#0
        r"""\draw (0.5, 2.25) to[C] (3.5,2.25) ;""",#1
        r"""\draw (0.5,0.025) to [R] (-1,0.025) to[short] (-1,-0.5) node[ground]{} ;""",#2
        r"""\draw (0.5, 1) to[R, v=$$] (-1.5,1)node[ground]{} ;""",#3
        stroke_width=2,
        fill_opacity=0,
        stroke_opacity=1,
        tex_environment="circuitikz",
        tex_template=template,
        ).shift(LEFT*1.2)


        self.play(FadeIn(a, b))
        self.wait(0.2)#1
        self.play(a.animate.scale(2.5).shift(UL).shift(LEFT*0.05), b.animate.scale(25000).shift(RIGHT*0.5+UP*0.25))
        self.wait(0.2)#3
        self.play(ReplacementTransform(b,c))
        self.wait(0.2)#5
        self.play(a.animate.scale(0.4).shift(DOWN+RIGHT*0.25), c.animate.scale(0.4).shift(LEFT*1.215+DOWN*0.35))
        self.wait(0.2)#7

        aniline1 = Line(start= UP*0.275+LEFT*4.25,
        end = UP*0.275+LEFT*0.475,
        stroke_width=0
            )
        animdot=Dot(radius=0).move_to(aniline1.get_start()) 
        i_arr1 = always_redraw(lambda:
           Arrow(start = animdot.get_center()-[0.5,0,0],end = animdot.get_center()+[0.5,0,0],stroke_width=15, 
           max_stroke_width_to_length_ratio=100, max_tip_length_to_length_ratio=100, color = BLUE).scale(2).move_to(animdot)
           )
        num = ValueTracker(0)
        numb2 = ValueTracker(0)

        num1 = always_redraw(lambda: DecimalNumber(num.get_value(), 0).shift(UP*0.65+LEFT*1.4))
        num1_l = Tex("mV").scale(0.8).next_to(num1, RIGHT, 0.1)
        num2 = always_redraw(lambda: DecimalNumber(numb2.get_value(), 0).shift(DOWN*0.8+LEFT*1.4))
        num2_l = Tex("mV").scale(0.8).next_to(num2, RIGHT, 0.1)

        self.play(FadeIn(animdot, i_arr1))
        self.wait(0.2)#9
        self.play(MoveAlongPath(animdot, aniline1))
        self.wait(0.2)#11
        self.play(FadeOut(animdot, i_arr1))

        animdot=Dot(radius=0).move_to(aniline1.get_start()) 

        self.play(FadeIn(animdot, i_arr1, num1, num2, num1_l, num2_l))
        self.wait(0.2)#13
        self.play(MoveAlongPath(animdot, aniline1), num.animate.set_value(3))
        self.wait(0.2)#115
        self.play(ReplacementTransform(a,d), FadeOut(i_arr1))
        self.wait(0.2)#17

        aniline1 = Line(start= UP*0.275+LEFT*4.25,
        end = UP*0.275+LEFT*0.475,
        stroke_width=0
            )
        animdot=Dot(radius=0).move_to(aniline1.get_start()) 
        i_arr1 = always_redraw(lambda:
           Arrow(start = animdot.get_center()-[0.5,0,0],end = animdot.get_center()+[0.5,0,0],stroke_width=15, 
           max_stroke_width_to_length_ratio=100, max_tip_length_to_length_ratio=100, color = BLUE).scale(2).move_to(animdot)
           )
        
        aniline2 = Line(start= UP*(-1.1)+LEFT*3.8,
        end = UP*-1.1+LEFT*0.475,
        stroke_width=0
            )
        animdot2=Dot(radius=0).move_to(aniline2.get_start()) 
        i_arr2 = always_redraw(lambda:
           Arrow(start = animdot2.get_center()-[0.5,0,0],end = animdot2.get_center()+[0.5,0,0],stroke_width=15, 
           max_stroke_width_to_length_ratio=100, max_tip_length_to_length_ratio=100, color = RED).scale(1.7).move_to(animdot2)
           )
        
        self.play(FadeIn(animdot, i_arr1, i_arr2, num1, num2, num1_l, num2_l), num.animate.set_value(0))
        self.wait(0.2)#15
        self.play(LaggedStart(MoveAlongPath(animdot, aniline1),MoveAlongPath(animdot2, aniline2),lag_ratio=0.3),
                  LaggedStart(num.animate.set_value(3),numb2.animate.set_value(2),lag_ratio=0.3), run_time = 2)
        self.wait(0.2)#17
        self.play(FadeOut(animdot, i_arr1, i_arr2))
        self.wait(0.2)#19
        self.play(ReplacementTransform(d,e),num.animate.set_value(3),numb2.animate.set_value(2), FadeOut(c))
        self.wait(0.2)#21
        self.play(ReplacementTransform(e,f))
        self.wait(0.2)#23

        aniline1 = Line(end= UP*0.25+LEFT*4.75,
        start = UP*0.25+LEFT*1.8,
        stroke_width=0
            )
        aniline2 = Line(start= DOWN*0.425+RIGHT*2,
        end = DOWN*0.425+RIGHT*2.475,
        stroke_width=0
            )
        aniline3 = Line(start= DOWN*0.425+RIGHT*2.475,
        end = UP*2.05+RIGHT*2.475,
        stroke_width=0
            )
        aniline4 = Line(start= UP*2.05+RIGHT*2.475,
        end = UP*2.05+LEFT*1.8,
        stroke_width=0
            )
        
        aniline5 = Line(start= UP*2.05+LEFT*1.8,
        end = UP*0.25+LEFT*1.8,
        stroke_width=0
            )

        animdot=Dot(radius=0).move_to(aniline1.get_start()) 
        i_arr1 = always_redraw(lambda:
           Arrow(start = animdot.get_center()+[0.5,0,0],end = animdot.get_center()-[0.5,0,0],stroke_width=15, 
           max_stroke_width_to_length_ratio=100, max_tip_length_to_length_ratio=100, color = BLUE).scale(2).move_to(animdot)
           )

        animdot2=Dot(radius=0).move_to(aniline2.get_start()) 
        i_arr2 = always_redraw(lambda:
           Arrow(start = animdot2.get_center()-[0.5,0,0],end = animdot2.get_center()+[0.5,0,0],stroke_width=15, 
           max_stroke_width_to_length_ratio=100, max_tip_length_to_length_ratio=100, color = RED).scale(2).move_to(animdot2)
           )

        rampscope = SineScope(0, b, RIGHT, 1, GREEN, 1)   
        rampline = Line(
            start=rampscope.ax.get_critical_point(LEFT), 
            end = rampscope.ax.get_critical_point(LEFT)+(rampscope.ax.get_critical_point(UR)-rampscope.ax.get_critical_point(LEFT)),
            color = GREEN
            )

        self.play(FadeIn(i_arr1, i_arr2, animdot, animdot2, rampscope.group))
        self.play(MoveAlongPath(animdot, aniline1))
        self.play(FadeOut(i_arr1), MoveAlongPath(animdot2, aniline2), run_time=0.5)

        i_arr3 = always_redraw(lambda:
           Arrow(start = animdot2.get_center()-[0,0.5,0],end = animdot2.get_center()+[0,0.5,0],stroke_width=15, 
           max_stroke_width_to_length_ratio=100, max_tip_length_to_length_ratio=100, color = RED).scale(2).move_to(animdot2)
           )

        self.play(ReplacementTransform(i_arr2, i_arr3), run_time=0.1)
        self.play(MoveAlongPath(animdot2, aniline3))

        i_arr4 = always_redraw(lambda:
           Arrow(start = animdot2.get_center()+[0.5,0,0],end = animdot2.get_center()-[0.5,0,0],stroke_width=15, 
           max_stroke_width_to_length_ratio=100, max_tip_length_to_length_ratio=100, color = RED).scale(2).move_to(animdot2)
           )

        
        
        self.play(ReplacementTransform(i_arr3, i_arr4), run_time=0.1)
        self.play(MoveAlongPath(animdot2, aniline4),Create(rampline))

        i_arr5 = always_redraw(lambda:
           Arrow(start = animdot2.get_center()-[0,-0.5,0],end = animdot2.get_center()+[0,-0.5,0],stroke_width=15, 
           max_stroke_width_to_length_ratio=100, max_tip_length_to_length_ratio=100, color = RED).scale(2).move_to(animdot2)
           )
        

        
        self.play(ReplacementTransform(i_arr4, i_arr5), run_time=0.1)
        self.play(MoveAlongPath(animdot2, aniline5))

        i_arr6 = always_redraw(lambda:
           Arrow(start = animdot2.get_center()+[0.5,0,0],end = animdot2.get_center()-[0.5,0,0],stroke_width=15, 
           max_stroke_width_to_length_ratio=100, max_tip_length_to_length_ratio=100, color = RED).scale(2).move_to(animdot2)
           )

        self.play(ReplacementTransform(i_arr5, i_arr6), run_time=0.1)
        self.play(MoveAlongPath(animdot2, aniline1))

        self.play(FadeOut(i_arr6))
        self.wait(0.2)#41
        