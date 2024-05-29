from manim import *

class anim(Scene):
    def construct(self):

        # Create the main rectangle representing the core
        core_rect = Rectangle(width=5, height=4, fill_opacity=0.2, stroke_width=2, color=RED_C)
        core_rect.move_to(ORIGIN).shift(RIGHT*3.5)
        title = Text("ARM Cortex-M4 Core", font_size=36, color=WHITE).next_to(core_rect, UP, buff = 0.2)
        title2 = Text("Nucleo F303K8", font_size=36, color=WHITE).shift(UP*3.5+RIGHT)
        title3 = Text("Outside World", font_size=36, color=WHITE).shift(UP*3.5+LEFT*5)

        # Create the components inside the core
        cpu = Rectangle(width=2, height=1, fill_opacity=0.2, stroke_width=2, color=RED_A)
        cpu.move_to(core_rect.get_center() + np.array([-1.5, 0.5, 0]))
        cpu_label = Tex("CPU", font_size=24, color=WHITE).move_to(cpu)

        fpu = Rectangle(width=2, height=1, fill_opacity=0.2, stroke_width=2, color=RED_A)
        fpu.move_to(core_rect.get_center() + np.array([1.5, 0.5, 0]))
        fpu_label = Tex("FPU", font_size=24, color=WHITE).move_to(fpu)
  
        # Create the peripherals inside the core
        nvic = Rectangle(width=2, height=1, fill_opacity=0.2, stroke_width=2, color=RED_A)
        buss_label = Tex("BUSS", font_size=16, color=WHITE).move_to(core_rect).shift(UP)

        nvic.move_to(core_rect.get_corner(UL) + np.array([1, -0.5, 0]))
        nvic_label = Tex("Interrupt Controller", font_size=16, color=WHITE).move_to(nvic)

        wakeup = Rectangle(width=2, height=1, fill_opacity=0.2, stroke_width=2, color=RED_A)
        wakeup.move_to(core_rect.get_corner(UR) + np.array([-1, -0.5, 0]))
        wakeup_label = Tex("Wake-up Controller", font_size=16, color=WHITE).move_to(wakeup)
        
        empty = Rectangle(width=5, height=2, fill_opacity=0.2, stroke_width=2, color=RED_A)
        empty.move_to(core_rect.get_center()+np.array([0, -1, 0]))
        misc_label = Tex("Lots of complicated stuff we won't worry about..", font_size=16, color=WHITE).move_to(empty)
    
        # Create the additional UART boxes
        uart1 = Rectangle(width=1.5, height=2, fill_opacity=0.2, stroke_width=2, color=TEAL_E)
        uart1.move_to(np.array([-1.25, 1.75, 0]))
        uart1_top_label = Tex("UART1", font_size=16, color=TEAL_B).move_to(uart1.get_center()+np.array([0, +0.5, 0]))
        uart1_rx_label = Tex("Rx Buffer", font_size=16, color=TEAL_B).move_to(uart1.get_center()+np.array([0, -0.25, 0]))
        uart1_tx_label = Tex("Tx Buffer", font_size=16, color=TEAL_B).move_to(uart1.get_center()+np.array([0, -0.75, 0]))
        uart_l1 = Line(start = uart1.get_left(), end = uart1.get_right(), stroke_width=2, color=TEAL_E )
        uart_l2 = Line(start = uart1.get_left()+np.array([0, -0.5, 0]), end = uart1.get_right()+np.array([0, -0.5, 0]), stroke_width=2, color=TEAL_E)

        # Create the additional UART boxes
        uart2 = Rectangle(width=1.5, height=2, fill_opacity=0.2, stroke_width=2, color=TEAL_E)
        uart2.move_to(np.array([-1.25, -1.2, 0]))
        uart2_top_label = Tex("UART2", font_size=16, color=TEAL_B).move_to(uart2.get_center()+np.array([0, +0.5, 0]))
        uart2_rx_label = Tex("Rx Buffer", font_size=16, color=TEAL_B).move_to(uart2.get_center()+np.array([0, -0.25, 0]))
        uart2_tx_label = Tex("Tx Buffer", font_size=16, color=TEAL_B).move_to(uart2.get_center()+np.array([0, -0.75, 0]))
        uart2_l1 = Line(start = uart2.get_left(), end = uart2.get_right(), stroke_width=2 , color=TEAL_E)
        uart2_l2 = Line(start = uart2.get_left()+np.array([0, -0.5, 0]), end = uart2.get_right()+np.array([0, -0.5, 0]), stroke_width=2, color=TEAL_E)

        mline = Line(start = np.array([-3,4,0]),end = np.array([-3,-4,0]), color = GREY).set_z_index(-1)

        g0 = AnimationGroup(Create(core_rect), Write(title), Write(title2), Write(title3))
        g1 = AnimationGroup(Create(nvic), Create(nvic_label), Create(wakeup), Create(wakeup_label))
        g2 = AnimationGroup(Create(cpu), Create(cpu_label), Create(fpu), Create(fpu_label))
        g3 = AnimationGroup(Create(empty),Create(misc_label), Create(buss_label))
        g4 = AnimationGroup(Create(uart1), Create(uart_l1),  Create(uart_l2), Create(uart1_top_label), Create(uart1_rx_label), Create(uart1_tx_label))
        g5 = AnimationGroup(Create(uart2), Create(uart2_l1),  Create(uart2_l2), Create(uart2_top_label), Create(uart2_rx_label), Create(uart2_tx_label))

        self.play(LaggedStart(g0,g1,g2,g3,g4,g5, Create(mline), lag_ratio=0.4, run_time = 5))
        self.wait()#1

        rxne = Line(start = nvic.get_left(), end = uart1.get_right()+np.array([0,-0.25, 0])).set_z_index(-1)
        
        self.play(Create(rxne))
        self.wait()#3

        keyb = ImageMobject("project/MIDI/key.jpg").shift(LEFT*5+UP*2.25).scale(0.3).set_z_index(1)
        pc = ImageMobject("project/MIDI/pc.jpg").shift(LEFT*5+DOWN*0.7).scale(0.3).set_z_index(1)

        kin = Line(start = keyb.get_right(), end = uart1.get_left()+np.array([0,0.5, 0])).set_z_index(-1)
        pin = Line(start = pc.get_right(), end = uart2.get_left()+np.array([0,0.5, 0])).set_z_index(-1)

        self.play(FadeIn(keyb), Create(kin),FadeIn(pc), Create(pin))
        self.wait()#5

        cpurd = Line(start = cpu.get_left(), end = uart1.get_right()+np.array([0,-0.35, 0])).set_z_index(-1)
        cputx = Line(start = cpu.get_left(), end = uart2.get_right()+np.array([0,-0.75, 0])).set_z_index(-1)
        self.play(Create(cpurd),Create(cputx))
        
        self.wait()#7

        binary_digits = [1, 0, 0, 1, 0, 0, 0, 0]
        decimal_digits = [DecimalNumber(digit, num_decimal_places=0) for digit in binary_digits]
        decimal_digits = VGroup(*decimal_digits)
        decimal_digits.move_to(kin.get_start() + [0, 0.25, 0])

        byte1 = [1, 0, 0, 1, 0, 0, 0, 0]
        byte1 = [DecimalNumber(digit, num_decimal_places=0) for digit in byte1]
        byte1 = VGroup(*byte1)
        byte1.arrange(RIGHT, buff=0.05)
        byte1.move_to(uart1.get_center()+np.array([0,-0.25,0])).scale(0.7)

        for digit, byte_index in zip(decimal_digits, range(0, 8)):
            binary_byte = byte1[0:byte_index%8+1]
            self.play(digit.animate.move_to(kin.get_end() + [0, 0.25, 0]),run_time=0.3)
            self.play(binary_byte.animate.set_opacity(1),digit.animate.set_opacity(0), run_time = 0.1)

        self.wait()#24

        self.play(binary_byte.animate.move_to(cpu.get_center()+np.array([0,-0.25, 0]))) 
        self.play(FadeOut(binary_byte))

        self.wait()#27

        binary_data = [0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 
                       0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0]

        byte = [DecimalNumber(digit, num_decimal_places=0) for digit in binary_data]
        byte = VGroup(*byte)
        byte.move_to(cputx.get_start()).scale(0.7)

        for digit in byte:
            self.play(digit.animate.move_to(cputx.get_end() + [0, 0.25, 0]),run_time=0.3)
            self.play(digit.animate.set_opacity(0),run_time=0.05)

        self.wait()

