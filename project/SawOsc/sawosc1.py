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
        self.sin = always_redraw(lambda: 
                    self.ax.plot(self.plot, 
                    x_range = [0,4*PI/3, 0.01], 
                    color = self.color,
                    use_smoothing = False)
                    )
        #put a dot at the end of the sine
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
        
        phi = ValueTracker(0)
        freq = ValueTracker(3)

        # Sawtooth Core Box
        saw_box = RoundedRectangle(
            corner_radius=0.2,
            width=3.5, height = 2.5,
            fill_color = PURPLE_B,
            fill_opacity = (0.6)
            ).shift(LEFT*3.5)
        rect_l = VGroup(Tex("Sawtooth"), Tex("Core")).arrange(DOWN).move_to(saw_box).shift(UP*0.5)
        ax0 = Axes(x_range=[0,6.28,0.1], y_range=[-1,1,1], x_length = 1, y_length = 0.5, tips = False,            
        ).move_to(saw_box.get_critical_point(DOWN)).shift(UP*0.5+LEFT*0.1).scale(0.8)
        rect_l2 = ax0.plot(lambda x: signal.sawtooth(2*x), x_range=[0,2*PI], color = WHITE, use_smoothing=False)
        sawlab = Tex("Saw").scale(0.6).next_to(ax0.get_critical_point(UP),UP,buff=0.15).shift(RIGHT*0.1)
        saw_core = VGroup(saw_box, rect_l, rect_l2, sawlab)

        # Waveshaper Box
        ws_box = RoundedRectangle(
            corner_radius=0.2,
            width=6.5, height = 2.5,
            fill_color = RED_B,
            fill_opacity = (0.7)
            ).shift(RIGHT*2.25)
        ws_l = Tex("Waveshaper").move_to(ws_box).shift(UP*0.5)

        ax1 = Axes(x_range=[0,6.28,3.14], y_range=[-1,1,1], x_length = 1, y_length = 0.5, tips = False,            
        ).move_to(ws_box.get_critical_point(DL)).shift(UP*0.5+RIGHT*0.9).scale(0.85)
        ws_l2 = ax1.plot(lambda x: np.sin(2*x), x_range=[0,2*PI], color = WHITE)
        sinlab = Tex("Sine").scale(0.6).next_to(ax1.get_critical_point(UP),UP,buff=0.15).shift(RIGHT*0.05)
        
        ax2 = Axes(x_range=[0,6.28,0.1], y_range=[-1,1,1], x_length = 1, y_length = 0.5, tips = False,            
        ).move_to(ws_box.get_critical_point(DOWN)).shift(UP*0.5+LEFT*0.1).scale(0.85)
        ws_l3 = ax2.plot(lambda x: signal.square(2*x), x_range=[0,2*PI], color = WHITE, use_smoothing=False)
        sqrlab = Tex("Square").scale(0.6).next_to(ax2.get_critical_point(UP),UP,buff=0.1).shift(RIGHT*0.05)

        ax3 = Axes(x_range=[0,6.28,0.1], y_range=[-1,1,1], x_length = 1, y_length = 0.5, tips = False,            
        ).move_to(ws_box.get_critical_point(DR)).shift(UP*0.5+LEFT*1.1).scale(0.85)
        ws_l4 = ax3.plot(lambda x: signal.sawtooth(2*x, 0.5), x_range=[0,2*PI], color = WHITE, use_smoothing=False)
        trilab = Tex("Triangle").scale(0.6).next_to(ax3.get_critical_point(UP),UP,buff=0.1)
        waveshaper = VGroup(ws_box, ws_l, ws_l2, ws_l3, ws_l4, sinlab, sqrlab, trilab).shift(RIGHT*0.1)

        #Connecting Line
        line1 = Line(
            start=saw_box.get_critical_point(RIGHT),
            end=(ws_box.get_critical_point(LEFT)),
            stroke_width=4
        )
        line1end = line1.get_end()

        self.play(FadeIn(saw_core))
        self.wait(0.2)#1
        self.play(LaggedStart(Create(line1), FadeIn(waveshaper), lag_ratio=0.5))
        self.wait(0.2)#3
        self.play(waveshaper.animate.shift(UP*1), saw_core.animate.shift(UP*1), line1.animate.shift(UP*1))
        self.wait(0.2)#5

        sinedown = sinlab.get_critical_point(DOWN)
        sqrdown = sqrlab.get_critical_point(DOWN)
        tridown = trilab.get_critical_point(DOWN)
        wsboxdown = ws_box.get_critical_point(DOWN)

        scopescale = 0.8
        sawscope = SineScope(lambda x: signal.sawtooth(freq.get_value()*x + (phi.get_value())), saw_box.get_critical_point(DOWN), DOWN, 0.75, BLUE_C, scopescale)
        sinscope = SineScope(lambda x: np.sin(freq.get_value()*x + (phi.get_value()-PI)), [sinedown[0],wsboxdown[1],0], DOWN, 0.75, YELLOW_C, scopescale)
        sqrscope = SineScope(lambda x: signal.square(freq.get_value()*x + (phi.get_value()-PI)), [sqrdown[0],wsboxdown[1],0], DOWN, 0.75, PURPLE_C, scopescale)
        triscope = SineScope(lambda x: signal.sawtooth(freq.get_value()*x + phi.get_value(), 0.5), [tridown[0],wsboxdown[1],0], DOWN, 0.75, GREEN_C, scopescale)
        
        line2 = always_redraw(lambda: Line(
            start=saw_box.get_critical_point(DOWN),
            end=(sawscope.group.get_critical_point(UP)),
            stroke_width=4
        ))
        line3 = always_redraw(lambda: Line(
            start=[sinlab.get_critical_point(DOWN)[0],ws_box.get_critical_point(DOWN)[1],0],
            end=sinscope.group.get_critical_point(UP),
            stroke_width=4
        ))
        line4 = always_redraw(lambda: Line(
            start=[sqrlab.get_critical_point(DOWN)[0],ws_box.get_critical_point(DOWN)[1],0],
            end=sqrscope.group.get_critical_point(UP),
            stroke_width=4
        ))
        line5 = always_redraw(lambda: Line(
            start=[trilab.get_critical_point(DOWN)[0],ws_box.get_critical_point(DOWN)[1],0],
            end=triscope.group.get_critical_point(UP),
            stroke_width=4
        ))
        

        self.play(LaggedStart(Create(line2), Create(sawscope.group), Create(line3), Create(sinscope.group), Create(line4), 
                              Create(sqrscope.group), Create(line5), Create(triscope.group), lag_ratio = 0.2))
        self.wait(0.2)#7
        self.play(phi.animate.set_value(4*pi), run_time=4, rate_func = linear)
        self.play(phi.animate.set_value(8*pi),freq.animate.set_value(6), run_time=4, rate_func = linear)
        self.play(phi.animate.set_value(16*pi),freq.animate.set_value(3), run_time=4, rate_func = linear)
        self.wait(0.2)#13
        self.play(waveshaper.animate.shift(RIGHT*1), saw_core.animate.shift(RIGHT*1), line1.animate.shift(RIGHT*1), 
                  sawscope.ax.animate.shift(RIGHT*1),sinscope.ax.animate.shift(RIGHT*1),sqrscope.ax.animate.shift(RIGHT*1),triscope.ax.animate.shift(RIGHT*1))
        self.wait(0.2)#15

        # keyboard
        keyboard = ImageMobject("media/images/mkey.jpg").rotate(-90*DEGREES).scale(0.25).next_to(saw_box, LEFT, 1)
        outline = Rectangle(
        width=1.5, height = 2.5,
        fill_opacity = (0)
        ).move_to(keyboard)

        line6 = always_redraw(lambda: Line(
            start=outline.get_critical_point(RIGHT),
            end=saw_box.get_critical_point(LEFT),
            stroke_width=4
        ))

        cv = always_redraw(lambda: DecimalNumber(
            freq.get_value()/3,include_sign=False
        ).scale(0.7).next_to(outline.get_critical_point(RIGHT), UR, 0.1))
        cv_l = Tex("v").next_to(cv, RIGHT, 0)

        note1 = Rectangle(
        width=0.57, height = 0.09,
        fill_color=ORANGE,
        color=ORANGE,
        fill_opacity = (0.4),
        stroke_width=1
        ).move_to(keyboard).shift(LEFT*0.35+UP*0.3)

        note2 = Rectangle(
        width=0.57, height = 0.09,
        fill_color=ORANGE,
        color=ORANGE,
        fill_opacity = (0.4),
        stroke_width=1
        ).move_to(keyboard).shift(LEFT*0.35+DOWN*0.74)

        self.play(LaggedStart(FadeIn(keyboard, outline), Create(line6), FadeIn(cv, cv_l, note1), lag_ratio = 0.2))
        self.wait(0.2)#17
        self.play(phi.animate.set_value(20*pi), run_time=4, rate_func = linear)
        self.play(FadeOut(note1), FadeIn(note2), phi.animate.set_value(24*pi),freq.animate.set_value(6), run_time=4, rate_func = linear)
        self.play(phi.animate.set_value(28*pi), run_time=4, rate_func = linear)
        self.play(FadeOut(note2), FadeIn(note1), phi.animate.set_value(36*pi),freq.animate.set_value(3), run_time=4, rate_func = linear)
        self.wait(0.2)#23