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

        binary_labels = [DecimalNumber(digit, num_decimal_places=0) for digit in binary_digits]
        binary_labels = VGroup(*binary_labels)
        binary_labels.arrange(RIGHT, buff=0.05)
        binary_labels.next_to(micro, DOWN, buff=0.2)

        for digit, byte_index in zip(decimal_digits, range(0, len(binary_digits))):
            binary_byte = binary_labels[0:byte_index]
            self.play(LaggedStart(
                digit.animate.move_to(line.get_end() + [0, 0.25, 0]),
                binary_byte.animate.set_opacity(1),
                lag_ratio=0.8,
                run_time=0.4
            ))


        self.wait() 
