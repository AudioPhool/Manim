from manim import *
import math
cap = ValueTracker(0.5)
res = ValueTracker(1)
prev = 0
result = 0
peak = 0
t = 0
def ripple(func):
    global prev
    global result
    global peak
    global t
    if func>prev:
        result = func
        t = 0
        prev = result
        peak = func
    else:
        result = peak*math.exp(-t/(cap.get_value()*res.get_value()))
        t = t + 0.0165/2 
        prev = result
    return result

class anim(Scene):
    def construct(self):
        template = TexTemplate()
        template.add_to_preamble(r"\usepackage[siunitx, RPvoltages, american, europeanresistors]{circuitikz}")
        

        a = MathTex(
        r"""\draw (0,-3) to[sV, v=$$, voltage shift=1]  (0,0)  (0,-3) to[short, -o] (5,-3);""",
        r"""\draw (0,0)  to[diode]  (3,0) to[short, -o] (5,0); """,
        r"""\draw (5,0)  to[R, v^ = $R_{L}$]  (5,-3); """,
        r"""\draw (2.75,0)  to[C, o-o]  (2.75,-3); """,
        r"""\draw (0,-3) node[ground]{}; """,
        stroke_width=2,
        fill_opacity=0,
        stroke_opacity=1,
        tex_environment="circuitikz",
        tex_template=template,
        ).scale(0.65).shift(RIGHT*3+DOWN*1.5)

        b = MathTex(
        r"""\draw (0,-3) to[sV, v=$$, voltage shift=1]  (0,0)  (0,-3) to[short, -o] (5,-3);""",
        r"""\draw (0,0)  to[diode]  (3,0) to[short, -o] (5,0); """,
        r"""\draw (5,0)  to[R, v^ = $$]  (5,-3); """,
        r"""\draw (2.75,0)  to[C, o-o]  (2.75,-3); """,
        r"""\draw (0,-3) node[ground]{}; """,
        stroke_width=2,
        fill_opacity=0,
        stroke_opacity=1,
        tex_environment="circuitikz",
        tex_template=template,
        ).scale(0.65).shift(RIGHT*3+DOWN*1.5)

        eq1 = MathTex("V_{Cap} = V_{pk}*e^{-t/{RC}}", color = PURPLE_B).scale(1.25).shift(RIGHT*3+UP*3)

        ax1 = Axes(x_range = [0,2*PI, PI/2], y_range = [-1,1], x_length = 6, y_length = 4.5,tips = False).shift(4*LEFT)
        capacitor = always_redraw(lambda: 
                ax1.plot(lambda x:ripple(np.sin(3 * x)),
                x_range = [0,2*PI,0.0165],
                color = BLUE,
                use_smoothing = True)
            )
        sine = always_redraw(lambda: 
                ax1.plot(lambda x:(0.99*np.sin(3 * x)),
                x_range = [0,2*PI],
                color = YELLOW,
                use_smoothing = True).set_z_index(-1)
            )
        scalea = 0.6
        clab1 = always_redraw(lambda:MathTex("C=").scale(scalea).next_to(a[3], RIGHT,buff=0.1))
        c = always_redraw(lambda:DecimalNumber(
                 2*cap.get_value(), 
                 show_ellipsis=False, 
                 num_decimal_places=1,
                 include_sign = False
                 ).scale(scalea).next_to(clab1, DOWN,buff=0.1))
        clab2 = always_redraw(lambda:MathTex("uF").scale(scalea).next_to(c, RIGHT,buff=0.1))

        rlab1 = always_redraw(lambda:MathTex("R=").scale(scalea).next_to(b[2], RIGHT,buff=0.1))
        r = always_redraw(lambda:DecimalNumber(
                 1000*res.get_value(), 
                 show_ellipsis=False, 
                 num_decimal_places=1,
                 include_sign = False
                 ).scale(scalea).next_to(rlab1, DOWN,buff=0.1))
        rlab2 = always_redraw(lambda:MathTex("\Omega").scale(scalea).next_to(r, RIGHT,buff=0.1))

        self.add(ax1,capacitor,sine,a,eq1,c,clab1,clab2)
        self.wait(0.2)
        self.play(Indicate(eq1))
        self.wait(0.2)
        self.play(cap.animate.set_value(2), run_time = 3)
        self.wait(0.2)
        self.play(cap.animate.set_value(4), run_time = 2)
        self.wait(0.2)
        self.play(cap.animate.set_value(1), run_time = 3)
        self.wait(0.2)

        
        #eq1   = MathTex(r"V_{cap} = V_{pk}*e^{-t/{RC}}", color = PURPLE_B).scale(1.25).shift(RIGHT*3+UP*3)
        eq2   = MathTex(r"V_{min} = V_{pk}*e^{-T/{RC}}", color = PURPLE_B).scale(1.25).shift(RIGHT*3+UP*1)
        eq3   = MathTex(r"V_{min} = V_{pk}*(1-\frac{T}{RC})", color = PURPLE_B).scale(1.25).shift(RIGHT*3+UP*1)
        eq4   = MathTex(r"V_{rip} = V_{Max}-V_{Min}", color = PURPLE_B).scale(1.25).shift(RIGHT*3+UP*1.3)
        eq4_2 = MathTex(r"V_{rip} = V_{pk}-V_{pk}*(1-\frac{T}{RC})", color = PURPLE_B).scale(1.25).shift(RIGHT*3+UP*1)
        #eq5   = MathTex(r"V_{Min} = V_{pk}*e^{-T/{RC}}", color = PURPLE_B).scale(1.25).shift(RIGHT*3+UP*1.3)
        eq5   = MathTex(r"V_{rip} = V_{pk}-V_{pk}-\frac{V_{P}T}{RC}", color = PURPLE_B).scale(1.25).shift(RIGHT*3+UP*1)
        eq6 = MathTex(r"V_{rip} = \frac{V_{P}}{fRC}", color = PURPLE_B).scale(1.25).shift(RIGHT*4+UP*1)
        eq7   = MathTex(r"V_{rip} = \frac{V_{dc}}{R*fC}", color = PURPLE_B).scale(1.25).shift(RIGHT*3+UP*1)
        eq8   = MathTex(r"V_{Ripple} = \frac{I_{dc}}{fC}", color = PURPLE_B ).scale(1.25).shift(RIGHT*3+UP*1)

        ex1 = MathTex(r"Let\, 'T' = time\,\, from\,\, max\,\, to\,\,    min", color = RED).scale(0.7).shift(RIGHT*3+UP*2) 
        ex2 = MathTex(r"Assume\, RC >> T", color = RED).scale(0.7).shift(RIGHT*3+UP*2)
        ex3 = MathTex(r"", color = RED).scale(0.7).shift(RIGHT*3+UP*2)
        ex3_2 = MathTex(r"V_{max} = V_{pk}", color = RED).scale(0.7).shift(RIGHT*3+UP*2)
        ex4 = MathTex(r"", color = RED).scale(0.7).shift(RIGHT*3+UP*2)
        ex5 = MathTex(r"f = \frac{1}{T} or T = \frac{1}{f} ", color = RED).scale(0.7).shift(RIGHT*3+UP*2)
        ex6 = MathTex(r"V_{pk} \approx V_{dc} \,\, (V_{dc} = V_{pk}-0.5V_{rip})", color = RED).scale(0.7).shift(RIGHT*3+UP*2)
        ex7 = MathTex(r"\frac{V_{dc}}{R}=I_{dc}", color = RED).scale(0.7).shift(RIGHT*3+UP*2)

        self.add(eq1, a)
        self.play(ReplacementTransform(eq1.copy(),eq2),FadeIn(ex1))
        self.wait(0.2)
        self.play(eq2.animate.shift(UP*2), FadeOut(eq1), FadeOut(ex1))
        self.wait(0.2)

        self.play(ReplacementTransform(eq2.copy(),eq3), FadeIn(ex2))
        self.wait(0.2)
        self.play(eq3.animate.shift(UP*2), FadeOut(eq2), FadeOut(ex2))
        self.wait(0.2)

        self.play(ReplacementTransform(eq3.copy(),eq4), FadeIn(ex3))
        self.wait(0.2)
        self.play(eq4.animate.shift(UP*2), FadeOut(eq3), FadeOut(ex3))
        self.wait(0.2)

        self.play(ReplacementTransform(eq4.copy(),eq4_2), FadeIn(ex3_2))
        self.wait(0.2)
        self.play(eq4_2.animate.shift(UP*2), FadeOut(eq4), FadeOut(ex3_2))
        self.wait(0.2)

        self.play(ReplacementTransform(eq4_2.copy(),eq5), FadeIn(ex4))
        self.wait(0.2)
        self.play(eq5.animate.shift(UP*2), FadeOut(eq4_2), FadeOut(ex4))
        self.wait(0.2)

        self.play(ReplacementTransform(eq5.copy(),eq6), FadeIn(ex5))
        self.wait(0.2)
        self.play(eq6.animate.shift(UP*2+LEFT*1), FadeOut(eq5), FadeOut(ex5))
        self.wait(0.2)

        self.play(ReplacementTransform(eq6.copy(),eq7), FadeIn(ex6))
        self.wait(0.2)
        self.play(eq7.animate.shift(UP*2), FadeOut(eq6), FadeOut(ex6))
        self.wait(0.2)

        self.play(ReplacementTransform(eq7.copy(),eq8), FadeIn(ex7))
        self.wait(0.2)
        self.play(eq8.animate.shift(UP*2), FadeOut(eq7), FadeOut(ex7))
        self.wait(0.2)

        self.play(eq8.animate.shift(DOWN*1.25).scale(1.5), ReplacementTransform(a,b), FadeIn(r,rlab1,rlab2))
        self.wait(0.2)

        self.wait(0.2)
        self.play(res.animate.set_value(0.5), run_time = 3)
        self.wait(0.2)
        self.play(cap.animate.set_value(4), run_time = 2)
        self.wait(0.2)
        self.play(res.animate.set_value(0.25), run_time = 3)
        self.wait(0.2)
        self.play(cap.animate.set_value(8), run_time = 2)
        self.wait(0.2)
        self.play(res.animate.set_value(0.1), cap.animate.set_value(12), run_time = 3)
        self.wait(0.2)