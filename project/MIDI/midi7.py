from manim import *

class anim(Scene):
    def construct(self):

        # Define the code to display
        code_text = '''int __io_putchar(int ch){
    HAL_UART_Transmit(&huart2, (uint8_t *)&ch, sizeof(ch), HAL_MAX_DELAY);
    return ch;
}'''
        # Create a Code object with the code text
        code = Code(code = code_text, language='c++', font="Consolas").scale(0.5)

        # Animate the code (optional)
        self.play(Write(code))

            # Define the code to display
        codet2 = '''void uart_MIDI_RX_callback(void){
	HAL_UART_Receive(&huart1, midi, sizeof(midi), HAL_MAX_DELAY);
}'''

        # Create a Code object with the code text
        code2 = Code(code = codet2, language='c++', font="Consolas").scale(0.5)

        self.wait()#1
        self.play(FadeOut(code))
        self.wait()#3
        self.play(Write(code2))
        self.wait()#5


