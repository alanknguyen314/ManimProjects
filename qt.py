from multiprocessing.connection import wait
from manimlib import *
from manim import *

####################################################
# Name: Alan K. Nguyen 


class qt(Scene):
    def construct(self):
        title1 = MathTex(" \\text{\\justifying{ Let's prove that the wave equation has the ability to normalize itself").scale_to_fit_width(12)
        title2 = MathTex("\\text{Let's begin with this equality:}").to_edge(UP).scale(0.7).align_on_border(LEFT)
        equation1 = MathTex("\\frac{d}{dt}\int_{-\infty}^{+\infty} |\\Psi(x, t)|^2dx = \\int_{-\infty}^{+\infty} \\frac{\partial}{\partial t}|\\Psi(x, t)|^2dx.").next_to(title2,DOWN).scale(0.7).align_on_border(LEFT)
        text11 = MarkupText(
            f'all in red <span fgcolor="{YELLOW}">except this</span>', color=RED
        ).next_to(equation1, DOWN).scale(0.4).align_on_border(LEFT)
        text12 = MathTex("\\text{I use a full derivative in the LHS because the integral is only a function of t.}").next_to(text11, DOWN).scale(0.4).align_on_border(LEFT)
        text13 = MathTex("\\text{However, a partial derivative is used in the RHS because the probability density is a function of both t and x.}").next_to(text12, DOWN).scale(0.4).align_on_border(LEFT)

        equation2 = MathTex("\\text{(1)}\\frac{\partial}{\partial t} (|\Psi|^2) = \\frac{\partial}{\partial t}(\Psi \Psi^*) = \Psi^*\\frac{\partial \Psi}{\partial t} + \Psi\\frac{\partial \Psi^*}{\partial t}").next_to(text13, DOWN).scale(0.7).align_on_border(LEFT)
        equation3 = MathTex("\\text{(2)}\\frac{\partial \Psi}{\partial t} = \\frac{i\hbar}{2m}\\frac{\partial^2\Psi}{\partial x^2} - \\frac{i}{\hbar}V \Psi.").next_to(equation2, DOWN).scale(0.7).align_on_border(LEFT)
        



        self.play(Create(title1))
        #self.wait(2)
        self.play(Transform(title1, title2))
        self.play(Create(equation1))
        self.play(Create(text11))
        self.play(Create(text12))
        self.play(Create(text13))

        #self.wait(3)
        self.play(Create(equation2))
        #self.wait(2)
        self.play(Create(equation3))


