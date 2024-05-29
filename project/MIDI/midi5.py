from manim import *

class anim(Scene):
    def construct(self):

        keyb = ImageMobject("project/MIDI/key.jpg").shift(LEFT*5+UP*0).scale(0.4).set_z_index(1)
        micro = ImageMobject("project/MIDI/mnobg.png").shift(RIGHT*0+UP*0).scale(0.75).set_z_index(1)
        synth = ImageMobject("project/MIDI/synth.png").shift(RIGHT*5+UP*0).scale(0.9).set_z_index(1)
        line = Line(start = keyb.get_center(), end= synth.get_center())
        
        self.add(keyb, micro, synth, line)
        self.wait()#1

        notes = ['C3','D3','E3','F3','G3','A3','B3','C4']
        notegrp = [Tex(note) for note in notes]
        notegrp = VGroup(*notegrp)
        notegrp.next_to(keyb, RIGHT, buff=0.1).shift([0, 0.25, 0])

        volts = [3,3.166,3.332,3.415,3.581,3.747,3.83,3.913,4]
        voltgrp = [DecimalNumber(volt, num_decimal_places=3) for volt in volts]
        voltgrp = VGroup(*voltgrp)
        voltgrp.next_to(micro, RIGHT, buff=0.1).shift([0, 0.25, 0])

        for note, volt in zip(notegrp, voltgrp):
            self.play(LaggedStart(
                FadeIn(note),
                note.animate.move_to(micro.get_left() + [0, 0.25, 0]),
                FadeIn(volt),
                volt.animate.move_to(synth.get_left() + [-0.4, 0.25, 0]),
                
                lag_ratio=0.8,
                run_time=1  
            ))
            self.play(FadeOut(note, volt))

        self.wait()#9
