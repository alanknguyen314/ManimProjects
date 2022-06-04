from manimlib.imports import *
import os
import pyclbr
import numpy as np
import matplotlib.pyplot as plt

class quadratic(Scene):
    def construct(self):

        # Title
        titlep1 = Text("\sqrt{x^2} = |x|")
        self.play(ShowCreationThenFadeOut(titlep1))


