from cmath import pi
from manim import *
from scipy import signal

def comp(func):
    if func>0.7:
        result = 0
    else:
        result = -1
    return result

def comp2(func):
    if func>0.95:
        result = 0
    else:
        result = -1
    return result

def compd(func):
    if func>0.9:
        result = 1
    else:
        result = -1
    return result

def comp2d(func):
    if func>0.8:
        result = 0
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
        node[op amp, noinv input down, anchor=-] (OA){CA3130}
        (OA.-) to[short] ++(-0.5,0) to[short] (0.5, 2.25)
        (OA.out) to[short] ++(0.12, 0) coordinate(OAo) to[short] (3.5,2.25) 
        (OA.+) to[short] ++(-0.5,0);""",#0
        r"""\draw (0.5, 2.25) to[C] (3.5,2.25) ;""",#1
        r"""\draw (0.5, 2.25) to[short](0.5, 3.25) to[short] (1.25,3.25) node[njfet, rotate=-90, anchor=S](Q1){} (Q1.D)to[short](3.5,3.25) to[short] (3.5,2.25) (Q1.G)to[short] ++(5,0)to[diode]++(0,-1)node[ground]{};""",#1
        r"""\draw (0.5,0.025) to[short] (0.5,-0.5) node[ground]{} ;""",#2
        r"""\draw (-1.5,-0.5) node[ground]{} to[vsource](-1.5,1) to[R] (0.5, 1);""",#3
        r"""\draw (3.5,0.51) to[R] (5,0.51) node[op amp, noinv input down, anchor=-] (OA){LM311} (OA.+) node[vcc]{} (OA.out) to[short] ++(0,4.21) to[short] ++(-0.64,0) (OA.out) to[R] ++(1.5,0) node[ground]{};""",#0
        r"""\draw (5,0.51) to[short] ++(0,0.75) to[C] ++(2.4,0);""",#3
        stroke_width=2,
        fill_opacity=0,
        stroke_opacity=1,
        tex_environment="circuitikz",
        tex_template=template,
        ).scale(0.8).shift(RIGHT*0.15)
        v5 = Tex("5v").next_to(a[3],LEFT).shift(RIGHT*5.25+UP*0.25)
        adj = 2.5
        capscope = SineScope(lambda x: ((signal.sawtooth(adj*x + phi.get_value(), 0.8)*0.5)+0.5), a[1], RIGHT, 0.2, GREEN, 0.7)
        outscope = SineScope(lambda x: comp(signal.sawtooth(adj*x + phi.get_value()+0.2)), (a[4].get_center()+[1.2,0.75,0]), RIGHT, 7.7, ORANGE, 0.7)

        v1 = always_redraw(lambda: DecimalNumber(((signal.sawtooth(adj*4.29 + phi.get_value())*0.1)+0.9)*5, 1).next_to(capscope.ax, UP, buff = 0.25))
        v1l = always_redraw(lambda: Tex("V").scale(0.8).next_to(v1,RIGHT,0.05))

        v2 = always_redraw(lambda: DecimalNumber(comp2d((signal.sawtooth(adj*4.29 + phi.get_value()-0.1)*0.1)+0.9)*15, 1).next_to(outscope.ax, UP, buff = 0.25))
        v2l = always_redraw(lambda: Tex("V").scale(0.8).next_to(v2,RIGHT,0.05))

        self.play(FadeIn(a,capscope.group,outscope.group, v5, v1,v1l,v2,v2l))
        self.wait(0.2)#5
        self.play(phi.animate.set_value(7.9*pi), run_time=5, rate_func=linear)
        self.wait(0.2)#7

