from manim import *
from scipy import interpolate

class anim(Scene):
    def construct(self):
        template = TexTemplate()
        template.add_to_preamble(r"\usepackage[siunitx, RPvoltages, american, europeanresistors]{circuitikz}")
        
        
        top    = Rectangle(width=1, height=0.5, color=WHITE, fill_color = GOLD_D, fill_opacity = 0.9, stroke_width = 0.6)
        label  = Tex("- +").move_to(top)
        pos    = Rectangle(width=0.135  , height=0.05, color=WHITE, fill_color = GRAY_A, fill_opacity = 0.9, stroke_width = 0.6
                           ).align_to(top.get_critical_point(UR)+[-0.25,0,0], DR)
        neg    = Rectangle(width=0.15, height=0.075, color=WHITE, fill_color = GRAY_A, fill_opacity = 0.9, stroke_width = 0.6
                           ).align_to(top.get_critical_point(UL)+[0.15,0,0], DL)    
        bottom = Rectangle(width=1, height=1  , color=WHITE, fill_color = GRAY_D, fill_opacity = 0.9, stroke_width = 0.6
                           ).align_to(top.get_critical_point(DOWN), UP)
        
        batt = VGroup(top, label, bottom, pos, neg)
        
        self.play(FadeIn(batt))
        self.wait(0.2)
        self.play(batt.animate.shift(UP*2))
        self.wait(0.2)
        
        stroke = 2
        
        res = MathTex(r"""\draw (0,-2) to[short] (0,0);""",
        stroke_width=2,
        fill_opacity=0,
        stroke_opacity=1,
        tex_environment="circuitikz",
        tex_template=template
        ).shift(RIGHT*3)
        restop = res.get_critical_point(UP)
        resbot = res.get_critical_point(DOWN)
        
        dmm = MathTex(r"""\draw (0,0) to[qvprobe, v = $$, mirror] ++(-2,0);""",
        stroke_width=2,
        fill_opacity=0,
        stroke_opacity=1,
        tex_environment="circuitikz",
        tex_template=template
        ).shift(DOWN*2)
        dmmr = dmm.get_critical_point(RIGHT)
        dmml = dmm.get_critical_point(LEFT)

        line1 = Line(
            start=pos.get_critical_point(UP),
            end=(pos.get_critical_point(UP)+[0,0.75,0]),
            stroke_width=stroke
        )
        line1end = line1.get_end()
        
        line2 = Line(
            start=line1end,
            end=([restop[0],line1end[1],0]),
            stroke_width=stroke
        )
        line2end = line2.get_end()

        line3 = Line(
            start=line2end,
            end=restop,
            stroke_width=stroke
        )
        line4 = Line(
            start=resbot,
            end=([restop[0],dmmr[1]-0.1975,0]),
            stroke_width=stroke
        )
        line4end = line4.get_end()

        line5 = Line(
            start=line4end,
            end=(dmmr+[0,-0.1975,0]),
            stroke_width=stroke
        )

        line6 = Line(
            start=neg.get_critical_point(UP),
            end=(neg.get_critical_point(UP)+[0,0.75,0]),
            stroke_width=stroke
        )
        line6end = line6.get_end()
        
        line7 = Line(
            start=line6end,
            end=([-3,line6end[1],0]),
            stroke_width=stroke
        )
        line7end = line7.get_end()
        line8 = Line(
            start=line7end,
            end=([-3,dmml[1]-0.1975,0]),
            stroke_width=stroke
        )
        line9 = Line(
            start=line8.get_end(),
            end=(dmml+[0,-0.1975,0]),
            stroke_width=stroke
        )
        #self.play(Create(line1,line2,line3,line4,line5,line6,line7,line8,line9,res,dmm))
        self.play(LaggedStart(Create(line1),Create(line6),Create(line2),Create(line7),Create(line3),Create(line8),
                              Create(res),Create(line4),Create(line5),Create(line9),Create(dmm),
                              lag_ratio=0.4), run_time = 3)
        circuit = VGroup(line1,line6,line2,line7,line3,line8,res,line4,line5,line9,dmm,batt)
        self.wait(0.2)
        
        draw = ValueTracker(0.001)
        
        axes = Axes(x_range=(0,6,1), y_range=(6,10,1),x_length=6, y_length=4.5, 
                    x_axis_config={"include_numbers": False, "numbers_to_exclude": [0]}, y_axis_config={"include_numbers": True}).shift(RIGHT*4)
        a_lab = axes.get_axis_labels(x_label="t", y_label="V")
        curve = always_redraw( lambda:
            axes.plot(lambda x: 
                ((0.0041*x**5) + (-0.0483*x**4) + (0.1009*x**3) + (0.3454*x**2) + (-1.4054*x) + (9.2206)), x_range=[0,draw.get_value()],color=YELLOW_C)
        )
        dot = always_redraw(lambda: Dot(color = YELLOW_C).move_to(curve.get_end()))
        
        self.play(LaggedStart(circuit.animate.shift(LEFT*4+DOWN*0.25), FadeIn(axes,a_lab, curve,dot),lag_ratio=0.5))
        self.wait(0.2)
        self.play(draw.animate.set_value(5), run_time = 5)
        self.wait(0.2)
        
        res2 = MathTex(r"""\draw (2,0) to[vR, v^= $$, mirror] (0,0);""",
        stroke_width=2,
        fill_opacity=0,
        stroke_opacity=1,
        tex_environment="circuitikz",
        tex_template=template
        ).shift(DOWN*1.95+LEFT*4)
        
        
        self.play(circuit.animate.shift(UP*0.5),dmm.animate.shift(UP*2),line5.animate.shift(UP*2),line9.animate.shift(UP*2))
        self.wait(0.2)
        
        line10 = Line(
            start=line8.get_end(),
            end=(res2.get_critical_point(LEFT)),
            stroke_width=stroke
        )
        
        line11 = Line(
            start=line4.get_end(),
            end=(res2.get_critical_point(RIGHT)),
            stroke_width=stroke
        )
        
        self.play(FadeIn(res2), FadeIn(line10, line11), FadeOut(dot, curve), draw.animate.set_value(0.001))
        self.wait(0.2)
        
        draw2 = ValueTracker(0.001)
        
        poly2 = [-0.034358974358975, 0.406643356643363, -1.582342657342689, 2.330740093240166, -1.448187645687716, 9.220454545454563]
        curve2 = always_redraw( lambda:
            axes.plot(lambda x: 
                ((poly2[0]*x**5) + (poly2[1]*x**4) + (poly2[2]*x**3) + (poly2[3]*x**2) + (poly2[4]*x) + (poly2[5])), x_range=[0,draw2.get_value()],color=YELLOW_C)
        )
        dot2 = always_redraw(lambda: Dot(color = YELLOW_C).move_to(curve2.get_end()))
        R_lab = MathTex("R =").scale(1).shift(DOWN*3+LEFT*4)
        number2 = always_redraw(lambda:DecimalNumber(
                 10000-(3000*(10-((poly2[0]*draw2.get_value()**5) + (poly2[1]*draw2.get_value()**4) + (poly2[2]*draw2.get_value()**3) + (poly2[3]*draw2.get_value()**2) + (poly2[4]*draw2.get_value()) + (poly2[5])))), 
                 show_ellipsis=False, 
                 num_decimal_places=0
                 ).scale(1).next_to(R_lab, RIGHT))
        
        self.play(FadeIn(curve2, dot2, R_lab, number2))
        self.wait(0.2)
        self.play(draw2.animate.set_value(5), run_time = 7, rate_func = linear)
        self.wait(0.2)