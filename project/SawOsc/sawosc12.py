from cmath import pi
from manim import *
from scipy import signal

def clip(func):
    if func>1:
        result = 1
    elif func<-1:
        result = -1
    else:
        result = func
    return result

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
        self.x_range = [0, 2*PI]
        self.y_range = [-1,1]

        #set up axis
        self.ax = NumberPlane(x_range=[0,4.29, 1], x_length=2.5, y_range=[-1,1, 1], y_length=1
                            ).next_to(self.next_to, self.direction, buff = self.buff).set_opacity(0).scale(self.scale)
                    
        #plot custom function from self.plot 
        #e.g "to_plot = lambda x: np.sin((3 * x) + (phi.get_value()))"
        self.sin = always_redraw(lambda: 
                    self.ax.plot(self.plot, 
                    x_range = [0,4*PI/3, 0.01], 
                    color = self.color,
                    stroke_width=3,
                    use_smoothing = False)
                    )
        #put a dot at the end of the function
        self.dot = always_redraw(lambda: 
                    Dot(point = self.sin.get_end()).scale(self.scale)
                    )
        #draw a box & a line
        self.b = always_redraw(lambda:RoundedRectangle(corner_radius=0.2,width=2.5, height = 1.25).move_to(self.ax).scale(self.scale))
        self.l = always_redraw(lambda:Line(start=self.b.get_critical_point(LEFT), end=self.b.get_critical_point(RIGHT),color = BLUE_C, stroke_width = 2, stroke_opacity = 1))
        #vgroup for animation purposes eg: FadeIn(scope1.group)
        self.group = VGroup(self.sin, self.dot, self.b, self.l)

