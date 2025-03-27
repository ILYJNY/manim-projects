from manimlib import *
import numpy as np




class hiworld(Scene):
    def construct(self):#

        text = TexText("""
        $$\int_{-\infty}^{\infty} \\frac{\sin{x}}{x} \,dx = \,?$$\\\\
        """)
        text1 = TexText('''$$\int_{-\infty}^{\infty} \\frac{\sin{x}}{x} \,dx$$\\\\''')
        text2 = TexText('''
                $$\int_{-\infty}^{\infty} \\frac{1}{x}\,\cdot\,\sin{x}$$
                ''')
        text3 = TexText('''
                $$\\frac{1}{x}$$''')
        text4 = TexText('''
                $$ = \int_{0}^{\infty}e^{-xt}\,dt$$''')
        text5 = TexText('$$\\leftarrow \; Laplace \quad Transform$$')
        text6 = TexText('''
                $$\int_{-\infty}^{\infty} \int_{0}^{\infty}\sin{x}\cdot e^{-xt}\,dt \,dx$$
                ''')
        text7 = TexText('''$$\int_{-\infty}^{\infty} \,dt \left(\int_{0}^{\infty}\sin{x}\cdot e^{-xt}\,dx\\right)$$''')
        text8 = TexText('''$$\int_{0}^{\infty}\sin{x}\cdot e^{-xt}\,dx$$''')
        text9 = TexText('''
                $$ e^{ix} = i\sin{x} + \cos{x}, \, \\therefore\, \sin{x} = \\frac{e^{ix}-e^{ix}}{2i}$$
                ''')
        text10 = TexText('''
                $$\\frac{1}{2i} \cdot \int_{0}^{\infty} e^{-xt} \cdot \left(e^{ix} - e^{-ix}\\right) \, dx$$
                ''')
        text11 = TexText('''
                $$\\frac{1}{2i}\cdot$$
                ''')
        text12 = TexText('''
                $$\int_{0}^{\infty}e^{-x(t-i)}\,dx-\int_{0}^{\infty}e^{-x(t+i)}\,dx$$
                ''')
        text13 = TexText('''
                $$by.\; Laplace$$
                ''')
        text14 = TexText('''
                $$^{(t-i)}$$
                ''')
        text15 = TexText('''
                $$^{(t+i)}$$
                ''')
        text16 = TexText('''
                $$\left(\\frac{1}{t-i} - \\frac{1}{t+i}\\right)$$
                ''')
        text17 = TexText('''
                $$\\frac{2i}{t^2 + 1}$$
                ''')
        text18 = TexText('''
                        $$\\frac{1}{t^2 + 1}$$
                        ''')
        text19 = TexText('''
                $$\int_{-\infty}^{\infty} \\frac{1}{t^2 + 1}\,dt$$
                ''')
        text20 = TexText('''
                $$t = \\tan{u}$$
                ''')
        text21 = TexText('''
                $$\\frac{dt}{du} = \sec^2{u}$$
                ''')
        text22 = TexText('''
                $$dt = \sec^2{u}\,du$$
                ''')
        text23 = TexText('''
                $$t \in (-\infty, \infty)\; \\rightarrow \; \\tan{x}\in(-\\frac{\pi}{2}, \\frac{\pi}{2})$$
                ''')
        text24 = TexText('''
                $$\\tan^2{u} + 1 = \sec^2{u}$$
                ''')
        text25 = TexText('''
                $$\int_{-\\frac{\pi}{2}^{\\frac{\pi}{2}}}\\frac{1}{\sec^2{u}}\cdot\sec^2{u}\,du$$
                ''')
        text26 = TexText('''
                $$\int_{-\\frac{\pi}{2}^{\\frac{\pi}{2}}}\,du$$
                ''')
        text27 = TexText('''$$\\frac{\pi}{2} - (-\\frac{\pi}{2})$$''')
        text28 = TexText('''$$\pi$$''')
        text29 = TexText('''$$\sin{x}$$''')
        text30 = TexText('''$$\int_{0}^{\infty}$$''')
        text31 = TexText('''$$\cdot \,e^{-xt}\,dx$$''')
        text32 = TexText('''$$\int_{0}^{\infty}e^{-x}$$''')
        text33 = TexText('''$$\int_{0}^{\infty}e^{-x}$$''')
        text34 = TexText('''$$dx$$''')
        text35 = TexText('''$$dx$$''')
        text36 = TexText('''$$-$$''')
        text38 = TexText('''$$\int_{0}^{\infty}\sin{x}\cdot e^{-xt}\,dx$$''')
        text39 = TexText('''$$\int_{-\infty}^{\infty} \,dt$$''')
        text40 = TexText('''
                $$\\frac{1}{2i}\cdot\left(\int_{0}^{\infty}e^{-x(t-i)}\,dx-\int_{0}^{\infty}e^{-x(t+i)}\,dx\\right)$$
                ''')
        text41 = TexText('''$$by.\; Laplace \quad \\frac{1}{x} = \int_{0}^{\infty}e^{-xt}\,dt$$''')
        sineAxes = Axes(
            x_range=[-10, 10, 1],
            y_range=[-10, 10, 1],
            height=20,
            width=20,
            axis_config={
                "include_tip": False
            },
            y_axis_config={
                "include_tip": False
            }
        )

        Sinx = ParametricCurve(
            lambda u: (1 / 5 * u, 2 * math.sin(u) / u, 0.01),
            t_range=(-100, 100, 0.1),
        )
        # text.scale(2.0)
        # self.play(Write(text))
        # self.wait(0.5)
        # self.play(FadeOut(text),run_time=2)
        #
        # self.clear()
        # text.to_edge(UP)
        # text.scale(0.5)
        # self.play(Write(text),run_time=2)
        #
        #
        #
        # self.play(ShowCreation(sineAxes))
        # self.play(ShowCreation(Sinx))
        # self.wait(1)
        # self.play(FadeOut(sineAxes))
        # self.play(FadeOut(Sinx))
        # self.play(text.animate.scale(2))
        # self.play(text.animate.shift(2*DOWN))
        # #self.play(Write(text))
        # self.play(FadeOut(text),run_time=0.5)
        #
        # #self.play(Write(text1))
        # self.play(Write(text2))
        # text3.scale(1)
        # text3.shift(LEFT*0.201)
        # text3.shift(UP*0.03)
        # self.play(Write(text3),run_time=0.1)
        # self.play(Uncreate(text2))
        # self.play(text3.animate.shift(LEFT*1.5))
        # text4.shift(RIGHT*0.3)
        # self.play(Write(text4))
        # text5.shift(DOWN*1)
        # text5.shift(RIGHT*0.5)
        # text5.scale(0.7)
        # self.play(Write(text5))
        # self.play(Uncreate(text3),Uncreate(text4),Uncreate(text5))
        # self.play(Write(text2))
        # self.play(Uncreate(text2),Write(text6))
        # text8.shift(RIGHT*0.8705)
        self.play(Uncreate(text6), Write(text7),Write(text8))
        self.wait(1)
        self.play(text7.animate.shift(UP*2))
        self.play(text7.animate.scale(0.85))
        self.play(text8.animate.scale(0.9))
        text29.scale(0.9)
        text29.shift(RIGHT*0.47)
        text29.shift(UP*0.03)
        text30.scale(0.9)
        #text30.shift(UP*0.03)
        text31.shift(UP*0.075)
        text31.scale(0.9)
        text31.shift(RIGHT * 1.787)
        text30.shift(LEFT * 0.43)

        self.play(Write(text30),Write(text31),Write(text29),Uncreate(text8))
        self.wait(1)
        text38.scale(0.85)
        text38.shift(UP*2)
        text38.shift(RIGHT*0.72)
        text39.scale(0.85)
        text39.shift(UP * 2)
        text39.shift(LEFT*1.9)
        self.play(Write(text38),Write(text39),Uncreate(text7))
        self.play(text29.animate.set_color(RED))
        self.wait(1)
        self.play(Uncreate(text31),Uncreate(text30))
        self.play(text29.animate.shift(LEFT * 0.47))
        self.play(text29.animate.shift(DOWN * 0.03))
        self.play(text29.animate.scale(1))
        self.play(text29.animate.set_color(WHITE))
        self.play(text29.animate.shift(UP*1))
        self.play(Write(text9))
        self.wait(1)
        self.play(Uncreate(text29),Uncreate(text9),Write(text10))
        self.wait(1)
        self.play(Write(text12),Uncreate(text10))
        self.wait(1)
        text14.shift(UP*0.163)
        text14.shift(LEFT*1.35)
        text15.shift(UP * 0.163)
        text15.shift(RIGHT * 2.42)
        text33.shift(LEFT * 2.65)
        text32.shift(RIGHT * 1.15)
        text34.shift(RIGHT * 3.23)
        text34.shift(UP * 0.045)
        text35.shift(LEFT * 0.55)
        text35.shift(UP * 0.045)
        self.play(Write(text35),Write(text34),Write(text32),Write(text33),Write(text15),Write(text14),Write(text36))
        self.wait(1)
        self.play(Uncreate(text12))
        self.wait(1)
        self.play(text14.animate.set_color(BLUE),text15.animate.set_color(BLUE))
        text40.scale(0.85)
        text40.shift(RIGHT * 1)
        text40.shift(UP * 2)
        self.play(text39.animate.shift(LEFT*1.9),Uncreate(text38),Write(text40))
        self.wait(1)
        text41.to_edge(DOWN)
        text41.scale(0.8)
        self.play(Write(text41))
        self.wait(1)
        self.play(Uncreate(text41))
        self.play(FadeOut(text32),FadeOut(text33),FadeOut(text34),FadeOut(text35),FadeOut(text36))
        self.play(Write(text16))
        self.play(text14.animate.scale(1))
        self.play(text15.animate.scale(1))










#
# class GraphSceneTest(Scene):
#     def construct(self):
#         def func(x):
#             return math.sin(x)/x
#
#         graph = self.get_(func, x_min=-100, x_max=100)
#         graph.set_color(WHITE)
#         def rect(x):
#             return x
#         recta=self.get_graph(rect, x_min=-100, x_max=100)
#         kwargs = {
#             "x_min" : -100,
#             "x_max" : 100,
#             "fill_opacity" : 0.1,
#             "stroke_width" : 0.1,
#
#         }
#         self.graph=graph
#         iteraciones=6
#         self.rect_list = self.get_reimann_rectangles_list(
#             graph,iteraciones,start_color=BLUE,end_color=BLUE,**kwargs
#         )
#         flat_rects = self.get_reimann_rectangles(
#             self.get_graph(lambda x: -10), dx=0.01, start_color=BLUE, end_color=BLUE, **kwargs
#         )
#         rects = self.rect_list[0]
#         self(
#             flat_rects, rects,
#             replace_mobject_with_target_in_scene = True,
#             run_time = 0.1
#         )
