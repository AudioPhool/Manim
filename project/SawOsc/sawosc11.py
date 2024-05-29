import math
from cmath import pi
from manim import *
from scipy import signal

class anim(Scene):
    def construct(self):
        template = TexTemplate()
        template.add_to_preamble(r"\usepackage[siunitx, RPvoltages, american, europeanresistors]{circuitikz} \ctikzset{multipoles/dipchip/width=1.5} \ctikzset{multipoles/dipchip/pin spacing=0.2}")
        
        t = ValueTracker(0.000000001)
        phi2 = ValueTracker(0)

        a1 = Axes(
            x_range = [0,5.5,1], 
            x_length = 6, 
            y_range = [0,5.5,1],
            y_length = 6, 
            tips=True,
            ).add_coordinates()
        labels = a1.get_axis_labels(x_label='RC', y_label='V').set_color(RED)

        parab = always_redraw(lambda: a1.plot(lambda x : 5*math.exp(-x/(1)), x_range = [0,t.get_value()], color = YELLOW)) #(2x+1)(x+1)
        dot = always_redraw(lambda: Dot(fill_color = WHITE, fill_opacity = 0.8).scale(1).move_to(parab.get_end()))
        lab = Tex('V = ').shift(UP)
        v = always_redraw(lambda: DecimalNumber(5*math.exp(-t.get_value()/(1))).next_to(lab,RIGHT))
        self.add(a1, parab, dot, labels, lab, v)
        self.wait(0.2)
        self.play(t.animate.set_value(1), run_time = 2)
        self.wait(0.2)
        self.play(t.animate.set_value(5), run_time = 2)
        self.wait(0.2)