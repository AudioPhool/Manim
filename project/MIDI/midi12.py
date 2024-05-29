from manim import *

class anim(Scene):
    def construct(self):
        keyb = ImageMobject("project/MIDI/key.jpg").scale(2.35).shift(UP*4+RIGHT*3.75)
        
        c3 = Tex("3.000",color = BLUE_D).next_to(keyb, DL, buff=0.1).shift(DOWN*0.5+RIGHT*1.8)
        c4 = Tex("4.000",color = BLUE_D).next_to(keyb, DOWN, buff=0.1).shift(DOWN*0.5)

        # Add c3 and c4 to the scene
        self.add(keyb, c3, c4)

        a1=Tex("3.083",color = GOLD_D).next_to(c3, UR, buff=0.1).shift(LEFT*0.4)
        a2=Tex("3.167",color = BLUE_D).next_to(c3, RIGHT, buff=0.8).shift(LEFT*0.4)
        a3=Tex("3.250",color = GOLD_D).next_to(a1, RIGHT, buff=0.5)
        a4=Tex("3.333",color = BLUE_D).next_to(a2, RIGHT, buff=0.35)
        a5=Tex("3.417",color = BLUE_D).next_to(a4, RIGHT, buff=0.3)
        a6=Tex("3.5",color = GOLD_D).next_to(a5, UR, buff=0.1).shift(LEFT*0.15)
        a7=Tex("3.583",color = BLUE_D).next_to(a5, RIGHT, buff=0.35)
        a8=Tex("3.667",color = GOLD_D).next_to(a6, RIGHT, buff=0.5)
        a9=Tex("3.750",color = BLUE_D).next_to(a7, RIGHT, buff=0.35)
        a10=Tex("3.833",color = GOLD_D).next_to(a8, RIGHT, buff=0.35)
        a11=Tex("3.917",color = BLUE_D).next_to(a9, RIGHT, buff=0.35)

        
        self.wait()#1
        self.play(LaggedStart(TransformFromCopy(c3,a1),TransformFromCopy(c3,a2),TransformFromCopy(c3,a3),TransformFromCopy(c3,a4),TransformFromCopy(c3,a5),TransformFromCopy(c3,a6),
                              TransformFromCopy(c3,a7),TransformFromCopy(c3,a8),TransformFromCopy(c3,a9),TransformFromCopy(c3,a10),TransformFromCopy(c3,a11),lag_ratio=0.5))
        self.wait()#3