class anim(Scene):
    def construct(self):
        template = TexTemplate()
        template.add_to_preamble(r"\usepackage[siunitx, RPvoltages, american, europeanresistors]{circuitikz} \ctikzset{multipoles/dipchip/width=1.5} \ctikzset{multipoles/dipchip/pin spacing=0.2}")
        
        phi = ValueTracker(-0.1)

        

        a = MathTex(
        r"""\draw (0.5,1) to[short] ++(0.5,0)
        node[op amp, noinv input down, anchor=-] (OA){TL072}
        (OA.-) to[short] ++(-0.5,0) to[short] (0.5, 2.25)
        (OA.out) to[short] ++(0.12, 0) coordinate(OAo) to[short] (3.5,2.25) 
        (OA.+) node[ground]{};""",#0
        r"""\draw (0.5, 2.25) to[R,l=$R_2$] (3.5,2.25) ;""",#1
        r"""\draw (0.5, 2.25) to[short](0.5, 3.5) to[C, l=$C_1$] (3.5,3.5) to[short] (3.5,2.25) ;""",#2
        r"""\draw (-1.5,1) to[R, l=$R_1$] (0.5,1) ;""",#3
        stroke_width=2,
        fill_opacity=0,
        stroke_opacity=1,
        tex_environment="circuitikz",
        tex_template=template,
        ).scale(0.8).shift(RIGHT*0.15)

        inscope1 = SineScope(lambda x: ((signal.sawtooth(5*x + phi.get_value())*0.25)+0.25), a[3], LEFT, 0.5, YELLOW, 1)
        outscope1 = SineScope(lambda x: ((signal.sawtooth(5*x + phi.get_value())*0.25)+0.25), a, RIGHT, 0.2, BLUE, 1)

        eq = MathTex("f_{lpf}=1 / {2 \pi R_2 C_1}").shift(UP+LEFT*3)

        self.play(FadeIn(a, eq, inscope1.group, outscope1.group))
        self.wait(0.2)#1

        b = MathTex(
        r"""\draw (0.5,1) to[short] ++(0.5,0)
        node[op amp, noinv input down, anchor=-] (OA){TL072}
        (OA.-) to[short] ++(-0.5,0) to[short] (0.5, 2.25)
        (OA.out) to[short] ++(0.12, 0) coordinate(OAo) to[short] (3.5,2.25) 
        (OA.+) node[ground]{};""",#0
        r"""\draw (0.5, 2.25) to[R,l=$40k$] (3.5,2.25) ;""",#1
        r"""\draw (0.5, 2.25) to[short](0.5, 3.5) to[C, l=$200pF$] (3.5,3.5) to[short] (3.5,2.25) ;""",#2
        r"""\draw (-1.5,1) to[R, l=$R_1$] (0.5,1) ;""",#3
        stroke_width=2,
        fill_opacity=0,
        stroke_opacity=1,
        tex_environment="circuitikz",
        tex_template=template,
        ).scale(0.8).shift(RIGHT*1)

        inscope2 = SineScope(lambda x: ((signal.sawtooth(5*x + phi.get_value())*0.25)+0.25), b[3], LEFT, 0.5, YELLOW, 1)
        outscope2 = SineScope(lambda x: ((signal.sawtooth(5*x + phi.get_value())*0.25)+0.25), b, RIGHT, 0.2, BLUE, 1)
        eqb = MathTex("20kHz =1 / {2 \pi*40k*200pF}").shift(UP+LEFT*3.7)

        c = MathTex(
        r"""\draw (0.5,1) to[short] ++(0.5,0)
        node[op amp, noinv input down, anchor=-] (OA){TL072}
        (OA.-) to[short] ++(-0.5,0) to[short] (0.5, 2.25)
        (OA.out) to[short] ++(0.12, 0) coordinate(OAo) to[short] (3.5,2.25) 
        (OA.+) node[ground]{};""",#0
        r"""\draw (0.5, 2.25) to[R,l=$R_2$] (3.5,2.25) ;""",#1
        r"""\draw (0.5, 2.25) to[short](0.5, 3.5) to[C, l=$200pF$] (3.5,3.5) to[short] (3.5,2.25) ;""",#2
        r"""\draw (-1.5,1) to[R, l=$R_1$] (0.5,1) ;""",#3
        stroke_width=2,
        fill_opacity=0,
        stroke_opacity=1,
        tex_environment="circuitikz",
        tex_template=template,
        ).scale(0.8).shift(RIGHT*1)

        inscope3 = SineScope(lambda x: ((signal.sawtooth(5*x + phi.get_value())*0.25)+0.25), c[3], LEFT, 0.5, YELLOW, 1)
        outscope3 = SineScope(lambda x: ((signal.sawtooth(5*x + phi.get_value())*0.25)+0.25), c, RIGHT, 0.2, BLUE, 1)
        eqc = MathTex("Gain = -R_2 / R_1}").shift(UP+LEFT*3.5)
        eqb2 = MathTex("f_{lpf}=1 / {2 \pi R_2 C_1}").shift(UP*0.5+LEFT*3)

        self.play(ReplacementTransform(a, b), ReplacementTransform(eq, eqb),ReplacementTransform(inscope1.group, inscope2.group),
                                                                            ReplacementTransform(outscope1.group, outscope2.group))
        self.wait(1)#3
        self.play(ReplacementTransform(b, c), ReplacementTransform(eqb, eqc),ReplacementTransform(inscope2.group, inscope3.group),
                                                                            ReplacementTransform(outscope2.group, outscope3.group))
        self.wait(1)#5

        d = MathTex(
        r"""\draw (0.5,1) to[short] ++(0.5,0)
        node[op amp, noinv input down, anchor=-] (OA){TL072}
        (OA.-) to[short] ++(-0.5,0) to[short] (0.5, 2.25)
        (OA.out) to[short] ++(0.12, 0) coordinate(OAo) to[short] (3.5,2.25) 
        (OA.+) node[ground]{};""",#0
        r"""\draw (0.5, 2.25) to[R,l=$40k$] (3.5,2.25) ;""",#1
        r"""\draw (0.5, 2.25) to[short](0.5, 3.5) to[C, l=$200pF$] (3.5,3.5) to[short] (3.5,2.25) ;""",#2
        r"""\draw (-1.5,1) to[R, l=$10k$] (0.5,1) ;""",#3
        stroke_width=2,
        fill_opacity=0,
        stroke_opacity=1,
        tex_environment="circuitikz",
        tex_template=template,
        ).scale(0.8).shift(RIGHT*1)

        eqd = MathTex("-4X = 40k / 10k").shift(UP+LEFT*3.5)
        eqb22 = MathTex("20kHz =1 / {2 \pi*40k*200pF}").shift(UP*0.5+LEFT*3.7)
        inscope4 = SineScope(lambda x: ((signal.sawtooth(5*x + phi.get_value())*0.25)+0.25), c[3], LEFT, 0.5, YELLOW, 1)
        outscope4 = SineScope(lambda x: (clip((signal.sawtooth(5*x + phi.get_value())*-1)-1)), c, RIGHT, 0.2, BLUE, 1)

        self.play(ReplacementTransform(c, d), ReplacementTransform(eqc, eqd),  ReplacementTransform(inscope3.group, inscope4.group),  
                                                                               ReplacementTransform(outscope3.group, outscope4.group), FadeIn(eqb2))
        self.wait(1)#7
        self.play(ReplacementTransform(eqb2, eqb22))
        self.wait(1)#9

        e = MathTex(
        r"""\draw (0.5,1) to[short] ++(0.5,0)
        node[op amp, noinv input down, anchor=-] (OA){TL072}
        (OA.-) to[short] ++(-0.5,0) to[short] (0.5, 2.25)
        (OA.out) to[short] ++(0.12, 0) coordinate(OAo) to[short] (3.5,2.25) 
        (OA.+) node[ground]{};""",#0
        r"""\draw (0.5, 2.25) to[R,l=$40k$] (3.5,2.25) ;""",#1
        r"""\draw (0.5, 2.25) to[short](0.5, 3.5) to[C, l=$200pF$] (3.5,3.5) to[short] (3.5,2.25) ;""",#2
        r"""\draw (-1.5,1) to[R, l=$10k$] (0.5,1) ;""",#3
        r"""\draw (0.5,1) to[R, l_=$56k$] (0.5,-0.5) to[vR, l_=$5.6k$] (0.5,-2)node[vee]{-15v} ;""",#3
        stroke_width=2,
        fill_opacity=0,
        stroke_opacity=1,
        tex_environment="circuitikz",
        tex_template=template,
        ).scale(0.7).shift(RIGHT*1)

        eqd2 = MathTex("Gain = -4X").shift(UP+LEFT*3.5)
        eqd3 = MathTex("-250uA = -15v/60k").shift(UP+LEFT*3.5)
        eqe2 = MathTex("f_{lpf} = 20k").shift(UP*0.5+LEFT*3.5)
        eqf = Tex("Adj R4 to center").shift(UP*-2+LEFT*3)
        trim = ValueTracker(-1)
        inscope5 = SineScope(lambda x: ((signal.sawtooth(5*x + phi.get_value())*0.25)+0.25), c[3], LEFT, 0.5, YELLOW, 1)
        outscope5 = SineScope(lambda x: (clip((signal.sawtooth(5*x + phi.get_value())*-1)+trim.get_value())), c, RIGHT, 0.2, BLUE, 1)

        self.play(FadeTransform(d,e), ReplacementTransform(eqd, eqd2), ReplacementTransform(eqb22, eqe2), FadeIn(eqf),  ReplacementTransform(inscope4.group, inscope5.group),  
                                                                               ReplacementTransform(outscope4.group, outscope5.group))
        self.wait(0.2)#11    

        aniline1 = Line(start= e[4].get_critical_point(DOWN)+[0.35,0,0],
        end = e[4].get_critical_point(UP)+[0.35,0,0],
        stroke_width=0
            )
        animdot=Dot(radius=0).move_to(aniline1.get_start()) 
        i_arr1 = always_redraw(lambda:
           Arrow(start = animdot.get_center()-[0,0.5,0],end = animdot.get_center()+[0,0.5,0],stroke_width=15, 
           max_stroke_width_to_length_ratio=100, max_tip_length_to_length_ratio=100, color = RED).scale(2).move_to(animdot)
           )

        self.play(FadeIn(animdot, i_arr1),FadeOut(eqe2), ReplacementTransform(eqd2, eqd3))
        self.wait(0.2)#13
        self.play(MoveAlongPath(animdot, aniline1))
        self.wait(0.2)#15
        self.play(FadeOut(animdot, i_arr1))
        self.wait(0.2)#17


        aniline1 = Line(start= e[1].get_critical_point(RIGHT)+[0,-0.2,0],
        end = e[1].get_critical_point(LEFT)+[0,-0.2,0],
        stroke_width=0
            )
        animdot=Dot(radius=0).move_to(aniline1.get_start()) 
        i_arr1 = always_redraw(lambda:
           Arrow(start = animdot.get_center()+[0.5,-0,0],end = animdot.get_center()-[0.5,0,0],stroke_width=15, 
           max_stroke_width_to_length_ratio=100, max_tip_length_to_length_ratio=100, color = BLUE).scale(2).move_to(animdot)
           )

        self.play(FadeIn(animdot, i_arr1),FadeOut(eqd3))
        self.wait(0.2)#19
        self.play(MoveAlongPath(animdot, aniline1), trim.animate.set_value(0))
        self.wait(0.2)#21
        self.play(FadeOut(animdot, i_arr1))
        self.wait(0.2)#23
        