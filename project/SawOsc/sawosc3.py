from cmath import pi
from manim import *
from scipy import signal

result = 0
t = 0
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
def ramp(x = 0, on = 0):
    global result
    if(on == 1):
        if(x < 0 < PI/2):
            result = x/16
        else:
            result = result    
    else:
        result = 0
    return result

class anim(Scene):
    def construct(self):
        template = TexTemplate()
        template.add_to_preamble(r"\usepackage[siunitx, RPvoltages, american, europeanresistors]{circuitikz} \ctikzset{multipoles/dipchip/width=1.5} \ctikzset{multipoles/dipchip/pin spacing=0.2}")
        
        on = ValueTracker(0)

        a = MathTex(
        r"""\draw (0.5,1) to[short] ++(0.5,0)
        node[op amp, noinv input down, anchor=-] (OA){\texttt{}}
        (OA.-) to[short] ++(-0.5,0) to[short] (0.5, 2.25)
        (OA.out) to[short] ++(0.12, 0) coordinate(OAo) to[short] (3.5,2.25)
        (OA.+) to[short] ++(-0.5,0);""",#0
        r"""\draw (0.5, 2.25) to[C] (3.5,2.25) ;""",#1
        r"""\draw (0.5,0.025) to[short] (0.5,-0.5) node[ground]{} ;""",#2
        r"""\draw (-1.5,1) to[R] (0.5, 1);""",#3
        stroke_width=2,
        fill_opacity=0,
        stroke_opacity=1,
        tex_environment="circuitikz",
        tex_template=template,
        ).scale(0.7)

        self.play(FadeIn(a))
        self.wait(0.2)#1
        self.play(Indicate(a[1], color = RED))
        self.wait(0.2)#3
        self.play(Indicate(a[2]), color = RED)
        self.wait(0.2)#5
        
        
        b = MathTex(
        r"""\draw (0.5,1) to[short] ++(0.5,0)
        node[op amp, noinv input down, anchor=-] (OA){\texttt{}}
        (OA.-) to[short] ++(-0.5,0) to[short] (0.5, 2.25)
        (OA.out) to[short] ++(0.12, 0) coordinate(OAo) to[short] (3.5,2.25)
        (OA.+) to[short] ++(-0.5,0);""",#0
        r"""\draw (0.5, 2.25) to[C] (3.5,2.25) ;""",#1
        r"""\draw (0.5,0.025) to[short] (0.5,-0.5) node[ground]{} ;""",#2
        r"""\draw (-1.5,1) to[R, v^=$$] (0.5, 1);""",#3
        stroke_width=2,
        fill_opacity=0,
        stroke_opacity=1,
        tex_environment="circuitikz",
        tex_template=template,
        ).scale(0.7)

        aniline1 = Line(start= UP*0.2+LEFT*2.25,
        end = UP*0.2+LEFT*0.475,
        stroke_width=0
            )
        aniline2 = Line(start= DOWN*0.3+RIGHT*2,
        end = DOWN*0.3+RIGHT*2.475,
        stroke_width=0
            )
        aniline3 = Line(start= DOWN*0.3+RIGHT*2.475,
        end = UP*1.425+RIGHT*2.475,
        stroke_width=0
            )
        aniline4 = Line(start= UP*1.425+RIGHT*2.475,
        end = UP*1.425+LEFT*0.475,
        stroke_width=0
            )
        
        aniline5 = Line(start= UP*1.425+LEFT*0.475,
        end = UP*0.2+LEFT*0.475,
        stroke_width=0
            )

        animdot=Dot(radius=0).move_to(aniline1.get_start()) 
        i_arr1 = always_redraw(lambda:
           Arrow(start = animdot.get_center()-[0.5,0,0],end = animdot.get_center()+[0.5,0,0],stroke_width=15, 
           max_stroke_width_to_length_ratio=100, max_tip_length_to_length_ratio=100, color = BLUE).scale(2).move_to(animdot)
           )
        
        animdot2=Dot(radius=0).move_to(aniline2.get_start()) 
        i_arr2 = always_redraw(lambda:
           Arrow(start = animdot2.get_center()-[0.5,0,0],end = animdot2.get_center()+[0.5,0,0],stroke_width=15, 
           max_stroke_width_to_length_ratio=100, max_tip_length_to_length_ratio=100, color = RED).scale(2).move_to(animdot2)
           )
        
        self.play(FadeTransform(a, b))
        self.play(FadeIn(i_arr1, i_arr2, animdot, animdot2))
        self.play(MoveAlongPath(animdot, aniline1), run_time = 0.5)
        self.play(MoveAlongPath(animdot2, aniline2), run_time=0.25)

        i_arr3 = always_redraw(lambda:
           Arrow(start = animdot2.get_center()-[0,0.5,0],end = animdot2.get_center()+[0,0.5,0],stroke_width=15, 
           max_stroke_width_to_length_ratio=100, max_tip_length_to_length_ratio=100, color = RED).scale(2).move_to(animdot2)
           )

        self.play(ReplacementTransform(i_arr2, i_arr3), run_time=0.25)
        self.play(MoveAlongPath(animdot2, aniline3))

        i_arr4 = always_redraw(lambda:
           Arrow(start = animdot2.get_center()+[0.5,0,0],end = animdot2.get_center()-[0.5,0,0],stroke_width=15, 
           max_stroke_width_to_length_ratio=100, max_tip_length_to_length_ratio=100, color = RED).scale(2).move_to(animdot2)
           )

        self.play(ReplacementTransform(i_arr3, i_arr4), run_time=0.25)
        self.play(MoveAlongPath(animdot2, aniline4))

        i_arr5 = always_redraw(lambda:
           Arrow(start = animdot2.get_center()-[0,-0.5,0],end = animdot2.get_center()+[0,-0.5,0],stroke_width=15, 
           max_stroke_width_to_length_ratio=100, max_tip_length_to_length_ratio=100, color = RED).scale(2).move_to(animdot2)
           )
        
        self.play(ReplacementTransform(i_arr4, i_arr5), run_time=0.25)
        self.play(MoveAlongPath(animdot2, aniline5))
        self.play(FadeOut(i_arr5),FadeOut(i_arr1))

        rampscope = SineScope(lambda x: ramp(x, on.get_value()), b, RIGHT, 1, GREEN, 1)

        animdot=Dot(radius=0).move_to(aniline1.get_start()) 
        i_arr1 = always_redraw(lambda:
           Arrow(start = animdot.get_center()-[0.5,0,0],end = animdot.get_center()+[0.5,0,0],stroke_width=15, 
           max_stroke_width_to_length_ratio=100, max_tip_length_to_length_ratio=100, color = BLUE).scale(2).move_to(animdot)
           )

        animdot2=Dot(radius=0).move_to(aniline2.get_start()) 
        i_arr2 = always_redraw(lambda:
           Arrow(start = animdot2.get_center()-[0.5,0,0],end = animdot2.get_center()+[0.5,0,0],stroke_width=15, 
           max_stroke_width_to_length_ratio=100, max_tip_length_to_length_ratio=100, color = RED).scale(2).move_to(animdot2)
           )

        self.play(FadeIn(i_arr1, i_arr2, animdot, animdot2, rampscope.group))
        self.play(MoveAlongPath(animdot, aniline1), run_time = 0.5)
        self.play(MoveAlongPath(animdot2, aniline2), run_time=0.25)

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
        rampline = Line(
            start=rampscope.ax.get_critical_point(LEFT), 
            end = rampscope.ax.get_critical_point(LEFT)+(rampscope.ax.get_critical_point(UR)-rampscope.ax.get_critical_point(LEFT))/4,
            color = GREEN
            )

        self.play(ReplacementTransform(i_arr3, i_arr4), run_time=0.1)
        self.play(MoveAlongPath(animdot2, aniline4),Create(rampline))

        i_arr5 = always_redraw(lambda:
           Arrow(start = animdot2.get_center()-[0,-0.5,0],end = animdot2.get_center()+[0,-0.5,0],stroke_width=15, 
           max_stroke_width_to_length_ratio=100, max_tip_length_to_length_ratio=100, color = RED).scale(2).move_to(animdot2)
           )
        
        self.play(ReplacementTransform(i_arr4, i_arr5), run_time=0.1)
        self.play(MoveAlongPath(animdot2, aniline5))
        self.play(FadeOut(i_arr5),FadeOut(i_arr1))
        self.wait(0.2)#41
        
        animdot=Dot(radius=0).move_to(aniline1.get_start()) 
        i_arr1 = always_redraw(lambda:
           Arrow(start = animdot.get_center()-[0.5,0,0],end = animdot.get_center()+[0.5,0,0],stroke_width=15, 
           max_stroke_width_to_length_ratio=100, max_tip_length_to_length_ratio=100, color = BLUE).scale(2).move_to(animdot)
           )

        animdot2=Dot(radius=0).move_to(aniline2.get_start()) 
        i_arr2 = always_redraw(lambda:
           Arrow(start = animdot2.get_center()-[0.5,0,0],end = animdot2.get_center()+[0.5,0,0],stroke_width=15, 
           max_stroke_width_to_length_ratio=100, max_tip_length_to_length_ratio=100, color = RED).scale(2).move_to(animdot2)
           )

        self.play(FadeIn(i_arr1, i_arr2, animdot, animdot2))
        self.play(MoveAlongPath(animdot, aniline1), run_time = 0.5)
        self.play(MoveAlongPath(animdot2, aniline2), run_time=0.25)

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
        rampline = Line(
            start=rampscope.ax.get_critical_point(LEFT), 
            end = rampscope.ax.get_critical_point(LEFT)+(rampscope.ax.get_critical_point(UR)-rampscope.ax.get_critical_point(LEFT))*0.5,
            color = GREEN
            )
        
        self.play(ReplacementTransform(i_arr3, i_arr4), run_time=0.1)
        self.play(MoveAlongPath(animdot2, aniline4),Create(rampline))
        i_arr5 = always_redraw(lambda:
           Arrow(start = animdot2.get_center()-[0,-0.5,0],end = animdot2.get_center()+[0,-0.5,0],stroke_width=15, 
           max_stroke_width_to_length_ratio=100, max_tip_length_to_length_ratio=100, color = RED).scale(2).move_to(animdot2)
           )
        
        self.play(ReplacementTransform(i_arr4, i_arr5), run_time=0.1)
        self.play(MoveAlongPath(animdot2, aniline5))
        self.play(FadeOut(i_arr5),FadeOut(i_arr1))
        self.wait(0.2)#41

        animdot=Dot(radius=0).move_to(aniline1.get_start()) 
        i_arr1 = always_redraw(lambda:
           Arrow(start = animdot.get_center()-[0.5,0,0],end = animdot.get_center()+[0.5,0,0],stroke_width=15, 
           max_stroke_width_to_length_ratio=100, max_tip_length_to_length_ratio=100, color = BLUE).scale(2).move_to(animdot)
           )

        animdot2=Dot(radius=0).move_to(aniline2.get_start()) 
        i_arr2 = always_redraw(lambda:
           Arrow(start = animdot2.get_center()-[0.5,0,0],end = animdot2.get_center()+[0.5,0,0],stroke_width=15, 
           max_stroke_width_to_length_ratio=100, max_tip_length_to_length_ratio=100, color = RED).scale(2).move_to(animdot2)
           )

        self.play(FadeIn(i_arr1, animdot, animdot2))
        self.play(MoveAlongPath(animdot, aniline1), run_time = 0.5)
        self.play(MoveAlongPath(animdot2, aniline2), run_time=0.25)

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
        rampline = Line(
            start=rampscope.ax.get_critical_point(LEFT), 
            end = rampscope.ax.get_critical_point(LEFT)+(rampscope.ax.get_critical_point(UR)-rampscope.ax.get_critical_point(LEFT))*0.75,
            color = GREEN
            )
        
        self.play(ReplacementTransform(i_arr3, i_arr4), run_time=0.1)
        self.play(MoveAlongPath(animdot2, aniline4),Create(rampline))
        i_arr5 = always_redraw(lambda:
           Arrow(start = animdot2.get_center()-[0,-0.5,0],end = animdot2.get_center()+[0,-0.5,0],stroke_width=15, 
           max_stroke_width_to_length_ratio=100, max_tip_length_to_length_ratio=100, color = RED).scale(2).move_to(animdot2)
           )
        
        self.play(ReplacementTransform(i_arr4, i_arr5), run_time=0.1)
        self.play(MoveAlongPath(animdot2, aniline5))
        self.play(FadeOut(i_arr5),FadeOut(i_arr1))
        self.wait(0.2)#41

        animdot=Dot(radius=0).move_to(aniline1.get_start()) 
        i_arr1 = always_redraw(lambda:
           Arrow(start = animdot.get_center()-[0.5,0,0],end = animdot.get_center()+[0.5,0,0],stroke_width=15, 
           max_stroke_width_to_length_ratio=100, max_tip_length_to_length_ratio=100, color = BLUE).scale(2).move_to(animdot)
           )

        animdot2=Dot(radius=0).move_to(aniline2.get_start()) 
        i_arr2 = always_redraw(lambda:
           Arrow(start = animdot2.get_center()-[0.5,0,0],end = animdot2.get_center()+[0.5,0,0],stroke_width=15, 
           max_stroke_width_to_length_ratio=100, max_tip_length_to_length_ratio=100, color = RED).scale(2).move_to(animdot2)
           )
        
        self.play(FadeIn(i_arr1, i_arr2, animdot, animdot2))
        self.play(MoveAlongPath(animdot, aniline1), run_time = 0.5)
        self.play(MoveAlongPath(animdot2, aniline2), run_time=0.25)

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
        rampline = Line(
            start=rampscope.ax.get_critical_point(LEFT), 
            end = rampscope.ax.get_critical_point(LEFT)+(rampscope.ax.get_critical_point(UR)-rampscope.ax.get_critical_point(LEFT)),
            color = GREEN
            )
        
        self.play(ReplacementTransform(i_arr3, i_arr4), run_time=0.1)
        self.play(MoveAlongPath(animdot2, aniline4),Create(rampline))
        i_arr5 = always_redraw(lambda:
           Arrow(start = animdot2.get_center()-[0,-0.5,0],end = animdot2.get_center()+[0,-0.5,0],stroke_width=15, 
           max_stroke_width_to_length_ratio=100, max_tip_length_to_length_ratio=100, color = RED).scale(2).move_to(animdot2)
           )
        
        self.play(ReplacementTransform(i_arr4, i_arr5), run_time=0.1)
        self.play(MoveAlongPath(animdot2, aniline5))
        self.play(FadeOut(i_arr5),FadeOut(i_arr1))
        self.wait(0.2)#41