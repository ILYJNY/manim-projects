from manimlib import *
import numpy as np

class RectangleExample(Scene):
    def construct(self):
        dx = 0.01
        def func(x):
            return math.sin(x)/x
        while True:
        now_x = 0
        rect1 = Rectangle(width=dx, height=math.fabs(func(now_x)),color=BLUE, fill_opacity=1)
        # self.play(ShowCreation(rect1))
        # rect2 = Rectangle(width=1.0, height=4.0)
        # rect3 = Rectangle(width=2.0, height=2.0)

        rects = Group(rect1, rect2).arrange(buff=1)
        self.add(rects)
        self.play(FadeIn(rects))