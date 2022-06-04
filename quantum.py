from manimlib import *
from manim import *

####################################################################
# "titre" means "title" in french                                  #
# I hope it's clear, if not you can send me a message              #
####################################################################

class qt(Scene):
    def construct(self):
        title1 = MathTex("\\text{Let's prove that the wave equation has the ability to normalize itself \
             } ax^2+bx+c=0 \\text{ for x}")
        equation1 = MathTex("\\frac{d}{dt}\int_{-\infty}^{+\infty} \! |\\Psi(x, t)|^2 \, \mathrm{d}x")

        self.play(Create(title1))
        self.wait(2)
        self.play(Uncreate(title1),Transform(title1,equation1))