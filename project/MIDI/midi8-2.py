from manim import *

class anim(Scene):
    def construct(self):

        # Define the code to display
        code_text = '''typedef struct{
        uint8_t status; //Note On/Off
        uint8_t data1;  //Note Number
        uint8_t data2;  //Velocity
        } midiEvent;
        midiEvent event[3]'''

        # Create a Code object with the code text
        code = Code(code = code_text, language='c++', font="Consolas",style = "monokai").scale(0.9).shift(UP*2.7)

        #create arrays
        buffer_array = VGroup(*[Rectangle(width=1, height=0.5, color = GRAY) for i in range(8)]).arrange(RIGHT, buff = 0.01).next_to(code, DOWN, buff = 0.2)
        buffer_label = Tex(".status", color = ORANGE).set_z(1).next_to(buffer_array, RIGHT, 0.2)
        buffer_arrayg = VGroup(buffer_array, buffer_label)

        buffer_array1 = VGroup(*[Rectangle(width=1, height=0.5, color = GRAY) for i in range(8)]).arrange(RIGHT, buff = 0.01).next_to(buffer_array, DOWN, buff = 0)
        buffer_label12 = Tex(".data1", color = ORANGE).set_z(1).next_to(buffer_array1, RIGHT, 0.2)
        buffer_label1 = Tex("event[0]", color = YELLOW_D).set_z(1).next_to(buffer_array1, LEFT, 0.2)
        buffer_array1g = VGroup(buffer_array1, buffer_label1, buffer_label12)

        buffer_array2 = VGroup(*[Rectangle(width=1, height=0.5, color = GRAY) for i in range(8)]).arrange(RIGHT, buff = 0.01).next_to(buffer_array1, DOWN, buff = 0)
        buffer_label2 = Tex(".data2", color = ORANGE).set_z(1).next_to(buffer_array2, RIGHT, 0.2)
        buffer_array2g = VGroup(buffer_array2, buffer_label2)


        
        #create arrays
        buffer1_array = VGroup(*[Rectangle(width=1, height=0.5, color = GRAY) for i in range(8)]).arrange(RIGHT, buff = 0.01).next_to(buffer_array2, DOWN, buff = 0.2)
        buffer1_label = Tex(".status", color = ORANGE).set_z(1).next_to(buffer1_array, RIGHT, 0.2)
        buffer1_arrayg = VGroup(buffer1_array, buffer1_label)

        buffer1_array1 = VGroup(*[Rectangle(width=1, height=0.5, color = GRAY) for i in range(8)]).arrange(RIGHT, buff = 0.01).next_to(buffer1_array, DOWN, buff = 0)
        buffer1_label1 = Tex("event[1]", color = YELLOW_D).set_z(1).next_to(buffer1_array1, LEFT, 0.2)
        buffer1_label12 = Tex(".data1", color = ORANGE).set_z(1).next_to(buffer1_array1, RIGHT, 0.2)
        buffer1_array1g = VGroup(buffer1_array1, buffer1_label1, buffer1_label12)

        buffer1_array2 = VGroup(*[Rectangle(width=1, height=0.5, color = GRAY) for i in range(8)]).arrange(RIGHT, buff = 0.01).next_to(buffer1_array1, DOWN, buff = 0)
        buffer1_label2 = Tex(".data2", color = ORANGE).set_z(1).next_to(buffer1_array2, RIGHT, 0.2)
        buffer1_array2g = VGroup(buffer1_array2, buffer1_label2)



        #create arrays
        buffer2_array = VGroup(*[Rectangle(width=1, height=0.5, color = GRAY) for i in range(8)]).arrange(RIGHT, buff = 0.01).next_to(buffer1_array2, DOWN, buff = 0.2)
        buffer2_label = Tex(".status", color = ORANGE).set_z(1).next_to(buffer2_array, RIGHT, 0.2)
        buffer2_arrayg = VGroup(buffer2_array, buffer2_label)

        buffer2_array1 = VGroup(*[Rectangle(width=1, height=0.5, color = GRAY) for i in range(8)]).arrange(RIGHT, buff = 0.01).next_to(buffer2_array, DOWN, buff = 0)
        buffer2_label12 = Tex(".data1", color = ORANGE).set_z(1).next_to(buffer2_array1, RIGHT, 0.2)
        buffer2_label1 = Tex("event[2]", color = YELLOW_D).set_z(1).next_to(buffer2_array1, LEFT, 0.2)
        buffer2_array1g = VGroup(buffer2_array1, buffer2_label1, buffer2_label12)

        buffer2_array2 = VGroup(*[Rectangle(width=1, height=0.5, color = GRAY) for i in range(8)]).arrange(RIGHT, buff = 0.01).next_to(buffer2_array1, DOWN, buff = 0)
        buffer2_label2 = Tex(".data2", color = ORANGE).set_z(1).next_to(buffer2_array2, RIGHT, 0.2)
        buffer2_array2g = VGroup(buffer2_array2, buffer2_label2)



        event1 = VGroup(buffer_arrayg, buffer_array1g, buffer_array2g)
        event2 = VGroup(buffer1_arrayg, buffer1_array1g, buffer1_array2g)
        event3 = VGroup(buffer2_arrayg, buffer2_array1g, buffer2_array2g)

        # Add animation to fill each byte in the appropriate array
        byte0 = [1, 0, 0, 1, 0, 0, 0, 0]
        byte0 = [DecimalNumber(digit,num_decimal_places=0)for digit in byte0]
        byte0 = VGroup(*byte0)
        byte0.arrange(RIGHT, buff = 0.81).move_to(buffer_array)
        byte1 = [0, 0, 1, 1, 0, 0, 0, 0]
        byte1 = [DecimalNumber(digit,num_decimal_places=0)for digit in byte1]
        byte1 = VGroup(*byte1)
        byte1.arrange(RIGHT, buff = 0.81).move_to(buffer_array1)
        byte2 = [0, 1, 0, 0, 0, 0, 0, 0]
        byte2 = [DecimalNumber(digit,num_decimal_places=0)for digit in byte2]
        byte2 = VGroup(*byte2)
        byte2.arrange(RIGHT, buff = 0.81).move_to(buffer_array2)

        byte3 = [1, 0, 0, 0, 0, 0, 0, 0]
        byte3 = [DecimalNumber(digit,num_decimal_places=0)for digit in byte3]
        byte3 = VGroup(*byte3)
        byte3.arrange(RIGHT, buff = 0.81).move_to(buffer1_array)
        byte4 = [0, 0, 1, 1, 0, 0, 0, 0]
        byte4 = [DecimalNumber(digit,num_decimal_places=0)for digit in byte4]
        byte4 = VGroup(*byte4)
        byte4.arrange(RIGHT, buff = 0.81).move_to(buffer1_array1)
        byte5 = [0, 0, 0, 0, 0, 0, 0, 0]
        byte5 = [DecimalNumber(digit,num_decimal_places=0)for digit in byte5]
        byte5 = VGroup(*byte5)
        byte5.arrange(RIGHT, buff = 0.81).move_to(buffer1_array2)

        byte6 = [1, 0, 0, 1, 0, 0, 0, 0]
        byte6 = [DecimalNumber(digit,num_decimal_places=0)for digit in byte6]
        byte6 = VGroup(*byte6)
        byte6.arrange(RIGHT, buff = 0.81).move_to(buffer2_array)
        byte7 = [0, 0, 0, 1, 0, 1, 0, 0]
        byte7 = [DecimalNumber(digit,num_decimal_places=0)for digit in byte7]
        byte7 = VGroup(*byte7)
        byte7.arrange(RIGHT, buff = 0.81).move_to(buffer2_array1)
        byte8 = [0, 0, 0, 1, 1, 0, 1, 0]
        byte8 = [DecimalNumber(digit,num_decimal_places=0)for digit in byte8]
        byte8 = VGroup(*byte8)
        byte8.arrange(RIGHT, buff = 0.81).move_to(buffer2_array2)

        self.play(Create(code))
        self.wait(0.1)#1
        self.play(LaggedStart(Create(event1),Create(event2),Create(event3),Create(byte0),Create(byte1),Create(byte2),Create(byte3),
                              Create(byte4),Create(byte5),Create(byte6),Create(byte7),Create(byte8)))
        self.wait(0.1)#3

        # Define the code to display
        code_text1 = '''status_byte = event[2].status'''

        # Create a Code object with the code text
        code2 = Code(code = code_text1, language='c++', font="Consolas",style = "monokai").scale(0.9).shift(UP*2.7)
        byte6c = byte6.copy()
        self.play(ReplacementTransform(code,code2))
        self.wait(0.1)#3
        self.play(Indicate(byte6, 1.1, RED))
        self.wait(0.1)#5
        self.play(FadeTransform(byte6c,code2))
        self.wait(0.1)#5
        






