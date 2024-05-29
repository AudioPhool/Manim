from manim import*
import math

prev = 0
result = 0
peak = 0
t = 0

phi = ValueTracker(0)
vr1 = ValueTracker(15.6)
vr2 = ValueTracker(15.6)

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
        result = peak*math.exp(-t/1.25)
        t = t + 0.0165 
        prev = result
    return result

def v1(func):
    if 0<func<15.6:
        result = func - 0.6
    elif func <= 0:
        result = 0
    else :
        result = 15
    return result

class SineScope():
    #draws an oscilloscope and can plot a function
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
        self.ax = always_redraw(lambda:NumberPlane(x_range=[0,4.29, 1], x_length=2.5, y_range=[-1,1, 1], y_length=1)
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

        a = MathTex(
        r"""\draw (-0.5,0) to[short] ++(1.5,0)
        node[op amp, noinv input up, anchor=+] (OA){\texttt{}}
        (OA.-) to[short] ++(-0.5,0) to[short] (0.5, -2) to[short] (5,-2)
        (OA.out) to[short] ++(0.12, 0) coordinate(OAo) to[short] (3.5,1.15)
        (OA.+) to[short] ++(-0.5,0);""",
        r"""\draw (-0.5,-4) to[zzD, -o] (-0.5, 0);""",
        r"""\draw (-0.5, 0) to[R, l=$R_3$, -o] (-0.5,2);""",
        r"""\draw (-0.5,2) to [short, -o] (-1.5,2) node[above]{$v_{in}$};""",
        r"""\draw (-0.5,-4) node[ground]{} ;""",
        r"""\draw (-0.5,2) to[short] (2.5,2) to[Tnpn, invert] (4.5,2) to[short] (5,2);""",
        r"""\draw (5,2) to[R,l_=$R_1$, o-] (5,-2);""",#6
        r"""\draw (5,-2) to[R,l_=$R_2$, o-] (5,-4) node[ground]{};""",#7
        r"""\draw (5,2) to [short, -o] (6,2) node[above]{$v_{out}$};""",#8
        stroke_width=2,
        fill_opacity=0,
        stroke_opacity=1,
        tex_environment="circuitikz",
        tex_template=template,
        ).scale(0.7)

        b = MathTex(
        r"""\draw (-0.5,0) to[short] (1,0);""",#0
        r"""\draw (1,0)node[op amp, noinv input up, anchor=+] (OA){\texttt{}}
        (OA.-) to[short] ++(-0.5,0) to[short] (0.5, -2) to[short] (5,-2)
        (OA.out) to[short] ++(0.12, 0) coordinate(OAo) to[short] (3.5,1.15)
        (OA.+) to[short] ++(-0.5,0);""",#1
        r"""\draw (-0.5,-4) to[zzD,v^>= $$, -o] (-0.5, 0);""",#2
        r"""\draw (-0.5, 0) to[R, v^>= $$, -o] (-0.5,2);""",#3
        r"""\draw (-0.5,2) to [short, -o] (-1.5,2) node[above]{$v_{in}$};""",#4
        r"""\draw (-0.5,-4) node[ground]{} (-0.5,2) to[short] (2.5,2) ;""",#5
        r"""\draw (2.5,2) to[Tnpn, invert] (4.5,2) to[short] (5,2);""",#6
        r"""\draw (5,2) to[R,l_={$R_1$}, o-] (5,-2);""",#7
        r"""\draw (5,-2) to[R,l_={$R_2$}, o-] (5,-4) node[ground]{};""",#8
        r"""\draw (5,2) to [short, -o] (6,2) node[above]{$v_{out}$};""",#9
        stroke_width=2,
        fill_opacity=0,
        stroke_opacity=1,
        tex_environment="circuitikz",
        tex_template=template,
        ).scale(0.7)

        c = MathTex(
        r"""\draw (-0.5,0) to[short] (1,0);""",#0
        r"""\draw (1,0)node[op amp, noinv input up, anchor=+] (OA){\texttt{}}
        (OA.-) to[short] ++(-0.5,0) to[short] (0.5, -2) to[short] (5,-2)
        (OA.out) to[short] ++(0.12, 0) coordinate(OAo) to[short] (3.5,1.15)
        (OA.+) to[short] ++(-0.5,0);""",#1
        r"""\draw (-0.5,-4) to[zzD,v^>= $$, -o] (-0.5, 0);""",#2
        r"""\draw (-0.5, 0) to[R, v^>= $$, -o] (-0.5,2);""",#3
        r"""\draw (-0.5,2) to [short, -o] (-1.5,2) node[above]{$v_{in}$};""",#4
        r"""\draw (-0.5,-4) node[ground]{} (-0.5,2) to[short] (2.5,2) ;""",#5
        r"""\draw (2.5,2) to[Tnpn, invert] (4.5,2) to[short] (5,2);""",#6
        r"""\draw (5,2) to[R,l_={$2k$}, o-] (5,-2);""",#7
        r"""\draw (5,-2) to[R,l_={$1k$}, o-] (5,-4) node[ground]{};""",#8
        r"""\draw (5,2) to [short, -o] (6,2) node[above]{$v_{out}$};""",#9
        stroke_width=2,
        fill_opacity=0,
        stroke_opacity=1,
        tex_environment="circuitikz",
        tex_template=template,
        ).scale(0.7)

        d = MathTex(
        r"""\draw (-0.5,0) to[short] (1,0);""",#0
        r"""\draw (1,0)node[op amp, noinv input up, anchor=+] (OA){\texttt{}}
        (OA.-) to[short] ++(-0.5,0) to[short] (0.5, -2) to[short] (5,-2)
        (OA.out) to[short] ++(0.12, 0) coordinate(OAo) to[short] (3.5,1.15)
        (OA.+) to[short] ++(-0.5,0);""",#1
        r"""\draw (-0.5,-4) to[zzD,v^>= $$, -o] (-0.5, 0);""",#2
        r"""\draw (-0.5, 0) to[R, v^>= $$, -o] (-0.5,2);""",#3
        r"""\draw (-0.5,2) to [short, -o] (-1.5,2) node[above]{$v_{in}$};""",#4
        r"""\draw (-0.5,-4) node[ground]{} (-0.5,2) to[short] (2.5,2) ;""",#5
        r"""\draw (2.5,2) to[Tnpn, invert] (4.5,2) to[short] (5,2);""",#6
        r"""\draw (5,2) to[R,l_={$R_1$}, o-] (5,-2);""",#7
        r"""\draw (5,-2) to[R,l_={$R_2$}, o-] (5,-4) node[ground]{};""",#8
        r"""\draw (5,2) to [short, -o] (6,2) node[above]{$v_{out}$};""",#9
        stroke_width=2,
        fill_opacity=0,
        stroke_opacity=1,
        tex_environment="circuitikz",
        tex_template=template,
        ).scale(0.7)

        scope1 = SineScope(lambda x: ripple(np.sin((3 * x) + (phi.get_value()))), a[3], DL, 0.5,YELLOW)
        scope2 = SineScope(lambda x: 0.75, a[8], DR, 0.5, BLUE)

        vin = always_redraw(lambda:DecimalNumber(21.2*ripple(np.sin((2*PI) + (phi.get_value()))),
                            num_decimal_places=1).move_to(scope1.group.get_critical_point(UP)+[0,0.3,0])
        )
        vin_l = always_redraw(lambda: MathTex("V").next_to(vin.get_critical_point(RIGHT), buff = 0.1))

        vout = always_redraw(lambda:DecimalNumber(15,
                            num_decimal_places=1).move_to(scope2.group.get_critical_point(UP)+[0,0.3,0])
        )
        vout_l = always_redraw(lambda: MathTex("V").next_to(vout.get_critical_point(RIGHT), buff = 0.1))

        vr = always_redraw(lambda:DecimalNumber((21.2*ripple(np.sin((2*PI) + (phi.get_value()))))-5,
                            num_decimal_places=1).move_to(a[2].get_critical_point(LEFT)+[-0.5,0,0])
        )
        vr_l = always_redraw(lambda: MathTex("V").next_to(vr.get_critical_point(RIGHT), buff = 0.1))

        vd = always_redraw(lambda:DecimalNumber(5,
                            num_decimal_places=1).move_to(a[1].get_critical_point(LEFT)+[-0.8,0,0])
        )
        vd_l = always_redraw(lambda: MathTex("V").next_to(vd.get_critical_point(RIGHT), buff = 0.1))

        vninv = always_redraw(lambda:DecimalNumber(5,
                            num_decimal_places=1).move_to(b[1].get_critical_point(LEFT)+[0,0.8,0])
        )
        vninv_l = always_redraw(lambda: MathTex("V").next_to(vninv.get_critical_point(RIGHT), buff = 0.1))

        vinv = always_redraw(lambda:DecimalNumber((v1(vr2.get_value()))/3,
                            num_decimal_places=1).move_to(b[1].get_critical_point(LEFT)+[0,-0.3,0])
        )
        vinv_l = always_redraw(lambda: MathTex("V").next_to(vinv.get_critical_point(RIGHT), buff = 0.1))

        voutp = always_redraw(lambda:DecimalNumber(vr1.get_value(),
                            num_decimal_places=1).move_to(b[7].get_critical_point(LEFT)+[-1.75,0.25,0])
        )
        voutp_l = always_redraw(lambda: MathTex("V").next_to(voutp.get_critical_point(RIGHT), buff = 0.1))

        vout2 = always_redraw(lambda:DecimalNumber(v1(vr2.get_value()),
                            num_decimal_places=1).move_to(b[9].get_critical_point(DR)+[1,0,0])
        )
        vout2_l = always_redraw(lambda: MathTex("V").next_to(vout2.get_critical_point(RIGHT), buff = 0.1))

        vres1 = always_redraw(lambda:DecimalNumber((v1(vr2.get_value())/3)*2,
                            num_decimal_places=1).move_to(c[7].get_critical_point(RIGHT)+[0.5,0,0])
        )
        vres1_l = always_redraw(lambda: MathTex("V").next_to(vres1.get_critical_point(RIGHT), buff = 0.1))

        vres2 = always_redraw(lambda:DecimalNumber(v1(vr2.get_value())/3,
                            num_decimal_places=1).move_to(c[8].get_critical_point(RIGHT)+[0.5,0.250,0])
        )
        vres2_l = always_redraw(lambda: MathTex("V").next_to(vres2.get_critical_point(RIGHT), buff = 0.1))

        self.play(Write(a))#0
        self.wait(0.2)
        self.play(Indicate(a[5]))#2
        self.wait(0.2)
        self.play(Indicate(a[5]),Indicate(a[0]),Indicate(a[6]), run_time=1.5)#4
        self.wait(0.2)      
        self.play(FadeIn(scope1.group, vin, vin_l), FadeIn(scope2.group, vout, vout_l))#6
        self.wait(0.2)
        self.play(phi.animate.set_value(4*PI), run_time = 3, rate_func = linear)#8
        self.wait(0.2)
        self.play(Indicate(a[1]))#10
        self.wait(0.2)
        self.play(FadeTransform(a,b), FadeIn(vr, vr_l), FadeIn(vd, vd_l))#12
        self.wait(0.2)
        self.play(phi.animate.set_value(8*PI), run_time = 3, rate_func = linear)#14
        self.wait(0.2)
        self.play(FadeTransform(vd.copy(),vninv),FadeTransform(vd_l.copy(),vninv_l))#16
        self.wait(0.2)
        self.play(Indicate(b[1]),Indicate(b[7]),Indicate(b[6]))#18
        self.wait(0.2)
        self.play(Indicate(b[2]))#20
        self.wait(0.2)
        self.play(Indicate(vout),Indicate(vout_l))#22
        self.wait(0.2)
        self.play(Indicate(b[8]))#24
        self.wait(0.2)
        self.play(FadeIn(vres2, vres2_l))#26
        self.wait(0.2)
        self.play(FadeTransform(vres2.copy(),vinv),FadeTransform(vres2_l.copy(),vinv_l))#28
        self.wait(0.2)
        self.play(Indicate(b[7]))#30
        self.wait(0.2)
        self.play(FadeIn(vres1, vres1_l))#32
        self.wait(0.2)
        self.play(FadeTransform(b,c))#34
        self.wait(0.2)
        self.play(FadeIn(vninv, vninv_l, vinv, vinv_l, voutp, voutp_l, vout2, vout2_l), FadeOut(scope2.group, vout, vout_l),vr1.animate.set_value(0), vr2.animate.set_value(0))#26
        self.wait(0.2)
        self.play(phi.animate.set_value(16*PI),vr1.animate.set_value(15.6), vr2.animate.set_value(15.6),  run_time = 5, rate_func = linear)#28
        self.wait(1)
        self.play(phi.animate.set_value(20*PI),vr1.animate.set_value(15.6), vr2.animate.set_value(14.1),  run_time = 2.5, rate_func = linear)#30
        self.wait(1)
        self.play(phi.animate.set_value(28*PI),vr1.animate.set_value(16), vr2.animate.set_value(15.6),  run_time = 5, rate_func = linear)#32
        self.wait(1)
        self.play(FadeTransform(c,d),vr1.animate.set_value(0), vr2.animate.set_value(0),phi.animate.set_value(8*PI))#44
        self.wait(0.2)
        self.play(phi.animate.set_value(16*PI),vr1.animate.set_value(15.6), vr2.animate.set_value(15.6),  run_time = 5, rate_func = linear)#28
        self.wait(1)
        self.play(phi.animate.set_value(20*PI),vr1.animate.set_value(15.6), vr2.animate.set_value(14.1),  run_time = 2.5, rate_func = linear)#30
        self.wait(1)
        self.play(phi.animate.set_value(28*PI),vr1.animate.set_value(16), vr2.animate.set_value(15.6),  run_time = 5, rate_func = linear)#32
        self.wait(1)
