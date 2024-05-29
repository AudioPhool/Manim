from cmath import pi
from manim import *
from scipy import signal

def comp(func):
    if func>0.6:
        result = 1
    else:
        result = -1
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
        self.x_range = [0,2*PI]
        self.y_range = [-1,1]

        #set up axis
        self.ax = NumberPlane(x_range=[0,4.29, 1], x_length=2.5, y_range=[-1,1, 1],stroke_width=2, y_length=1
                            ).next_to(self.next_to, self.direction, buff = self.buff).set_opacity(0).scale(self.scale)
                    
        #plot custom function from self.plot 
        #e.g "to_plot = lambda x: np.sin((3 * x) + (phi.get_value()))"
        self.sin = always_redraw(lambda: 
                    self.ax.plot(self.plot, 
                    x_range = [0,4*PI/3, 0.01],stroke_width=2,  
                    color = self.color,
                    use_smoothing = False)
                    )
        #put a dot at the end of the sine
        self.dot = always_redraw(lambda: 
                    Dot(point = self.sin.get_end()).scale(self.scale)
                    )
        #draw a box & a line
        self.b = always_redraw(lambda:RoundedRectangle(corner_radius=0.2,width=2.5,stroke_width=2, height = 1.25).move_to(self.ax).scale(self.scale))
        self.l = always_redraw(lambda:Line(start=self.b.get_critical_point(LEFT), end=self.b.get_critical_point(RIGHT),color = BLUE_C, stroke_width = 2, stroke_opacity = 1))
        #vgroup for animation purposes eg: FadeIn(scope1.group)
        self.group = VGroup(self.sin, self.dot, self.b, self.l)

class anim(Scene):
    def construct(self):
        template = TexTemplate()
        template.add_to_preamble(r"\usepackage[siunitx, RPvoltages, american, europeanresistors]{circuitikz} \ctikzset{multipoles/dipchip/width=1.5} \ctikzset{multipoles/dipchip/pin spacing=0.2}")
        
        phi = ValueTracker(0)
        freq = ValueTracker(3)

        #comparator Box
        saw_box = RoundedRectangle(
            corner_radius=0.2,
            width=3.5, height = 2.5,stroke_width=2,
            fill_color = BLUE_B,
            fill_opacity = (0.6)
            ).shift(LEFT*0)
        rect_l = Tex("Comparator").next_to(saw_box, UP, 0.25)
        

        line1 = Line(start = saw_box.get_critical_point(LEFT)+[0,0.675, 0]   , end = saw_box.get_critical_point(LEFT ) + [-0.75, 0.675, 0],stroke_width=2)
        line2 = Line(start = saw_box.get_critical_point(LEFT)+[0, -0.675, 0] , end = saw_box.get_critical_point(LEFT ) + [-0.75,-0.675, 0],stroke_width=2)
        line3 = Line(start = saw_box.get_critical_point(RIGHT)               , end = saw_box.get_critical_point(RIGHT) + [0.75,0, 0],stroke_width=2)

        ref = Tex("Input").next_to(line1.get_start(), RIGHT, buff=0.25)
        input = Tex("Ref").next_to(line2.get_start(), RIGHT, buff=0.25)
        out = Tex("Output").next_to(line3.get_start(), LEFT, buff=0.25)

        compbox = VGroup(saw_box, rect_l, ref, input, out)
        sinescope = SineScope(lambda x: np.sin(3*x + phi.get_value()), line1.get_end(), LEFT, 0, GREEN, 1)
        refscope = SineScope(lambda x: 0.6, line2.get_end(), LEFT, 0, ORANGE, 1)
        outscope = SineScope(lambda x: comp(np.sin(3*x+ phi.get_value())), line3.get_end(), RIGHT, 0, PURPLE, 1)
        sinescope2 = SineScope(lambda x: np.sin(3*x+ phi.get_value()), outscope.group, UP, 0.5, YELLOW_B, 1)
        refscope2 = SineScope(lambda x: 0.6, outscope.group, UP, 0.5, RED_B, 1)

        self.play(FadeIn(compbox))
        self.wait(0.2)#1
        self.play(LaggedStart(Create(line1), Create(sinescope.group), Create(line2), Create(refscope.group),lag_ratio=0.5))
        self.wait(0.2)#3
        self.play(LaggedStart(Create(line3), Create(outscope.group),lag_ratio=1))
        self.wait(0.2)#5
        self.play(LaggedStart(TransformFromCopy(sinescope.group, sinescope2.group),TransformFromCopy(refscope.group, refscope2.group),lag_ratio=0.2))
        self.wait(0.2)#7
        self.play(phi.animate.set_value(6*pi), run_time=10)
        self.wait(0.2)#9

        a = MathTex(
        r"""\draw (0,0) node[op amp, noinv input down, anchor=center] (OA){LM311} (OA.out)to[short]++(0.2,0)  (OA.+)to[short]++(-0.2,0)  (OA.-)to[short]++(-0.2,0);""",#0
        stroke_width=2,
        fill_opacity=0,
        stroke_opacity=1,
        tex_environment="circuitikz",
        tex_template=template,
        ).scale(0.975)

        self.play(FadeTransform(compbox, a))
        self.wait(0.2)#11