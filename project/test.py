from manim import*
class anim(Scene):
    def construct(self):
        template = TexTemplate()
        template.add_to_preamble(r"\usepackage[siunitx, RPvoltages, american, europeanresistors]{circuitikz}")

        keyboard = ImageMobject("media/images/mkey.jpg")

        self.play(FadeIn(keyboard))