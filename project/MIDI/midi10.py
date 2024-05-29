from manim import *

class anim(Scene):
    def construct(self):
        
        keyb = ImageMobject("project/MIDI/key.jpg").shift(LEFT*5+UP*0).scale(0.35).set_z_index(1)
        micro = ImageMobject("project/MIDI/micro.png").shift(RIGHT*0.5+UP*0).scale(1.5).set_z_index(1).rotate(25*DEGREES)

        line = Line(start=keyb.get_center(), end=ORIGIN)
        l1 = Line(start= [0,1.5,0] , end= [3.5,1.5,0])
        l2 = Line(start= [0,0,0]   , end= [3.5,0,0])
        l3 = Line(start= [0,-1.5,0], end= [3.5,-1.5,0])

        tlab = Tex("Trig").next_to(l1.get_end(), UL, buff = 0.1)
        glab = Tex("Gate").next_to(l2.get_end(), UL, buff = 0.1)
        cvlab = Tex("CV").next_to(l3.get_end(), UL, buff = 0.1)

        trig_led = Circle(radius=0.35, fill_opacity=1.0, fill_color=BLUE_E, stroke_width = 3, stroke_color = WHITE).next_to(l1.get_end(),RIGHT,buff=0)
        gate_led = Circle(radius=0.35, fill_opacity=1.0, fill_color=MAROON_E, stroke_width = 3, stroke_color = WHITE).next_to(l2.get_end(),RIGHT,buff=0)
        volt = ValueTracker(0)
        cv = DecimalNumber(
            num_decimal_places=3,
            include_sign=False,
            unit="V"
        ).next_to(l3.get_end(), RIGHT, buff = 0.05)
        cv.add_updater(lambda d: d.set_value(volt.get_value()))

        self.play(LaggedStart(FadeIn(micro),FadeIn(keyb),Create(line),Create(l1),Create(l2),Create(l3), Create(tlab), Create(glab), Create(cvlab), Create(trig_led), Create(gate_led), Create(cv),lag_ratio=0.8,run_time = 1))
        self.wait()#1

        # Add a box that highlights a single key on the MIDI keyboard image
        key_box = Rectangle(height = 0.8, width=0.15,stroke_opacity = 0, fill_color = ORANGE,fill_opacity = 0.7).move_to(keyb.get_center()+[-0.02,-0.5,0]).set_z_index(2)
        mc1 = Tex("Note On")
        mc2= Tex("(0x90)").next_to(mc1,DOWN,buff=0.05)
        mc = VGroup(mc1,mc2).move_to(line.get_start()+[0,0.5,0])
        mc3 = Tex("Note Off")
        mc4= Tex("(0x80)").next_to(mc3,DOWN,buff=0.05)
        mcoff = VGroup(mc3,mc4).move_to(line.get_start()+[0,0.5,0])
        
        self.play(LaggedStart(FadeIn(key_box), mc.animate.move_to(line.get_end()+[-1.5,0.5,0])))
        self.wait()#3

        timer = ValueTracker(0)
        timer_text = DecimalNumber(
            num_decimal_places=1,
            include_sign=False,
            unit="ms",
        ).next_to(trig_led, RIGHT, buff=0.1)
        timer_text.add_updater(lambda d: d.set_value(timer.get_value()))
        self.play(
            FadeIn(timer_text),
            run_time=0.5
        )
        self.wait(0.1)#5
        self.play(trig_led.animate.set_fill(color=PURE_BLUE),run_time = 0.1)
        self.wait(0.1)#7
        self.play(gate_led.animate.set_fill(color=PURE_RED),run_time = 0.1)
        self.wait(0.1)#9
        self.play(volt.animate.set_value(4))
        self.wait(0.1)#11
        self.play(timer.animate.set_value(10),run_time = 3, rate_func = linear)
        self.wait(0.1)#13
        self.play(trig_led.animate.set_fill(color=BLUE_E),run_time = 0.1)
        self.wait(0.1)#15
        self.play(LaggedStart(FadeOut(key_box),FadeOut(mc), mcoff.animate.move_to(line.get_end()+[-1.5,0.5,0])))
        self.wait(0.1)#17
        self.play(gate_led.animate.set_fill(color=MAROON_E),run_time = 0.1)
        self.wait(0.1)#19