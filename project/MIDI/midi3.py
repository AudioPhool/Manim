from manim import *

class anim(Scene):
    def construct(self):
        template = TexTemplate()
        template.add_to_preamble(r"\usepackage[siunitx, RPvoltages, american, europeanresistors]{circuitikz}")

        label1 = Tex("Byte 1: ")
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
        byte3 = [0, 1, 0, 0, 0, 0, 0, 0]
        byte3 = [DecimalNumber(digit, num_decimal_places=0) for digit in byte3]
        byte3 = VGroup(*byte3)
        byte3.arrange(RIGHT, buff=0.05)
        byte3.next_to(label3, RIGHT, buff=0.05).shift(UP*0.05)

        animgrp = VGroup(label1, byte1, label2, byte2, label3, byte3).scale(2).move_to([0,0,0])

        self.add(animgrp)
        self.wait()#1
        self.play(
        label1.animate.shift(LEFT*1 + UP*0.75),
        label2.animate.shift(LEFT*1 + UP*0),
        label3.animate.shift(LEFT*1 + UP*-0.75),
        # Change buffer for bits in each byte to spread them out
        byte1.animate.arrange(RIGHT, buff=0.4).next_to(label1, RIGHT, buff=0.05).shift(UP*0.1).shift(LEFT*0.9 + UP*0.75),
        byte2.animate.arrange(RIGHT, buff=0.4).next_to(label2, RIGHT, buff=0.05).shift(UP*0.1).shift(LEFT*0.9 + UP*0),
        byte3.animate.arrange(RIGHT, buff=0.4).next_to(label3, RIGHT, buff=0.05).shift(UP*0.1).shift(LEFT*0.9 + UP*-0.75)
        )
        self.wait()#3

        status_label = Tex("Status", color = RED).next_to(byte1[0], direction=UP, buff=0.1)
        data1_label = Tex("Data", color = RED).next_to(byte2[0], direction=UP, buff=0.1)
        data2_label = Tex("Data", color = RED).next_to(byte3[0], direction=UP, buff=0.1)
        label4 = Tex("Status Byte: ").move_to(label1).scale(2).shift(LEFT*1.2).set_color(color = RED)
        label5 = Tex("Data1 Byte: ").move_to(label2).scale(2).shift(LEFT*1.1).set_color(color = RED)
        label6 = Tex("Data2 Byte: ").move_to(label3).scale(2).shift(LEFT*1.1).set_color(color = RED)

        self.play(
        byte1[0].animate.set_color(RED_B),
        byte2[0].animate.set_color(RED_B),
        byte3[0].animate.set_color(RED_B),
        FadeIn(status_label, data1_label, data2_label)
        )
        # Define animation groups
        group1 = AnimationGroup(Transform(status_label.copy(), label4), FadeOut(label1))
        group2 = AnimationGroup(Transform(data1_label.copy(), label5), FadeOut(label2))
        group3 = AnimationGroup(Transform(data2_label.copy(), label6), FadeOut(label3))
        self.wait()#5
        self.play(group1, run_time = 2)
        self.wait()#5

        self.play(
            LaggedStart(group2, group3, lag_ratio=0.7, run_time = 2)
        )

        self.wait()#7

        noteon_l = Tex("Note On", color = GOLD_E).next_to(byte1[2], direction=DOWN, buff=0.1)
        data1_label = Tex("Data", color = RED_B).next_to(byte2[0], direction=UP, buff=0.1)
        data2_label = Tex("Data", color = RED_B).next_to(byte3[0], direction=UP, buff=0.1)         

        self.play(
            byte1[1].animate.set_color(GOLD_A),
            byte1[2].animate.set_color(GOLD_A),
            byte1[3].animate.set_color(GOLD_A),
            FadeIn(noteon_l))

        self.wait()#9

        midch_l = Tex("MIDI Channel 1", color = BLUE).next_to(byte1[5], direction=UP, buff=0.1).shift(RIGHT*0.4)
        self.play(
            byte1[4].animate.set_color(BLUE_C),
            byte1[5].animate.set_color(BLUE_C),
            byte1[6].animate.set_color(BLUE_C),
            byte1[7].animate.set_color(BLUE_C),
            FadeIn(midch_l)
        )

        self.wait()#11

        note_l = Tex("Key 48 (C3)", color = GREEN_E).next_to(byte2[4], direction=DOWN, buff=0.1)
        self.play(
            byte2[1].animate.set_color(GREEN_C),
            byte2[2].animate.set_color(GREEN_C),
            byte2[3].animate.set_color(GREEN_C),
            byte2[4].animate.set_color(GREEN_C),
            byte2[5].animate.set_color(GREEN_C),
            byte2[6].animate.set_color(GREEN_C),
            byte2[7].animate.set_color(GREEN_C),
            FadeIn(note_l)
        )

        self.wait()#13

        vel_l = Tex("Velocity 64", color = PURPLE_D).next_to(byte3[4], direction=DOWN, buff=0.1)
        self.play(
            byte3[1].animate.set_color(PURPLE_C),
            byte3[2].animate.set_color(PURPLE_C),
            byte3[3].animate.set_color(PURPLE_C),
            byte3[4].animate.set_color(PURPLE_C),
            byte3[5].animate.set_color(PURPLE_C),
            byte3[6].animate.set_color(PURPLE_C),
            byte3[7].animate.set_color(PURPLE_C),
            FadeIn(vel_l)
        )

        self.wait()#13

