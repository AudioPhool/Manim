from manim import *

class anim(Scene):
    def construct(self):
        micro = ImageMobject("project/MIDI/mnobg.png").shift(RIGHT*6+UP*0).scale(0.65).set_z_index(1)
        
        # Create the buffer array
        buffer_array = VGroup(*[Rectangle(width=1, height=1, color = GRAY) for i in range(8)]).arrange(RIGHT, buff = 0.01)
        buffer_label = Tex("Midi Buffer", color = YELLOW_D).set_z(1).next_to(buffer_array, LEFT, 0.2)

        # Create the read and write headers
        read_header = Arrow(UP, UP+DOWN*0.5, buff=0)
        read_header.next_to(buffer_array[5], UP)
        read_label = Tex("Read\_h")
        read_label.next_to(read_header, UP)
        read_header_group = VGroup(read_header, read_label).set_color(RED_C)
        write_header = Arrow(DOWN, DOWN+UP*0.5, buff=0)
        write_label = Tex("Write\_h")
        write_header.next_to(buffer_array[5], DOWN)
        write_label.next_to(write_header, DOWN)
        write_header_group = VGroup(write_header, write_label).set_color(BLUE_C)
        
         # Define the buffer strings
        buffer_strings = ["C3", "Eb3", "G4", "Ab3", "C3", "", "", ""]

        

        # Add the buffer and headers to the scene
        self.play(Create(buffer_array), Create(read_header_group), Create(write_header_group), Create(buffer_label), FadeIn(micro))

        # Create the buffer array
        buffer_array = VGroup(*[Rectangle(width=1, height=1, color=GRAY) for i in range(8)]).arrange(RIGHT, buff=0.01)
        for i, rect in enumerate(buffer_array):
            text = Text(buffer_strings[i], font_size=20).set_color(WHITE)
            text.move_to(rect.get_center())
            self.play(Create(text), run_time = 0.2)

        buffer_strings = ["C3", "Eb3", "G4", "D3", "C3", "G4", "Bb3", "Ab3"]
        b1 = Text(buffer_strings[5], font_size=20).move_to(buffer_array[5].get_center())
        b2 = Text(buffer_strings[6], font_size=20).move_to(buffer_array[6].get_center())
        b3 = Text(buffer_strings[7], font_size=20).move_to(buffer_array[7].get_center())
        b4 = Text(buffer_strings[4], font_size=20).move_to(buffer_array[0].get_center())

        # Move the write head one position forward
        self.play(LaggedStart(Write(b1), write_header_group.animate.shift(RIGHT*1), lag_ratio=0.5, run_time=1))

        # Move the read head one position forward
        self.play(LaggedStart((b1.copy().animate.move_to(micro)), (read_header_group.animate.shift(RIGHT*1)) , lag_ratio=0, run_time=1))

        # Move the write head one position forward
        self.play(LaggedStart(Write(b2), write_header_group.animate.shift(RIGHT*1), lag_ratio=0.5, run_time=1))

        # Move the write head one position forward
        self.play(LaggedStart(Write(b3), write_header_group.animate.shift(LEFT*7), lag_ratio=0.5, run_time=1))

        # Move the write head one position forward
        self.play(LaggedStart((b2.copy().animate.move_to(micro)), (read_header_group.animate.shift(RIGHT*1)) , lag_ratio=0.5, run_time=1))

        # Move the write head one position forward
        self.play(LaggedStart((b3.copy().animate.move_to(micro)), (read_header_group.animate.shift(LEFT*7)) , lag_ratio=0.5, run_time=1))