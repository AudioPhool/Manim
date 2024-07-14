from manim import *

class anim(Scene):
    def construct(self):
        template = TexTemplate()
        template.add_to_preamble(r"\usepackage[siunitx, RPvoltages, american, europeanresistors]{circuitikz}")

        a = MathTex("a",
        stroke_width=3,
        fill_opacity=0,
        stroke_opacity=1,
        tex_environment="circuitikz",
        tex_template=template
        )

        ic = MathTex("I_C")
        eq = MathTex(" = ").next_to(ic,RIGHT, buff=0.2)
        isat = MathTex("I_S").next_to(eq,RIGHT, buff=0.2)
        exp = MathTex("(e^{V_{BE}/V_T} - 1)").next_to(isat,RIGHT, buff=0.2)

        ebs = VGroup(ic,eq,isat,exp)

        self.wait(0.1)          #0
        self.play(FadeIn(a))
        self.wait(0.1)          #2
        self.play(a.animate.shift(UP))
        self.play(Indicate(ebs[3])) 
        self.wait(0.1) #3
        
        current = ValueTracker(10)
        voltage = ValueTracker(0.65)

        ic1   = always_redraw(lambda: DecimalNumber(current.get_value(), 0))
        eq1   = MathTex(" = ").next_to(ic1,RIGHT, buff=0.2)
        isat1 = MathTex("I_S").next_to(eq1,RIGHT, buff=0.2)
        e1    = MathTex("(e").next_to(isat1,RIGHT, buff=0.2)
        vbe1  = always_redraw(lambda: DecimalNumber(voltage.get_value(), 2).next_to(e1,RIGHT, buff=0.1).shift(UP*0.2))
        vt1   = MathTex("/0.026").next_to(vbe1,RIGHT, buff=0.1).shift(DOWN*0.05)
        m11   = MathTex("-1)").next_to(vt1,RIGHT, buff=0.2).shift(DOWN*0.15)
        
        exp1 = VGroup(e1, vbe1, vt1, m11)
        ebs1 = VGroup(ic1,eq1,isat1,exp1)


        ic2   = MathTex("I_C")
        eq2   = MathTex(" = ").next_to(ic2,RIGHT, buff=0.2)
        isat2 = MathTex("I_S").next_to(eq2,RIGHT, buff=0.2)
        e2    = MathTex("(e").next_to(isat2,RIGHT, buff=0.2)
        vbe2  = MathTex("V_{BE}").next_to(e2,RIGHT, buff=0.1).shift(UP*0.2)
        vt2  = MathTex("/V_T").next_to(vbe2,RIGHT, buff=0.1).shift(DOWN*0.05)
        m12   = MathTex("-1)").next_to(vt2,RIGHT, buff=0.2).shift(DOWN*0.15)
        
        exp2 = VGroup(e2, vbe2, vt2, m12)
        ebs2 = VGroup(ic2,eq2,isat2,exp2)

        self.play(ReplacementTransform(ebs, ebs1)) 
        self.wait(0.1) #4
        self.play(current.animate.set_value(20), voltage.animate.set_value(0.69), run_time = 2 ) 
        self.wait(0.1) #5
        self.play(current.animate.set_value(5) , voltage.animate.set_value(0.63), run_time = 2 ) 
        self.wait(0.1) #6
        self.play(ReplacementTransform(ebs1, ebs2)) 
        self.wait(0.1) #7