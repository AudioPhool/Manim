from manim import *

class SineScope(Mobject):
    #draws an oscilloscope and can plot a function
    #e.g. scope1 = SineScope(lambda x: np.sin((3 * x) + (phi.get_value())), a[3], DL, 0.5,YELLOW)
    #plots a yellow sine wave using numpy, with a frequency of x rads and phi phase, down left of mobject a[3] with a buffer of 0.5
    def __init__(self,to_plot,next_to, direction, buff, color):
        #initialises the scope
        self.next_to = next_to
        self.direction = direction 
        self.buff = buff
        self.plot = to_plot
        self.color = color
        self.x_range = [0,4.29]
        self.y_range = [-1,1]

        #set up axis
        self.ax = always_redraw(lambda:NumberPlane(x_range=[0,4.29, 0.1], x_length=2.5, y_range=[-1,1, 1], y_length=1)
                    .next_to(self.next_to, self.direction, buff = self.buff).set_opacity(0)
                    )
        #plot custom function from self.plot 
        #e.g "to_plot = lambda x: np.sin((3 * x) + (phi.get_value()))"
        self.sin = always_redraw(lambda: 
                    self.ax.plot(self.plot, 
                    x_range = [0,4*PI/3], 
                    color = self.color,
                    use_smoothing = False)
                    )
        #put a dot at the end of the sine
        self.dot = always_redraw(lambda: 
                    Dot(point = self.sin.get_end())
                    )
        #draw a box & a line
        self.b = always_redraw(lambda:RoundedRectangle(corner_radius=0.2,width=2.5, height = 1.25).move_to(self.ax))
        self.l = always_redraw(lambda:Line(start=self.b.get_critical_point(LEFT), end=self.b.get_critical_point(RIGHT),color = BLUE_C, stroke_width = 2, stroke_opacity = 1))
        #vgroup for animation purposes eg: FadeIn(scope1.group)
        self.group = VGroup(self.sin, self.dot, self.b, self.l)

class anim(Scene):
    def construct(self):
        template = TexTemplate()
        template.add_to_preamble(r"\usepackage[siunitx, RPvoltages, american, europeanresistors]{circuitikz}")

        freq = ValueTracker(1)
        keyb = ImageMobject("project/MIDI/key.jpg").shift(LEFT*0+UP*0).scale(1)
        hl1 = Rectangle(color=RED,fill_color = RED_A, fill_opacity = 0.85, height=1.75, width=0.4).shift(LEFT*4.25+DOWN*1.05)

        volt = always_redraw(lambda: DecimalNumber(number=freq.get_value()).scale(2).shift(RIGHT*3.5+DOWN*1))
        labv = MathTex('v').scale(2).next_to(volt, RIGHT, buff=0.2)

        scope1 = SineScope(lambda x: np.sin((3 * x * freq.get_value())), volt, UP, 1.25,YELLOW)

        self.play(FadeIn(keyb))
        self.wait() 
        self.play(keyb.animate.shift(LEFT*2).scale(0.75),FadeIn(volt, labv), FadeIn(scope1.group),run_time=1)
        self.wait()
        self.play(FadeIn(hl1))
        self.wait()
        self.play(freq.animate.set_value(2), hl1.animate.shift(RIGHT*3.15))

