from manim import *
import math
draw = ValueTracker(4*PI/3)
phi = ValueTracker(-8*PI)
prev = 0
result = 0
peak = 0
t = 0
prev1 = 0
result1 = 0
peak1 = 0
t1 = 0
resultd1 = 0

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
        result = peak*math.exp(-t/0.55)
        t = t + 0.0165 
        prev = result
    return result

def rect(func):
    if(func >= 0):
        return func
    else:
        return 0

def charge1(func):
    global prev1
    global result1
    global peak1
    global t1
    if func>prev1:
        result1 = func
        t1 = 0
        prev1 = result1
        peak1 = func
    else:
        result1 = 1
        t1 = t1 + 0.0165 
        prev1 = result1
    return result1
def sin():
    sin = np.sin((3 * draw.get_value()) + (phi.get_value()))
    return sin

def rsin():
    sin = abs(np.sin((3 * draw.get_value()) + (phi.get_value())))
    return sin

def chsin():
    sin = charge1(np.sin((3 * draw.get_value()) + (phi.get_value())))
    return sin

class SineScope():
    def __init__(self,to_plot,next_to, direction, buff, color):
        self.next_to = next_to
        self.direction = direction 
        self.buff = buff
        self.plot = to_plot
        self.color = color
        self.x_range = [0,4.29]
        self.y_range = [-1,1]

        self.ax = always_redraw(lambda:NumberPlane(x_range=[0,4.29, 1], x_length=2.5, y_range=[-1,1, 1], y_length=1)
                    .next_to(self.next_to, self.direction, buff = self.buff).set_opacity(0)
                    )
        self.sin = always_redraw(lambda: 
                    self.ax.plot(self.plot, 
                    x_range = [0,draw.get_value()], 
                    color = self.color,
                    use_smoothing = False)
                    )
        self.dot = always_redraw(lambda: 
                    Dot(point = self.sin.get_end())
                    )
        self.b = always_redraw(lambda:RoundedRectangle(corner_radius=0.2,width=2.5, height = 1.25).move_to(self.ax))
        self.l = always_redraw(lambda:Line(start=self.b.get_critical_point(LEFT), end=self.b.get_critical_point(RIGHT),color = BLUE_C, stroke_width = 2, stroke_opacity = 1))
        self.group = VGroup(self.sin, self.dot, self.b, self.l)


class anim(Scene):
    def construct(self):
        template = TexTemplate()
        template.add_to_preamble(r"\usepackage[siunitx, RPvoltages, american, europeanresistors]{circuitikz}")
        
        a = MathTex(
        r"""\draw (0,-3) to[sV, v=$$, voltage shift=1]  (0,0) (0,-3) to[short, -o] (3,-3);""",
        r"""\draw (0,0)  to[diode, -o]  (3,0); """,
        #r"""\draw (3,0)  to[R, v^ = $R_{Load}$]  (3,-3); """,
        r"""\draw (0,-3) node[ground]{}; """,
        stroke_width=2,
        fill_opacity=0,
        stroke_opacity=1,
        tex_environment="circuitikz",
        tex_template=template,
        ).scale(0.75)

            

        scope1 = SineScope(lambda x: np.sin((3 * x) + (phi.get_value())), a[0], LEFT, 0.5, RED)
        scope2 = SineScope(lambda x: rect(np.sin((3 * x) + (phi.get_value()))), a, RIGHT, 0.5, YELLOW)
        r_sin = always_redraw(lambda: 
                    scope2.ax.plot(lambda x: 0.95*np.sin((3 * x) + (phi.get_value())), 
                    x_range = [0,draw.get_value()], 
                    color = RED,
                    use_smoothing = False)
                    ).set_z_index(-1)
        self.add(a, scope1.group, scope2.group, r_sin)
        self.wait(0.2)
        self.play(phi.animate.set_value(-4*PI/3), run_time = 6, rate_func = linear)
        self.wait(0.2)

        b = MathTex(
        r"""\draw (0,-3) to[sV, v=$$, voltage shift=1]  (0,0)  (0,-3) to[short, -o] (4.5,-3);""",
        r"""\draw (0,0)  to[diode]  (3,0) to[short, -o] (4.5,0); """,
        #r"""\draw (4.5,0)  to[R, v^ = $R_{L}$]  (4.5,-3); """,
        r"""\draw (3,0)  to[C, o-o]  (3,-3); """,
        r"""\draw (0,-3) node[ground]{}; """,
        stroke_width=2,
        fill_opacity=0,
        stroke_opacity=1,
        tex_environment="circuitikz",
        tex_template=template,
        ).scale(0.75)

        scope12 = SineScope(lambda x: np.sin((3 * x) + (phi.get_value())), b[0], LEFT, 0.5, YELLOW)
        scope22 = SineScope(lambda x: charge1(np.sin((3 * x) + (phi.get_value()))),  b, RIGHT, 0.5, BLUE)
        r_sin2 = always_redraw(lambda: 
                    scope22.ax.plot(lambda x: 0.95*np.sin((3 * x) + (phi.get_value())), 
                    x_range = [0,draw.get_value()], 
                    color = RED,
                    use_smoothing = False)
                    ).set_z_index(-1)
        self.play(FadeTransform(a,b),FadeTransform(scope2.group, scope22.group), FadeTransform(scope1.group, scope12.group), FadeTransform(r_sin, r_sin2))
        self.wait(0.2)
        self.play(phi.animate.set_value(4*PI), run_time = 6, rate_func = linear)
        self.wait(0.2)

        c = MathTex(
        r"""\draw (0,-3) to[sV, v=$$, voltage shift=1]  (0,0)  (0,-3) to[short, -o] (4.5,-3);""",
        r"""\draw (0,0)  to[diode]  (3,0) to[short, -o] (4.5,0); """,
        r"""\draw (4.5,0)  to[R, v^ = $R_{L}$]  (4.5,-3); """,
        r"""\draw (3,0)  to[C, o-o]  (3,-3); """,
        r"""\draw (0,-3) node[ground]{}; """,
        stroke_width=2,
        fill_opacity=0,
        stroke_opacity=1,
        tex_environment="circuitikz",
        tex_template=template,
        ).scale(0.75)

        scope13 = SineScope(lambda x: np.sin((3 * x) + (phi.get_value())), c[0], LEFT, 0.5, YELLOW)
        scope23 = SineScope(lambda x: ripple(np.sin((3 * x) + (phi.get_value()))), c[2], RIGHT, 0.5, BLUE)
        r_sin3 = always_redraw(lambda: 
                    scope23.ax.plot(lambda x: 0.95*np.sin((3 * x) + (phi.get_value())), 
                    x_range = [0,draw.get_value()], 
                    color = RED,
                    use_smoothing = False)
                    ).set_z_index(-1)

        self.play(FadeTransform(b,c),FadeTransform(scope22.group, scope23.group),FadeTransform(scope12.group, scope13.group),FadeTransform(r_sin2, r_sin3))
        self.wait(0.2)
        self.play(phi.animate.set_value(2*4*PI), run_time = 6, rate_func = linear)
        self.wait(0.2)