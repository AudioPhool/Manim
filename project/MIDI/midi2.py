from manim import *

class anim(Scene):
    def construct(self):
        template = TexTemplate()
        template.add_to_preamble(r"\usepackage[siunitx, RPvoltages, american, europeanresistors]{circuitikz}")

        keyb = ImageMobject("project/MIDI/key.jpg").shift(LEFT*4+UP*1.5).scale(0.3)
        micro = ImageMobject("project/MIDI/mnobg.png").shift(RIGHT*4+UP*1.5).scale(0.65).set_z_index(1)
        line = Line(start=keyb.get_right(), end=micro.get_center()).set_z_index(-1)

        self.play(FadeIn(keyb, micro, line)) 

        binary_digits = [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
        decimal_digits = [DecimalNumber(digit, num_decimal_places=0) for digit in binary_digits]
        decimal_digits = VGroup(*decimal_digits)
        decimal_digits.move_to(line.get_start() + [0, 0.25, 0])

        label1 = Tex("Byte 1: ").next_to(micro, DL, buff = 0.2, aligned_edge = RIGHT)
        byte1 = [1, 0, 0, 1, 0, 0, 0, 0]
        byte1 = [DecimalNumber(digit, num_decimal_places=0) for digit in byte1]
        byte1 = VGroup(*byte1)
        byte1.arrange(RIGHT, buff=0.05)
        byte1.next_to(label1, RIGHT, buff=0.05).shift(UP*0.05)
        
        label2 = Tex("Byte 2: ").next_to(label1, DOWN, buff = 0.2, aligned_edge = RIGHT)
        byte2 = [0, 0, 1, 1, 0, 0, 0, 0]
        byte2 = [DecimalNumber(digit, num_decimal_places=0) for digit in byte2]
        byte2 = VGroup(*byte2)
        byte2.arrange(RIGHT, buff=0.05)
        byte2.next_to(label2, RIGHT, buff=0.05).shift(UP*0.05)

        label3 = Tex("Byte 3: ").next_to(label2, DOWN, buff = 0.2, aligned_edge = RIGHT)
        byte3 = [0 , 1, 0, 0, 0, 0, 0, 0]
        byte3 = [DecimalNumber(digit, num_decimal_places=0) for digit in byte3]
        byte3 = VGroup(*byte3)
        byte3.arrange(RIGHT, buff=0.05)
        byte3.next_to(label3, RIGHT, buff=0.05).shift(UP*0.05)

        #anim 1-49
        for digit, byte_index in zip(decimal_digits, range(0, 24)):
            if byte_index < 8:
                binary_byte = byte1[0:byte_index%8+1]
                self.add(label1)
            elif (byte_index >= 8 and byte_index < 16):
                binary_byte = byte2[0:byte_index%8+1]
                self.add(label2)
            else:
                binary_byte = byte3[0:byte_index%8+1]
                self.add(label3)

            self.play(digit.animate.move_to(line.get_end() + [0, 0.25, 0]),run_time=0.3)
            self.play(binary_byte.animate.set_opacity(1), run_time = 0.1)

        self.wait() 

        animgrp = VGroup(label1, byte1, label2, byte2, label3, byte3)

        self.play(LaggedStart(FadeOut(decimal_digits, keyb, micro, line),animgrp.animate.scale(2).move_to([0,0,0]), lag_ratio=0.3))
