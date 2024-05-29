from manim import *

class anim(Scene):
    def construct(self):

        # Define the code to display
        code_text = '''uint8_t midi[3];'''
        # Create a Code object with the code text
        code = Code(code = code_text, language='c++', font="Consolas").scale(1).shift(UP*2.5)

        #create arrays
        buffer_array = VGroup(*[Rectangle(width=1, height=1, color = GRAY) for i in range(8)]).arrange(RIGHT, buff = 0.01)
        buffer_label = Tex("Midi[0]", color = YELLOW_D).set_z(1).next_to(buffer_array, LEFT, 0.2)
        buffer_array = VGroup(buffer_array, buffer_label).shift(UP*1.25)

        buffer_array1 = VGroup(*[Rectangle(width=1, height=1, color = GRAY) for i in range(8)]).next_to(buffer_array, DOWN, buff = 1).arrange(RIGHT, buff = 0.01)
        buffer_label1 = Tex("Midi[1]", color = YELLOW_D).set_z(1).next_to(buffer_array1, LEFT, 0.2)
        buffer_array1 = VGroup(buffer_array1, buffer_label1)

        buffer_array2 = VGroup(*[Rectangle(width=1, height=1, color = GRAY) for i in range(8)]).arrange(RIGHT, buff = 0.01)
        buffer_label2 = Tex("Midi[2]", color = YELLOW_D).set_z(1).next_to(buffer_array2, LEFT, 0.2)
        buffer_array2 = VGroup(buffer_array2, buffer_label2).shift(DOWN*1.25)

        self.play(LaggedStart(Create(code),Create(buffer_array),Create(buffer_array1),Create(buffer_array2)))
        self.wait()#1

        # Add animation to fill each byte in the appropriate array
        byte0 = [1, 0, 0, 1, 0, 0, 0, 0]
        byte0 = [DecimalNumber(digit,num_decimal_places=0)for digit in byte0]
        byte0 = VGroup(*byte0)
        byte0.arrange(RIGHT, buff = 0.81).shift(UP*1.25)
        byte1 = [0, 0, 1, 1, 0, 0, 0, 0]
        byte1 = [DecimalNumber(digit,num_decimal_places=0)for digit in byte1]
        byte1 = VGroup(*byte1)
        byte1.arrange(RIGHT, buff = 0.81).shift(UP*0)
        byte2 = [0, 1, 0, 0, 0, 0, 0, 0]
        byte2 = [DecimalNumber(digit,num_decimal_places=0)for digit in byte2]
        byte2 = VGroup(*byte2)
        byte2.arrange(RIGHT, buff = 0.81).shift(UP*-1.25)

        t1 = Tex("Status Byte",color = RED_C).next_to(buffer_array)
        t2 = Tex("Data1 Byte", color = ORANGE).next_to(buffer_array1)
        t3 = Tex("Data2 Byte", color = ORANGE).next_to(buffer_array2)

        self.play(LaggedStart(Create(byte0),Create(byte1),Create(byte2)))
        self.wait(0.1)#3
        self.play(LaggedStart(Create(t1),Create(t2),Create(t3)))
        self.wait()#5




