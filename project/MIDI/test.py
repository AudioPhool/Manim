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

        # List of styles to loop through
        styles = ["monokai", "manni", "murphy", "vs", "xcode", "fruity", "bw", "colorful", "emacs", "friendly", "native", "paraiso-dark", "paraiso-light", "pastie", "perldoc", "tango", "trac"]

        # Create a list of Code objects
        code_blocks = [Code(code=code_text, language='c++', font="Consolas", style=style).scale(0.1) for style in styles]

        # Group the Code objects into groups of 5
        groups = [code_blocks[i:i+5] for i in range(0, len(code_blocks), 5)]

        # Create a VGroup for each line of code blocks
        lines = [VGroup(*group).arrange(DOWN, buff=0.5) for group in groups]

        # Position the lines on the screen
        for i, line in enumerate(lines):
            line.move_to(3*UP - i*2*DOWN)

        # Add the lines to the scene
        self.add(*lines)
