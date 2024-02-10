from manim import *
import numpy as np

class Intro(Scene):
    def construct(self):

        #Quote shared in private conversation with Ben in Perimeter Institute circa 2013. 
        
        Quote1 = Tex(r"`If you want to understand the universe, study physics.")
        Quote2 = Tex(r"If you want to understand physics, study philosophy.'")
        Author = Tex(r'--Lee Smolin')
        Smolin = ImageMobject("media\images\external_images\LeeSmolinAtHarvard.jpg").scale(2)

        #Why do I need to use different quotation marks for opening and closing?

        Quote1.shift(UP*3)
        Quote2.next_to(Quote1, DOWN*.5)
        Author.next_to(Quote2, DOWN)
        Smolin.next_to(Author, DOWN)

        self.play(Succession(
            FadeIn(Quote1, run_time = 2),
            FadeIn(Quote2, run_time = 3),
            FadeIn(Author, Smolin, run_time = 1)), 
            )
        self.wait(2)

        Nobel_image = ImageMobject(r"media\images\external_images\nobel_2022.png") #Nobel prize winners
        Nobel_quote1 = Tex(r"`for experiments with entangled photons, ")
        Nobel_quote2 = Tex(r"establishing the violation of Bell inequalities'") 

        Nobel_image.shift(UP)
        Nobel_quote1.next_to(Nobel_image, DOWN)
        Nobel_quote2.next_to(Nobel_quote1, DOWN*.5)

        Nobel_quote = VGroup(Nobel_quote1, Nobel_quote2)

        self.play(Succession(
            FadeOut(Quote1, Quote2, Author, Smolin),
            FadeIn(Nobel_quote, Nobel_image)), 
            run_time = 2)
        self.wait(20)

        Telephone1 = Tex("Quantum Mechanics", " disproves", " Local", " Causality").next_to(Nobel_image, DOWN)
        Telephone2 = Tex("Quantum Mechanics", " disproves", " Local", " Real", "ism").next_to(Nobel_image, DOWN)
        Telephone3 = Tex("Quantum Mechanics", " disproves", " Real", "ism").next_to(Nobel_image, DOWN)
        Telephone4 = Tex("Quantum Mechanics", " shows universe isn't", " Real").next_to(Nobel_image, DOWN)
        Telephone5 = Tex("We live in a simulation").next_to(Nobel_image, DOWN)

        self.play(ReplacementTransform(Nobel_quote, Telephone1))
        self.wait(5.5)

        self.play(TransformMatchingTex(Telephone1, Telephone2))
        self.wait(1)

        self.play(TransformMatchingTex(Telephone2, Telephone3))
        self.wait(2.5)

        self.play(TransformMatchingTex(Telephone3, Telephone4))
        self.wait(2.5)

        self.play(Transform(Telephone4, Telephone5))
        self.wait(1)

class Outline(Scene):
    def construct(self):

        Section1 = Tex(r"Section 1").shift(UP*3)
        ul1 = Underline(Section1)
        Text1 = Tex(r"Defining philosophy terms").next_to(Section1, DOWN)
        Group1 = VGroup(Section1, ul1, Text1)
        

        Section2 = Tex(r"Section 2").next_to(Text1, DOWN*5)
        ul2 = Underline(Section2)
        Text2 = Tex(r"GHZ proof").next_to(Section2, DOWN)
        Group2 = VGroup(Section2, ul2, Text2)

        self.play(FadeIn(Group1))
        self.wait(5)
        self.play(FadeIn(Group2))
        self.wait(5)

class Locality(Scene):
    def construct(self):

        Title1 = Tex(r'Locality').to_edge(UP)
        ul1 = Underline(Title1)
        Definition1 = Tex(r'No object can move faster than light').next_to(Title1, DOWN)

        Locality = VGroup(Title1, ul1, Definition1)
        
        self.play(Write(Locality))
        self.wait(2)
        
        sine = lambda t: .5 * np.sin(12*t) #function for photon to trace out

        sin_path = FunctionGraph(
        sine,
        x_range= [-2*PI,2*PI],
        ).shift(UP)

        photon = Dot(color=YELLOW).shift(UP)

        curve = always_redraw(lambda: FunctionGraph(
        sine,
        color=YELLOW,
        x_range= [photon.get_center()[0] - .25, photon.get_center()[0] + .25],
        ).shift(UP)) #redraw photon curve every frame to be only part of the sine graph

        Mass = Dot(color = BLUE).shift(DOWN)
        Mass.shift([-2*PI, 0, 0])
        Mass.add_updater(lambda mob, dt: mob.shift(1.2*dt*RIGHT))

        self.add(photon, curve, Mass)
        self.play(
            MoveAlongPath(photon, sin_path,  rate_func = linear),
            run_time = 10,)
        
        self.play(FadeOut(Mass,photon,curve), 
                  run_time = .1)
        self.wait(5)
            

class Newton(Scene):
    def construct(self):

        Newton_quote1 = Text(r"`It is inconceivable that inanimate Matter should, without the Mediation of something else, ") 
        Newton_quote2 = Text(r'which is not material, operate upon, and affect other matter without mutual Contact…')
        Newton_quote3 = Text(r'That Gravity should be innate, inherent and essential to Matter, so that one body may ')
        Newton_quote4 = Text(r'act upon another at a distance thro’ a Vacuum, without the Mediation of any thing else, ')
        Newton_quote5 = Text(r'by and through which their Action and Force may be conveyed from one to another, ')
        Newton_quote6 = Text(r'is to me so great an Absurdity that I believe no Man who has in philosophical Matters ')
        Newton_quote7 = Text(r"a competent Faculty of thinking can ever fall into it. Gravity must be caused by an Agent ")
        Newton_quote8 = Text(r"acting constantly according to certain laws; but whether this Agent be material or immaterial, ")
        Newton_quote9 = Text(r"I have left to the Consideration of my readers' ")
        Newton_quote10 = Text(r'-- Isaac Newton (1692/3)')

        Newton_quote = VGroup(Newton_quote1,
                              Newton_quote2,
                              Newton_quote3,
                              Newton_quote4,
                              Newton_quote5,
                              Newton_quote6,
                              Newton_quote7,
                              Newton_quote8, 
                              Newton_quote9,
                              Newton_quote10,
                              )
        
        Newton_quote.shift(UP*2)
        Newton_quote.arrange(DOWN)
        Newton_quote.scale(.4)


        Earth = Circle(radius = 1/4, color = GREEN).shift(DOWN*3)
        Moon = Circle(radius = 1/16, color = GRAY).shift(DOWN*3)

        Earth.set_fill(GREEN, opacity= 1)
        Moon.set_fill(GRAY, opacity= 1)
        
        Earth.shift(LEFT*3)
        Moon.shift(RIGHT*3)
    
        self.play(
        Succession(
            AddTextLetterByLetter(Newton_quote1),
            AddTextLetterByLetter(Newton_quote2),
            AddTextLetterByLetter(Newton_quote3),
            AddTextLetterByLetter(Newton_quote4),
            AddTextLetterByLetter(Newton_quote5),
            AddTextLetterByLetter(Newton_quote6),
            AddTextLetterByLetter(Newton_quote7),
            AddTextLetterByLetter(Newton_quote8),
            AddTextLetterByLetter(Newton_quote9),
            AddTextLetterByLetter(Newton_quote10),), #wanted to add text word by word, but function is known to be glitched 
        Succession(
            FadeIn(Earth, Moon),
            Earth.animate.shift(LEFT*2),
            Indicate(Moon),
            Moon.animate.shift(LEFT*2)),
        run_time = 10)
        self.wait(18)

class Arcs(Scene):
    def construct(self):
        
        def signal():
            arc = Arc(radius = 6, start_angle=-.4, angle=0.8, arc_center=[-8, 0., 0.], color = BLUE)
            arc.add_updater(lambda mob, dt: mob.shift(1.5*RIGHT*dt))
            return arc #create wave moving to the right
        
        Earth = Circle(radius = 1/4, color = GREEN).shift(LEFT*3)
        Moon = Circle(radius = 1/16, color = GRAY).shift(RIGHT*3)


        Earth.set_fill(GREEN, opacity= 1)
        Moon.set_fill(GRAY, opacity= 1)
        self.play(FadeIn(Earth, Moon))
        self.wait(3)

        self.play(FadeIn(signal()))
        self.wait(2.4)
        self.play(Indicate(Moon))
        self.play(Moon.animate.shift(LEFT), run_time = 5)

        detector = Triangle().scale(1/16)
        detector.set_fill(YELLOW)
        detector.shift(RIGHT)

        self.play(FadeIn(detector), run_time = 3)
        self.play(FadeIn(signal()))
        self.wait(1)
        self.play(Indicate(detector))
        self.play(Indicate(Moon))
        self.play(Moon.animate.shift(LEFT), run_time = 5)


class Action(Scene):
    def construct(self):
        Title1 = Tex(r'Locality').to_edge(UP)
        ul1 = Underline(Title1)
        Definition1 = Tex(r'No object can move faster than light').next_to(Title1, DOWN)
        Locality = VGroup(Title1, ul1, Definition1)

        self.add(Locality)
        
        Title2 = Tex(r'No Action at a Distance').next_to(Locality, DOWN*3)
        ul2 = Underline(Title2)
        Definition2 = Tex(r'Interactions must be mediated through a physical signal').next_to(Title2, DOWN)
        NAAAD = VGroup(Title2, ul2, Definition2)

        self.play(Write(NAAAD), run_time = 2)
        self.wait(8)

class Action2(Scene):
    def construct(self):
        
        Title1 = Tex(r'Locality').to_edge(UP)
        ul1 = Underline(Title1)
        Definition1 = Tex(r'No object can move faster than light').next_to(Title1, DOWN)
        Locality = VGroup(Title1, ul1, Definition1)

        self.add(Locality)
        
        Title2 = Tex(r'No Action at a Distance').next_to(Locality, DOWN*3)
        ul2 = Underline(Title2)
        Definition2 = Tex(r'Interactions must be mediated through a physical signal').next_to(Title2, DOWN)
        NAAAD = VGroup(Title2, ul2, Definition2)

        self.add(NAAAD)

class Real_VD(Scene):
    def construct(self):

        Title1 = Tex(r'Realism').to_edge(UP)
        ul1 = Underline(Title1)
        Definition1 = Tex(r"External Reality exists independently of one's perceptions").next_to(Title1, DOWN)
        Realism = VGroup(Title1, ul1, Definition1)

        self.play(Write(Realism))
        self.wait(20)

class Real_VD2(Scene):
    def construct(self):
        
        Title1 = Tex(r'Realism').to_edge(UP)
        ul1 = Underline(Title1)
        Definition1 = Tex(r"External Reality exists independently of one's perceptions").next_to(Title1, DOWN)
        Realism = VGroup(Title1, ul1, Definition1)

        Strike_Through1 = Line(start = Title1.get_left(), end = Title1.get_right(), color = RED)
        Strike_Through2 = Line(start = Definition1.get_left(), end = Definition1.get_right(), color = RED)

        self.add(Realism)
        self.wait(10)

        Title2 = Tex(r'Value Definiteness').next_to(Realism, DOWN*3)
        ul2 = Underline(Title2)
        Definition2 = Tex(r"Measurements reveal pre-existing properties").next_to(Title2, DOWN)
        VD = VGroup(Title2, ul2, Definition2)

        self.play(Write(VD), Write(Strike_Through1), Write(Strike_Through2))
        self.wait(10)


class Weight(Scene):
    def construct(self):

        head = Circle(radius=.4, color = WHITE)
        body = Line(start = head.get_bottom(), end = head.get_bottom() - [0, 1, 0])
        arms = Line(start = (1/3)*(2*body.get_top() + body.get_bottom()) - [.5, 0, 0], end = (1/3)*(2*body.get_top() + body.get_bottom()) - [-.5, 0, 0]) 
        left_leg = Line(start = body.get_bottom() , end = body.get_bottom() - [.5, .5, 0])
        right_leg = Line(start = body.get_bottom() , end = body.get_bottom() - [-.5, .5, 0]) 

        Me = VGroup(head, body, arms, left_leg, right_leg)
        Me.shift(LEFT*2)
        Me.scale(1) #it's me, but with less hair
        
        Scales = Square(side_length=1.75*2)
        Window = Rectangle(height = .25*2, width = .5*2).next_to(Scales, UP)
        Scales_group = VGroup(Scales, Window)
        Scales_group.shift(RIGHT+DOWN*.5)


        self.play(FadeIn(Me))
        self.play(FadeIn(Scales_group))
        self.play(Me.animate.shift(RIGHT*3))

        Reading = MathTex("150", color = YELLOW)
        Reading.move_to(Window.get_center())
        Reading.scale(1)
        Reading2 = MathTex("150", color = YELLOW)
        Reading2.next_to(Me, RIGHT)

        self.play(FadeIn(Reading))
        self.wait(10)

        c = Circle(radius = 2)
        c.move_to(Me.get_center())
        angles = [n * (360 / 8) for n in range(8)]
        points = [c.point_at_angle(n*DEGREES) for n in angles]
        circles = [Dot(color=YELLOW, fill_opacity=1).move_to(p) for p in points] # points arranged in a circle around me


        self.play(FadeOut(Reading), run_time = .5)
        self.play(FadeIn(*circles))
        self.play(
            *[d.animate.move_to(Me.get_center()) for d in circles],
            )
        self.play(FadeIn(Reading, Reading2), Reading2.animate.shift(UP*.25), FadeOut(*circles))
        self.wait(6)

class Classical(Scene):
    def construct(self):

        Title1 = Tex(r'Locality').to_edge(UP)
        ul1 = Underline(Title1)
        Definition1 = Tex(r'No object can move faster than light').next_to(Title1, DOWN)
        Locality = VGroup(Title1, ul1, Definition1)

        

        Title2 = Tex(r'Value Definiteness').next_to(Locality, DOWN*3)
        ul2 = Underline(Title2)
        Definition2 = Tex(r"Measurements reveal pre-existing properties").next_to(Title2, DOWN)
        VD = VGroup(Title2, ul2, Definition2)

        self.play(Write(Locality), Write(VD), run_time=2)

        classical = Tex(r'Classical = {{Locality}} + {{Value Definiteness}}')
        self.play(
            TransformMatchingTex(Group(Title1, Title2), classical),
            FadeOut(ul1, Definition1, ul2, Definition2),
            run_time = 4)
        
class SG_1(ThreeDScene): 
    def construct(self):

        phi, *_ = self.camera.get_value_trackers()

        sphere = Sphere()
        sphere.set_color(WHITE)
        sphere.set_opacity(.1)

        self.play(Write(sphere))
        self.play(Rotating(sphere,axis = RIGHT, radians = PI/2), run_time = 1) #I need to run this animation for every scene, possible glitch?
        self.play(phi.animate.set_value(-.3)) 

        vec = Vector([0,.5,0])
        vec.next_to(sphere,UP,0)
        
        self.wait(3)

        self.play(Write(vec), run_time = 3)
        
        self.wait(.5)

        Stern = VGroup(sphere, vec)
        self.play(Stern.animate.shift(2*RIGHT))

        ball = Sphere(center=(0,0,0), radius=.125)
        ball.set_color(RED)
        ball.next_to(Stern,LEFT,0)
        ball.shift(3*LEFT)
        self.add(ball)

        self.play(ball.animate.move_to(sphere.get_center()), run_time = 2)
        self.wait(1)
        self.play(ball.animate.shift(UP*3))
        new_ball = ball.copy()
        new_ball.shift(DOWN*3)
        self.play(FadeOut(ball), FadeIn(new_ball))
        self.play(new_ball.animate.shift(DOWN*3))
        self.wait(8)

        State = MathTex(r"\vert \! Spin State \rangle = a \vert \! \uparrow \rangle + b \vert \! \downarrow \rangle")
        State.shift((LEFT*3+UP))

        Probabilities = MathTex(r"Prob(\uparrow) &= a^2\\ Prob(\downarrow) &= b^2")
        Probabilities.shift(LEFT*3+DOWN)

        self.play(Write(State), run_time = 3)
        self.wait(4)
        self.play(Write(Probabilities))
        self.wait(6)

        self.play(FadeOut(Probabilities, State, new_ball), run_time = 2)
        self.play(Rotate(Stern, angle = PI))

        opp_ball = ball = Sphere(center=sphere.get_center(), radius=.125)
        opp_ball.set_color(RED)
        self.play(FadeIn(opp_ball))

        Text_1 = Tex(r"This electron is deflecting")
        Text_2 = Tex(r"UPWARDS!") #Surprisingly contentious claim, but it is correct according to the Feynman Lectures Section III_06

        Text_up = VGroup(Text_1, Text_2).arrange(DOWN)

        Text_up.shift(LEFT*3)

        self.play(opp_ball.animate.shift(DOWN*3), Write(Text_up))
        self.wait(3)

        

class SG_2(ThreeDScene): #Scene may be too long. May not need to be ThreeDScene
    def construct(self):

        sphere = Sphere()
        sphere.set_color(WHITE)
        sphere.set_opacity(.1)

        self.play(Rotating(sphere,axis = RIGHT, radians = PI/2), run_time = .1) #I dont want to play this, but otherwise it doesnt work

        vec = Vector([0,.5,0])
        vec.next_to(sphere,UP,0)
        
        Stern_1 = VGroup(sphere, vec)
        Stern_2 = Stern_1.copy()
        
        Stern_1.shift(LEFT*3+DOWN)
        Stern_2.shift(RIGHT*3+DOWN)

        State_1 = MathTex(r"{{\vert}}{{ \! State \: 1}} {{\rangle}}{{ =  }}{{\frac{1}{\sqrt{2}}}}{{(\vert \! \uparrow \rangle}}{{ + }}{{\vert \! \downarrow \rangle}}{{)}}").scale(.5)
        State_2 = MathTex(r"{{\vert}}{{ \! State \: 2}} {{\rangle}}{{ =  }}{{\frac{1}{\sqrt{2}}}}{{(\vert \! \uparrow \rangle}}{{ - }}{{\vert \! \downarrow \rangle}}{{)}}").scale(.5)

        State_1.shift(LEFT*3+UP*3)
        State_2.shift(RIGHT*3+UP*3)

        Probability_1 = MathTex(r"Prob({{\uparrow}}) &= \frac{1}{2}\\ Prob({{\downarrow}}) &= \frac{1}{2}").scale(.5)
        Probability_2 = MathTex(r"Prob({{\uparrow}}) &= \frac{1}{2}\\ Prob({{\downarrow}}) &= \frac{1}{2}").scale(.5)

        Probability_1z = MathTex(r"Prob({{\uparrow}}{{in \: z}}) &= \frac{1}{2}\\ Prob({{\downarrow}}{{in \: z}}) &= \frac{1}{2}").scale(.5)
        Probability_2z = MathTex(r"Prob({{\uparrow}}{{in \: z}}) &= \frac{1}{2}\\ Prob({{\downarrow}}{{in \: z}}) &= \frac{1}{2}").scale(.5)

        Probability_1x = MathTex(r"Prob({{\uparrow}}{{in \: x}}) &= 1\\ Prob({{\downarrow}}{{in \: x}}) &= 0").scale(.5)
        Probability_2x = MathTex(r"Prob({{\uparrow}}{{in \: x}}) &= 0\\ Prob({{\downarrow}}{{in \: x}}) &= 1").scale(.5)

        Probability_1.shift(LEFT*3+UP*2)
        Probability_2.shift(RIGHT*3+UP*2)

        Probability_1z.shift(LEFT*3+UP*2)
        Probability_2z.shift(RIGHT*3+UP*2)

        Probability_1x.shift(LEFT*3+UP)
        Probability_2x.shift(RIGHT*3+UP)

        self.play(FadeIn(Stern_1, Stern_2, State_1, State_2))
        self.wait(4)
        self.play(Circumscribe(State_1[-3]), run_time = 1)
        self.play(Circumscribe(State_2[-3]), run_time = 1)

        class Electron(Sphere):
            def __init__(self, center, color = RED, radius = .125):
                super().__init__(
                    radius = radius,
                    color = color,
                    center = center,
                )

                
        
        for n in range(4):
            
            e1, e2 = Electron(center = sphere.get_center()), Electron(center = 6*RIGHT + sphere.get_center())
            e1.set_color(RED)
            e2.set_color(RED)
            self.play(FadeIn(e1, e2))

            if n%2 == 0:
                self.play(e1.animate.shift(UP*2), e2.animate.shift(UP*2), run_time = .5)

            else:
                self.play(e1.animate.shift(DOWN*2), e2.animate.shift(DOWN*2), run_time = .5)

            self.play(FadeOut(e1, e2), run_time = .125)


        self.play(Write(Probability_1), Write(Probability_2))
        self.wait(6)

        State_1z = MathTex(r"{{\vert}}{{ \! State \: 1}} {{\rangle}}{{ =  }}{{\frac{1}{\sqrt{2}}}}{{(\vert \! \uparrow \rangle}}{{_z}}{{ + }}{{\vert \! \downarrow \rangle}}{{_z}}{{)}}").scale(.5)
        State_2z = MathTex(r"{{\vert}}{{ \! State \: 2}} {{\rangle}}{{ =  }}{{\frac{1}{\sqrt{2}}}}{{(\vert \! \uparrow \rangle}}{{_z}}{{ - }}{{\vert \! \downarrow \rangle}}{{_z}}{{)}}").scale(.5)

        State_1x = MathTex(r"{{\vert}}{{\uparrow}} {{\rangle}}_x{{ =  }}{{\frac{1}{\sqrt{2}}}}{{(\vert \! \uparrow \rangle}}{{_z}}{{ + }}{{\vert \! \downarrow \rangle}}{{_z}}{{)}}").scale(.5)
        State_2x = MathTex(r"{{\vert}}{{\downarrow}} {{\rangle}}_x{{ =  }}{{\frac{1}{\sqrt{2}}}}{{(\vert \! \uparrow \rangle}}{{_z}}{{ - }}{{\vert \! \downarrow \rangle}}{{_z}}{{)}}").scale(.5)

        State_1z.shift(LEFT*3+UP*3)
        State_2z.shift(RIGHT*3+UP*3)

        State_1x.shift(LEFT*3+UP*3)
        State_2x.shift(RIGHT*3+UP*3)
        
        self.play(TransformMatchingTex(State_1, State_1z), TransformMatchingTex(State_2, State_2z))
        self.wait(3)

        self.play(Rotate(Stern_1, angle = -PI/2), Rotate(Stern_2, angle = -PI/2))
        
        for n in range(4):
            
            e1, e2 = Electron(center = sphere.get_center()), Electron(center = 6*RIGHT + sphere.get_center())
            e1.set_color(RED)
            e2.set_color(RED)
            self.play(FadeIn(e1, e2))

            self.play(e1.animate.shift(RIGHT*2), e2.animate.shift(LEFT*2))
            self.play(FadeOut(e1, e2), run_time = .125)
        self.wait(5)

        self.play(TransformMatchingTex(Probability_1, Probability_1z), TransformMatchingTex(Probability_2, Probability_2z))

        self.play(Write(Probability_1x), Write(Probability_2x))
        self.wait(5)

        self.play(TransformMatchingTex(State_1z, State_1x), TransformMatchingTex(State_2z, State_2x))
        self.wait(20)
        self.play(FadeOut(Probability_1z, Probability_2z,
                          Probability_1x, Probability_2x,
                          State_1x, State_2x))
        self.wait(10)

class SG_4(ThreeDScene): #SG_3 keeps glitching because it cant read previous partial movie files
    def construct(self):

        sphere = Sphere()
        sphere.set_color(WHITE)
        sphere.set_opacity(.1)

        self.play(Rotating(sphere,axis = RIGHT, radians = PI/2))

        vec = Vector([0,.5,0])

        self.add_fixed_in_frame_mobjects(vec) #Slows down rendering too much
        vec.next_to(sphere,UP,0)
        
        Stern_1 = VGroup(sphere, vec)
        Stern_2 = Stern_1.copy()

        Stern_1.shift(LEFT*3+DOWN)
        Stern_2.shift(RIGHT*3+DOWN)

        self.add_fixed_orientation_mobjects(Stern_1, Stern_2) #Extremely slow, but devices are not aligned otherwise. Change ThreeDScene to Scene?

        self.play(Rotate(Stern_1, angle = -PI/2), Rotate(Stern_2, angle = -PI/2))
        self.wait(4)

        self.play(Rotate(Stern_1, angle = -PI/2 - .1 , axis = UP), Rotate(Stern_2, angle = -PI/2 - .1, axis = UP))

        ball_1 = Sphere(center= sphere.get_center(), radius=.125)
        ball_1.set_color(RED)

        ball_2 = Sphere(center= sphere.get_center() + 6 * RIGHT, radius=.125)
        ball_2.set_color(RED)

        self.play(FadeIn(ball_1, ball_2))
        self.play(ball_1.animate.shift([-.5,0,2]), ball_2.animate.shift([.5,0,-2]))
        self.play(FadeOut(ball_1, ball_2))

        State_1 = MathTex(r"\vert \uparrow \rangle_y=  \frac{1}{\sqrt{2}}(\vert \! \uparrow \rangle_z + {{i}}{{ * \vert \! \downarrow \rangle_z)}}").scale(.5)
        State_2 = MathTex(r"\vert \downarrow \rangle_y =  \frac{1}{\sqrt{2}}(\vert \! \uparrow \rangle_z - {{i}}{{ * \vert \! \downarrow \rangle_z)}}").scale(.5)

        State_1.shift(LEFT*3+UP*3)
        State_2.shift(RIGHT*3+UP*3)

        self.wait(10)

        self.play(Write(State_1), Write(State_2))
        self.wait(10)
        self.play(Circumscribe(State_1[-2]), Circumscribe(State_2[-2]))
        self.wait(10)

class SG_5(Scene):
    def construct(self):

        Eqs =MathTex(r"{{\vert \! \uparrow \rangle}}{{_x}} &= {{\frac{1}{\sqrt{2}}}}({{\vert \! \uparrow \rangle}}{{_z}} + {{\vert \! \downarrow \rangle}}{{_z}}) \\ \
        {{\vert \! \downarrow \rangle}}{{_x}} &= {{\frac{1}{\sqrt{2}}}}({{\vert \! \uparrow \rangle}}{{_z}} - {{\vert \! \downarrow \rangle}}{{_z}}) \\ \
        {{\vert \! \uparrow \rangle}}{{_y}} &= {{\frac{1}{\sqrt{2}}}}({{\vert \! \uparrow \rangle}}{{_z}} +{{ i *}}{{ \vert \! \downarrow \rangle}}{{_z}}) \\ \
        {{\vert \! \downarrow \rangle}}{{_y}} &= {{\frac{1}{\sqrt{2}}}}({{\vert \! \uparrow \rangle}}{{_z}} - {{i * }}{{\vert \! \downarrow \rangle}}{{_z)}}").scale(.5)


        self.play(FadeIn(Eqs))
        self.wait(2)

        Eqs_2 =MathTex(r"{{\vert \! \uparrow \rangle}}{{_z}} &= {{\frac{1}{\sqrt{2}}}}({{\vert \! \uparrow \rangle}}{{_x}} + {{\vert \! \downarrow \rangle}}{{_x}}) \\ \
        {{\vert \! \downarrow \rangle}}{{_z}} &= {{\frac{1}{\sqrt{2}}}}({{\vert \! \uparrow \rangle}}{{_x}} - {{\vert \! \downarrow \rangle}}{{_x}}) \\ \
        {{\vert \! \uparrow \rangle}}{{_z}} &= {{\frac{1}{\sqrt{2}}}}({{\vert \! \uparrow \rangle}}{{_y}} + {{\vert \! \downarrow \rangle}}{{_y}}) \\ \
        {{\vert \! \downarrow \rangle}}{{_z}} &= {{\frac{1}{\sqrt{2}}}}{{ * i}}({{\vert \! \downarrow \rangle}}{{_y}} - {{\vert \! \uparrow \rangle}}{{_y}})").scale(.5)

        self.play(TransformMatchingTex(Eqs, Eqs_2), run_time = 6)
        self.wait(10)

class Hist_1(Scene):
    def construct(self):

        einstein = ImageMobject(r"media\images\external_images\Einstein_1921_by_F_Schmutzer_-_restoration.jpg") 
        bohm = ImageMobject(r"media\images\external_images\David_Bohm.jpg")
        bohr = ImageMobject(r"media\images\external_images\Niels_Bohr.jpg")
        neumann = ImageMobject(r"media\images\external_images\JohnvonNeumann-LosAlamos.gif")

        einstein.scale(.25)

        bohm.height  = bohr.height = neumann.height = einstein.height #Why are they not exactly the same height???
        bohm.width = bohr.width = neumann.width = einstein.width 

        HV_title = Tex("Hidden Variables").shift(LEFT*3+UP*2)
        HV_ul = Underline(HV_title)

        self.play(Write(VGroup(HV_title,HV_ul)))

        nHV_title = Tex("Quantum Randomness").shift(RIGHT*3+UP*2)
        nHV_ul = Underline(nHV_title)

        self.play(Write(VGroup(nHV_title, nHV_ul)))
        self.wait(5)

        HV_people = Group(einstein, bohm).arrange(RIGHT).next_to(HV_ul, DOWN)
        nHV_people = Group(neumann, bohr).arrange(RIGHT).next_to(nHV_ul, DOWN)

        self.play(FadeIn(HV_people))
        self.wait(20)
        self.play(FadeIn(nHV_people))
        self.wait(20)

class Hist_2(Scene):
    def construct(self):

        sphere = Sphere()
        sphere.set_color(WHITE)
        sphere.set_opacity(.1)

        self.play(Rotate(sphere,axis = RIGHT, angle = PI/2, run_time = .1))
        self.play(FadeOut(sphere))

        Bell_pic = ImageMobject(r"media\images\external_images\John_bell_2_(cropped).png").scale(.5).shift(LEFT*3)
        self.play(FadeIn(Bell_pic))

        self.wait(4)

        State = MathTex(r"\vert \Psi \rangle=  \frac{1}{\sqrt{2}}(\vert \! \uparrow \uparrow \rangle - \vert \! \downarrow \downarrow \rangle)}}").shift(RIGHT*3+UP*2)
        Note = Tex("*He didn't use this specific state but they're all very similar").scale(.5).to_edge(DOWN)

        self.play(Write(State))
        self.add(Note)
        self.wait(5)
        self.play(FadeOut(Note))

        vec = Vector([0,.5,0])
        vec.next_to(sphere,UP,0)
        
        Stern_1 = VGroup(sphere, vec)
        Stern_2 = Stern_1.copy().next_to(Stern_1, RIGHT)
        Sterns = VGroup(Stern_1, Stern_2)
        Sterns.next_to(State, 2*DOWN)

        self.play(FadeIn(Stern_1, Stern_2))

        e1 = Sphere(center= sphere.get_center(), radius=.125)
        e1.set_color(RED)

        e2 = Sphere(center= sphere.get_center() + 2.25*RIGHT, radius=.125)
        e2.set_color(BLUE)

        e11 = e1.copy()
        e22 = e2.copy()

        self.play(FadeIn(e1, e2))
        self.play(e1.animate.shift(UP*2), e2.animate.shift(UP*2))
        self.play(FadeOut(e1, e2))

        self.play(FadeIn(e11, e22))
        self.play(e11.animate.shift(DOWN*2), e22.animate.shift(DOWN*2))
        self.play(FadeOut(e11, e22))
        self.play(FadeOut(Sterns))

        self.wait(15)

        Theorem = MathTex(r"|P(\vec{a},\vec{b}) - P(\vec{a},\vec{c})| \leq 1 + P(\vec{b},\vec{c})").next_to(State, DOWN*2)

        self.play(Write(Theorem))
        self.wait(20)

class Bell_1(Scene):
    def construct(self):

        youtube_pic = ImageMobject(r"media\images\external_images\bell_youtube.png").scale(2)
        youtube_pic.shift(DOWN*2)
        self.play(FadeIn(youtube_pic))
        self.play(youtube_pic.animate.shift(UP*10), run_time = 10)
        self.wait(2)

class Proof_1(Scene):
    def construct(self):

        sphere = Sphere()
        sphere.set_color(WHITE)
        sphere.set_opacity(.1)

        self.play(Rotate(sphere,axis = RIGHT, angle = PI/2, run_time = .1))
        self.play(FadeOut(sphere))

        sphere_2 = sphere.copy()
        sphere_3 = sphere.copy()

        vec = Vector([0,.5,0])
        vec_2 = Vector([0,.5,0])
        vec_3 = Vector([0,.5,0])

        vec.next_to(sphere,UP,0)
        vec_2.next_to(sphere_2, UP, 0)
        vec_3.next_to(sphere_3, UP, 0)
        
        Stern_1 = VGroup(sphere, vec)
        Stern_2 = VGroup(sphere_2, vec_2)
        Stern_3 = VGroup(sphere_3, vec_3)

        Sterns = VGroup(Stern_1, Stern_2, Stern_3).arrange(RIGHT)
        
        Bell_State = MathTex(
            r"\vert {{\Psi}} \rangle = {{\frac{1}{\sqrt{2}}}}(\vert \! {{\uparrow}}{{\uparrow}} \rangle - \vert \! {{\downarrow}}{{\downarrow}} \rangle)")
        GHZ_State = MathTex(
            r"\vert {{GHZ}} \rangle = {{\frac{1}{\sqrt{2}}}}(\vert \! {{\uparrow}}{{\uparrow}}{{\uparrow}} \rangle - \vert \! {{\downarrow}}{{\downarrow}}{{\downarrow}} \rangle)")
        
        Bell_State.shift(UP*2)
        GHZ_State.shift(UP*2)

        self.play(Write(Bell_State))
        self.wait(5)
        self.play(TransformMatchingTex(Bell_State, GHZ_State))
        self.wait(14)

        GHZ_2= MathTex(
            r"\vert {{GHZ}} \rangle = {{\frac{1}{\sqrt{2}}}}(\vert \! {{\uparrow}}{{\uparrow}}{{\uparrow}} \rangle_{ {{z}}{{z}}{{z}}} - \vert \! {{\downarrow}}{{\downarrow}}{{\downarrow}} \rangle_{ {{z}}{{z}}{{z}}})")

        GHZ_2.shift(UP*2)
        
        Sterns.shift(DOWN)

        self.play(FadeIn(Sterns), TransformMatchingTex(GHZ_State, GHZ_2))
        self.wait(7)

        e1 = Sphere(center= sphere.get_center(), radius=.125)
        e1.set_color(RED)

        e2 = Sphere(center= sphere_2.get_center(), radius=.125)
        e2.set_color(BLUE)

        e3 = Sphere(center= sphere_3.get_center(), radius=.125)
        e3.set_color(GREEN)

        self.play(
            e1.animate.shift(UP*2),
            e2.animate.shift(UP*2),
            e3.animate.shift(UP*2),
        )

        self.play(FadeOut(e1, e2, e3))

        e1.move_to(sphere.get_center())
        e2.move_to(sphere_2.get_center())
        e3.move_to(sphere_3.get_center())

        self.play(
            e1.animate.shift(DOWN*2),
            e2.animate.shift(DOWN*2),
            e3.animate.shift(DOWN*2),
        )

        self.play(FadeOut(e1, e2, e3))

        self.wait(3)

        self.play(
            Rotate(Stern_1, -PI/2),
            Rotate(Stern_2, -PI/2),
            Rotate(Stern_3, -PI/2),
        )

        self.play(Sterns.animate.arrange(RIGHT, buff = 1))

        Z_to_X = MathTex(r"{{\vert \! \uparrow \rangle}}{{_z}} &= {{\frac{1}{\sqrt{2}}}}({{\vert \! \uparrow \rangle}}{{_x}} + {{\vert \! \downarrow \rangle}}{{_x}}) \\ \
        {{\vert \! \downarrow \rangle}}{{_z}} &= {{\frac{1}{\sqrt{2}}}}({{\vert \! \uparrow \rangle}}{{_x}} - {{\vert \! \downarrow \rangle}}{{_x}})")

        Z_to_X.scale(.5).to_corner(DL)

        self.play(Write(Z_to_X))

        self.wait(2)

        GHZ_zzz= MathTex(
            r"\vert {{GHZ}} \rangle = {{\frac{1}{\sqrt{2}}}}(\vert \! {{\uparrow}} \rangle_z \vert \! {{\uparrow}} \rangle_z \vert \! {{\uparrow}} \rangle_z -\
                  \vert \! {{\downarrow}} \rangle_z \vert \! {{\downarrow}} \rangle_z \vert \! {{\downarrow}} \rangle_z )")

        GHZ_zzz.shift(UP*2)

        self.play(TransformMatchingTex(GHZ_2, GHZ_zzz))

        GHZ_xzz = MathTex(
            r"\vert {{GHZ}} \rangle = {{\frac{1}{\sqrt{2}}}}({{\frac{1}{\sqrt{2}}}} \vert \! {{\uparrow}} {{ + \downarrow}} \rangle_x \
                \vert \! {{\uparrow}} \rangle_z \vert \! {{\uparrow}} \rangle_z - \
                  {{\frac{1}{\sqrt{2}}}}\vert \! {{\uparrow - }}{{\downarrow}} \rangle_x \
                  \vert \! {{\downarrow}} \rangle_z \vert \! {{\downarrow}} \rangle_z )"
        ) #Am I allowed to put two arrows in one ket? Probably not but otherwise the math is too crowded.

        
        GHZ_xzz.shift(UP*2)

        self.play(TransformMatchingTex(GHZ_zzz, GHZ_xzz))

        GHZ_xxz = MathTex(
            r"\vert {{GHZ}} \rangle = {{\frac{1}{\sqrt{2}}}}({{\frac{1}{\sqrt{2}}}} \vert \! {{\uparrow}} {{ + \downarrow}} \rangle_x \
                {{\frac{1}{\sqrt{2}}}} \vert \! {{\uparrow}} {{ + \downarrow}} \rangle_x \vert \! {{\uparrow}} \rangle_z \\ - \
                  {{\frac{1}{\sqrt{2}}}}\vert \! {{\uparrow - }}{{\downarrow}} \rangle_x \
                  {{\frac{1}{\sqrt{2}}}}\vert \! {{\uparrow - }}{{\downarrow}} \rangle_x \vert \! {{\downarrow}} \rangle_z )"
           )
        
        GHZ_xxz.shift(UP*2)

        self.play(TransformMatchingTex(GHZ_xzz, GHZ_xxz), Sterns.animate.shift(DOWN))

        GHZ_xxx = MathTex(
            r"\vert {{GHZ}} \rangle = {{\frac{1}{\sqrt{2}}}}({{\frac{1}{\sqrt{2}}}} \vert \! {{\uparrow}} {{ + \downarrow}} \rangle_x \
                {{\frac{1}{\sqrt{2}}}} \vert \! {{\uparrow}} {{ + \downarrow}} \rangle_x {{\frac{1}{\sqrt{2}}}} \vert \! {{\uparrow}} {{ + \downarrow}} \rangle_x \\ - \
                  {{\frac{1}{\sqrt{2}}}}\vert \! {{\uparrow - }}{{\downarrow}} \rangle_x \
                  {{\frac{1}{\sqrt{2}}}}\vert \! {{\uparrow - }}{{\downarrow}} \rangle_x {{\frac{1}{\sqrt{2}}}}\vert \! {{\uparrow - }}{{\downarrow}} \rangle_x )"
           )
        
        GHZ_xxx.shift(UP*2)

        self.play(TransformMatchingTex(GHZ_xxz, GHZ_xxx))

        GHZ_x = MathTex(
            r"\vert {{GHZ}} \rangle = {{\frac{1}{4}}}((\vert \! {{\uparrow}} {{\uparrow}} {{\uparrow}} \rangle_{xxx} + \
            \vert \! {{\uparrow}} {{\uparrow}} {{\downarrow}} \rangle_{xxx} + \
            \vert \! {{\uparrow}} {{\downarrow}} {{\uparrow}} \rangle_{xxx} + \
            \vert \! {{\uparrow}} {{\downarrow}} {{\downarrow}} \rangle_{xxx} + \\ \
            \vert \! {{\downarrow}} {{\uparrow}} {{\uparrow}} \rangle_{xxx} + \
            \vert \! {{\downarrow}} {{\uparrow}} {{\downarrow}} \rangle_{xxx} + \
            \vert \! {{\downarrow}} {{\downarrow}} {{\uparrow}} \rangle_{xxx} + \
            \vert \! {{\downarrow}} {{\downarrow}} {{\downarrow}} \rangle_{xxx}) - \\ \
            (\vert \! {{\uparrow}} {{\uparrow}} {{\uparrow}} \rangle_{xxx} - \
            \vert \! {{\uparrow}} {{\uparrow}} {{\downarrow}} \rangle_{xxx} - \
            \vert \! {{\uparrow}} {{\downarrow}} {{\uparrow}} \rangle_{xxx} + \
            \vert \! {{\uparrow}} {{\downarrow}} {{\downarrow}} \rangle_{xxx} - \\ \
            \vert \! {{\downarrow}} {{\uparrow}} {{\uparrow}} \rangle_{xxx} + \
            \vert \! {{\downarrow}} {{\uparrow}} {{\downarrow}} \rangle_{xxx} + \
            \vert \! {{\downarrow}} {{\downarrow}} {{\uparrow}} \rangle_{xxx} - \
            \vert \! {{\downarrow}} {{\downarrow}} {{\downarrow}} \rangle_{xxx}))"
           ).shift(UP*2)

        self.play(TransformMatchingTex(GHZ_xxx, GHZ_x), FadeOut(Z_to_X), Sterns.animate.shift(DOWN))

        GHZ_x_clean = MathTex(
            r"\vert {{GHZ}} \rangle = {{\frac{1}{2}}}(\vert \! {{\uparrow}}{{\uparrow}}{{\downarrow}}\rangle_{xxx} + \
            \vert \! {{\uparrow}}{{\downarrow}}{{\uparrow}}\rangle_{xxx} + \
            \vert \! {{\downarrow}}{{\uparrow}}{{\uparrow}}\rangle_{xxx} + \
            \vert \! {{\downarrow}}{{\downarrow}}{{\downarrow}}\rangle_{xxx})"
           ).shift(UP*3)
        
        self.play(TransformMatchingTex(GHZ_x, GHZ_x_clean), Sterns.animate.arrange(DOWN).shift(.5*DOWN))

        self.wait(10)

        e1.move_to(sphere.get_center())
        e2.move_to(sphere_2.get_center())
        e3.move_to(sphere_3.get_center())

        rect_1 = SurroundingRectangle(GHZ_x_clean[17:20])
        rect_2 = SurroundingRectangle(GHZ_x_clean[13:16])
        rect_3 = SurroundingRectangle(GHZ_x_clean[9:12])
        rect_4 = SurroundingRectangle(GHZ_x_clean[5:8])

        self.play(FadeIn(e1, e2, e3))

        self.wait(5)

        self.play(Create(rect_1),
            e1.animate.shift(LEFT*2),
            e2.animate.shift(LEFT*2),
            e3.animate.shift(LEFT*2),
        )

        self.play(FadeOut(e1, e2, e3))

        e1.move_to(sphere.get_center())
        e2.move_to(sphere_2.get_center())
        e3.move_to(sphere_3.get_center())

        self.add(e1, e2, e3)

        self.play(Succession(
            TransformMatchingShapes(rect_1, rect_2),
            AnimationGroup(e1.animate.shift(LEFT*2),
            e2.animate.shift(RIGHT*2),
            e3.animate.shift(RIGHT*2),
        ))) #Should have used Transform(), rectangles are not same size 

        self.play(FadeOut(e1, e2, e3))

        e1.move_to(sphere.get_center())
        e2.move_to(sphere_2.get_center())
        e3.move_to(sphere_3.get_center())

        self.add(e1, e2, e3)

        self.play(Succession(
            TransformMatchingShapes(rect_2, rect_3),
            AnimationGroup(e1.animate.shift(RIGHT*2),
            e2.animate.shift(LEFT*2),
            e3.animate.shift(RIGHT*2),
        )))

        self.play(FadeOut(e1, e2, e3))

        e1.move_to(sphere.get_center())
        e2.move_to(sphere_2.get_center())
        e3.move_to(sphere_3.get_center())

        self.add(e1, e2, e3)

        self.play(Succession(
            TransformMatchingShapes(rect_3, rect_4),
            AnimationGroup(e1.animate.shift(RIGHT*2),
            e2.animate.shift(RIGHT*2),
            e3.animate.shift(LEFT*2),
        )))

        self.play(FadeOut(e1, e2, e3, rect_4))

        self.wait(8)

        self.play(FadeOut(Stern_2, Stern_3), Stern_1.animate.move_to(RIGHT))
        e1.move_to(sphere.get_center())
        self.play(Create(e1), run_time = .1)

        Ax_1 = MathTex(r"\{ {{A_x}}\} = ").shift(LEFT*3)
        Ax_2 = MathTex(r"\{ {{A_x}}\} = {{+1}}").shift(LEFT*3)
        Ax_3 = MathTex(r"\{ {{A_x}}\} = {{-1}}").shift(LEFT*3)

        Ax_1[1].set_color(RED)
        Ax_2[1].set_color(RED)
        Ax_3[1].set_color(RED)

        self.play(FadeIn(Ax_1))

        self.wait(1)

        self.play(e1.animate.shift(RIGHT*2), TransformMatchingTex(Ax_1, Ax_2))
        self.play(FadeOut(e1))
        e1.move_to(sphere.get_center())

        self.wait(3)

        self.play(FadeIn(e1))
        self.play(e1.animate.shift(LEFT*2), TransformMatchingTex(Ax_2, Ax_3))
        self.wait(2)

        self.play(FadeOut(Stern_1, e1, Ax_3))

class Proof_2(Scene):
    def construct(self):

        GHZ_x_clean = MathTex(
            r"\vert {{GHZ}} \rangle = {{\frac{1}{2}}}(\vert \! {{\uparrow}}{{\uparrow}}{{\downarrow}}\rangle_{xxx} + \
            \vert \! {{\uparrow}}{{\downarrow}}{{\uparrow}}\rangle_{xxx} + \
            \vert \! {{\downarrow}}{{\uparrow}}{{\uparrow}}\rangle_{xxx} + \
            \vert \! {{\downarrow}}{{\downarrow}}{{\downarrow}}\rangle_{xxx})"
           ).shift(UP*3)
        
        self.add(GHZ_x_clean)

        Prod_1 = MathTex(r"\{ {{A_x}}\} \{ {{B_x}}\} \{ {{C_x}}\} = {{-1}} * {{-1}} * {{-1}} = -1")
        Prod_2 = MathTex(r"\{ {{A_x}}\} \{ {{B_x}}\} \{ {{C_x}}\} = {{-1}} * {{+1}} * {{+1}} = -1")
        Prod_3 = MathTex(r"\{ {{A_x}}\} \{ {{B_x}}\} \{ {{C_x}}\} = {{+1}} * {{-1}} * {{+1}} = -1")
        Prod_4 = MathTex(r"\{ {{A_x}}\} \{ {{B_x}}\} \{ {{C_x}}\} = {{+1}} * {{+1}} * {{-1}} = -1")

        Prod_1[1].set_color(RED)
        Prod_1[3].set_color(BLUE)
        Prod_1[5].set_color(GREEN)
        Prod_1[7].set_color(RED)
        Prod_1[9].set_color(BLUE)
        Prod_1[11].set_color(GREEN)

        Prod_2[1].set_color(RED)
        Prod_2[3].set_color(BLUE)
        Prod_2[5].set_color(GREEN)
        Prod_2[7].set_color(RED)
        Prod_2[9].set_color(BLUE)
        Prod_2[11].set_color(GREEN)

        Prod_3[1].set_color(RED)
        Prod_3[3].set_color(BLUE)
        Prod_3[5].set_color(GREEN)
        Prod_3[7].set_color(RED)
        Prod_3[9].set_color(BLUE)
        Prod_3[11].set_color(GREEN)

        Prod_4[1].set_color(RED)
        Prod_4[3].set_color(BLUE)
        Prod_4[5].set_color(GREEN)
        Prod_4[7].set_color(RED)
        Prod_4[9].set_color(BLUE)
        Prod_4[11].set_color(GREEN) 

        rect_1 = SurroundingRectangle(GHZ_x_clean[17:20])
        rect_2 = SurroundingRectangle(GHZ_x_clean[13:16])
        rect_3 = SurroundingRectangle(GHZ_x_clean[9:12])
        rect_4 = SurroundingRectangle(GHZ_x_clean[5:8])

        self.play(FadeIn(rect_1))
        self.play(FadeIn(Prod_1))
        self.wait(1)
        self.play(TransformMatchingTex(Prod_1, Prod_2), TransformMatchingShapes(rect_1, rect_2))   
        self.wait(1)     
        self.play(TransformMatchingTex(Prod_2, Prod_3), TransformMatchingShapes(rect_2, rect_3))
        self.wait(1)
        self.play(TransformMatchingTex(Prod_3, Prod_4), TransformMatchingShapes(rect_3, rect_4))        
        self.wait(9)
        self.play(FadeOut(Prod_4, GHZ_x_clean, rect_4))

class Proof_3(Scene):
    def construct(self):

        sphere = Sphere()
        sphere.set_color(WHITE)
        sphere.set_opacity(.1)

        self.play(Rotate(sphere,axis = RIGHT, angle = PI/2, run_time = .1))
        self.play(FadeOut(sphere))

        sphere_2 = sphere.copy()
        sphere_3 = sphere.copy()

        vec = Vector([0,.5,0])
        vec_2 = Vector([0,.5,0])
        vec_3 = Vector([0,.5,0])

        e1 = Sphere(center= sphere.get_center(), radius=.125)
        e1.set_color(RED)

        e2 = Sphere(center= sphere_2.get_center(), radius=.125)
        e2.set_color(BLUE)

        e3 = Sphere(center= sphere_3.get_center(), radius=.125)
        e3.set_color(GREEN)

        vec.next_to(sphere,UP,0)
        vec_2.next_to(sphere_2, UP, 0)
        vec_3.next_to(sphere_3, UP, 0)

        Stern_1 = VGroup(sphere, vec, e1)
        Stern_2 = VGroup(sphere_2, vec_2, e2)
        Stern_3 = VGroup(sphere_3, vec_3, e3)

        Sterns = VGroup(Stern_1, Stern_2, Stern_3)

        self.play(
            Rotate(Stern_1, -PI/2),
            Rotate(Stern_2, -PI/2),
            Rotate(Stern_3, -PI/2),
        )

        self.play(Sterns.animate.arrange(DOWN).shift(DOWN*.5))

        GHZ_zzz= MathTex(
            r"\vert {{GHZ}} \rangle = {{\frac{1}{\sqrt{2}}}}(\vert \! {{\uparrow}}{{\uparrow}}{{\uparrow}} \rangle_{ {{z}}{{z}}{{z}}} - \
                \vert \! {{\downarrow}}{{\downarrow}}{{\downarrow}} \rangle_{ {{z}}{{z}}{{z}}})")

        GHZ_zzz.shift(UP*3)

        self.play(FadeIn(GHZ_zzz))

        self.wait(3)

        self.play(
            Rotate(Stern_2, axis = UP + [0, 0, .5], angle = -PI/2),
            Rotate(Stern_3, axis = UP + [0, 0, .5], angle = -PI/2))
        
        self.play(Stern_2.animate.move_to(1.5*LEFT+DOWN),
                  Stern_3.animate.move_to(1.5*RIGHT+DOWN),
                  Stern_1.animate.move_to(UP))
        
        sphere_center = sphere.get_center()

        self.play(Stern_1.animate.shift(LEFT*sphere_center))

        self.wait(8)

        Z_to_Y = MathTex(r"{{\vert \! \uparrow \rangle}}{{_z}} &= {{\frac{1}{\sqrt{2}}}}({{\vert \! \uparrow \rangle}}{{_y}} + {{\vert \! \downarrow \rangle}}{{_y}}) \\ \
        {{\vert \! \downarrow \rangle}}{{_z}} &= {{\frac{1}{\sqrt{2}}}}{{ * i}}({{\vert \! \downarrow \rangle}}{{_y}} - {{\vert \! \uparrow \rangle}}{{_y}})")\
            .scale(.5).to_corner(DL)
        
        self.add(Z_to_Y)

        GHZ_xzz = MathTex(
            r"\vert {{GHZ}} \rangle = {{\frac{1}{\sqrt{2}}}}({{\frac{1}{\sqrt{2}}}} \vert \! {{\uparrow}} {{ + \downarrow}} \rangle_x \
                \vert \! {{\uparrow}} \rangle_z \vert \! {{\uparrow}} \rangle_z - \
                  {{\frac{1}{\sqrt{2}}}}\vert \! {{\uparrow - }}{{\downarrow}} \rangle_x \
                  \vert \! {{\downarrow}} \rangle_z \vert \! {{\downarrow}} \rangle_z )"
        ).shift(UP*2)

        self.play(TransformMatchingTex(GHZ_zzz, GHZ_xzz))

        GHZ_xyz = MathTex(
            r"\vert {{GHZ}} \rangle = {{\frac{1}{\sqrt{2}}}}({{\frac{1}{\sqrt{2}}}} \vert \! {{\uparrow}} {{ + \downarrow}} \rangle_x \
                {{\frac{1}{\sqrt{2}}}} \vert \! {{\uparrow}} {{ + \downarrow}} \rangle_y \vert \! {{\uparrow}} \rangle_z \\ - \
                  {{\frac{1}{\sqrt{2}}}}\vert \! {{\uparrow - }}{{\downarrow}} \rangle_x \
                  {{\frac{1}{\sqrt{2}}}}{{ * i}} \vert \! {{\downarrow}} {{ - \uparrow}} \rangle_y \vert \! {{\downarrow}} \rangle_z )"
        ).shift(UP*2)

        self.play(TransformMatchingTex(GHZ_xzz, GHZ_xyz), Sterns.animate.shift(DOWN))

        GHZ_xyy = MathTex(
            r"\vert {{GHZ}} \rangle = {{\frac{1}{\sqrt{2}}}}({{\frac{1}{\sqrt{2}}}} \vert \! {{\uparrow}} {{ + \downarrow}} \rangle_x \
                {{\frac{1}{\sqrt{2}}}} \vert \! {{\uparrow}} {{ + \downarrow}} \rangle_y {{\frac{1}{\sqrt{2}}}} \vert \! {{\uparrow}} {{ + \downarrow}} \rangle_y \\ - \
                  {{\frac{1}{\sqrt{2}}}}\vert \! {{\uparrow - }}{{\downarrow}} \rangle_x \
                  {{\frac{1}{\sqrt{2}}}}{{ * i}}\vert \! {{\downarrow}} {{ - \uparrow}} \rangle_y {{\frac{1}{\sqrt{2}}}}{{ * i}}\vert \! {{\downarrow}} {{ - \uparrow}} \rangle_y )"
        ).shift(UP*2)

        self.play(TransformMatchingTex(GHZ_xyz, GHZ_xyy))

        GHZ_y = MathTex(
            r"\vert {{GHZ}} \rangle = {{\frac{1}{4}}}((\vert \! {{\uparrow}} {{\uparrow}} {{\uparrow}} \rangle_{xyy} + \
            \vert \! {{\uparrow}} {{\uparrow}} {{\downarrow}} \rangle_{xyy} + \
            \vert \! {{\uparrow}} {{\downarrow}} {{\uparrow}} \rangle_{xyy} + \
            \vert \! {{\uparrow}} {{\downarrow}} {{\downarrow}} \rangle_{xyy} + \\ \
            \vert \! {{\downarrow}} {{\uparrow}} {{\uparrow}} \rangle_{xyy} + \
            \vert \! {{\downarrow}} {{\uparrow}} {{\downarrow}} \rangle_{xyy} + \
            \vert \! {{\downarrow}} {{\downarrow}} {{\uparrow}} \rangle_{xyy} + \
            \vert \! {{\downarrow}} {{\downarrow}} {{\downarrow}} \rangle_{xyy}) + \\ \
            (\vert \! {{\uparrow}} {{\uparrow}} {{\uparrow}} \rangle_{xyy} - \
            \vert \! {{\uparrow}} {{\uparrow}} {{\downarrow}} \rangle_{xyy} - \
            \vert \! {{\uparrow}} {{\downarrow}} {{\uparrow}} \rangle_{xyy} + \
            \vert \! {{\uparrow}} {{\downarrow}} {{\downarrow}} \rangle_{xyy} - \\ \
            \vert \! {{\downarrow}} {{\uparrow}} {{\uparrow}} \rangle_{xyy} + \
            \vert \! {{\downarrow}} {{\uparrow}} {{\downarrow}} \rangle_{xyy} + \
            \vert \! {{\downarrow}} {{\downarrow}} {{\uparrow}} \rangle_{xyy} - \
            \vert \! {{\downarrow}} {{\downarrow}} {{\downarrow}} \rangle_{xyy}))"
            ).shift(UP*2)
        

        self.play(TransformMatchingTex(GHZ_xyy, GHZ_y), FadeOut(Z_to_Y), Sterns.animate.shift(DOWN))

        GHZ_y_clean = MathTex(
            r"\vert {{GHZ}} \rangle = {{\frac{1}{2}}}(\vert \! {{\uparrow}}{{\uparrow}}{{\uparrow}}\rangle_{xyy} + \
            \vert \! {{\uparrow}}{{\downarrow}}{{\downarrow}}\rangle_{xyy} + \
            \vert \! {{\downarrow}}{{\uparrow}}{{\downarrow}}\rangle_{xyy} + \
            \vert \! {{\downarrow}}{{\downarrow}}{{\uparrow}}\rangle_{xyy})"
           ).shift(UP*3)
        
        self.play(TransformMatchingTex(GHZ_y, GHZ_y_clean), Stern_2.animate.shift(UP), Stern_3.animate.shift(UP), Stern_1.animate.shift(2*UP))

        self.wait(10)

        rect_4 = SurroundingRectangle(GHZ_y_clean[17:20])
        rect_3 = SurroundingRectangle(GHZ_y_clean[13:16])
        rect_2 = SurroundingRectangle(GHZ_y_clean[9:12])
        rect_1 = SurroundingRectangle(GHZ_y_clean[5:8])
        
        self.play(Create(rect_1),
            e1.animate.shift(RIGHT*2),
            e2.animate.shift((2*DOWN+[0,0,1])),
            e3.animate.shift((2*DOWN+[0,0,1])),
        )
        
        self.play(FadeOut(e1, e2, e3))

        e1.move_to(sphere.get_center())
        e2.move_to(sphere_2.get_center())
        e3.move_to(sphere_3.get_center())

        self.play(FadeIn(e1, e2, e3))

        self.play(Succession(
            TransformMatchingShapes(rect_1, rect_2),
            AnimationGroup(e1.animate.shift(RIGHT*2),
            e2.animate.shift((2*UP-[0,0,1])),
            e3.animate.shift((2*UP-[0,0,1])),
        )))

        self.play(FadeOut(e1, e2, e3))

        e1.move_to(sphere.get_center())
        e2.move_to(sphere_2.get_center())
        e3.move_to(sphere_3.get_center())

        self.play(FadeIn(e1, e2, e3))

        self.play(Succession(
            TransformMatchingShapes(rect_2, rect_3),
            AnimationGroup(e1.animate.shift(LEFT*2),
            e2.animate.shift((2*UP-[0,0,1])),
            e3.animate.shift((2*DOWN+[0,0,1])),
        )))

        self.play(FadeOut(e1, e2, e3))

        e1.move_to(sphere.get_center())
        e2.move_to(sphere_2.get_center())
        e3.move_to(sphere_3.get_center())

        self.play(FadeIn(e1, e2, e3))

        self.play(Succession(
            TransformMatchingShapes(rect_3, rect_4),
            AnimationGroup(e1.animate.shift(LEFT*2),
            e2.animate.shift((2*DOWN+[0,0,1])),
            e3.animate.shift((2*UP-[0,0,1])),
        )))

        self.play(FadeOut(Stern_1, Stern_2, Stern_3, rect_4, e1, e2, e3))

class Proof_4(Scene):
    def construct(self):

        GHZ_y_clean = MathTex(
            r"\vert {{GHZ}} \rangle = {{\frac{1}{2}}}(\vert \! {{\uparrow}}{{\uparrow}}{{\uparrow}}\rangle_{xyy} + \
            \vert \! {{\uparrow}}{{\downarrow}}{{\downarrow}}\rangle_{xyy} + \
            \vert \! {{\downarrow}}{{\uparrow}}{{\downarrow}}\rangle_{xyy} + \
            \vert \! {{\downarrow}}{{\downarrow}}{{\uparrow}}\rangle_{xyy})"
           ).shift(UP*3)
        
        rect_4 = SurroundingRectangle(GHZ_y_clean[17:20])
        rect_3 = SurroundingRectangle(GHZ_y_clean[13:16])
        rect_2 = SurroundingRectangle(GHZ_y_clean[9:12])
        rect_1 = SurroundingRectangle(GHZ_y_clean[5:8])

        self.add(GHZ_y_clean)

        Prod_0 = MathTex(r"\{ {{A_x}}\} \{ {{B_y}}\} \{ {{C_y}}{{\} = }}")
        Prod_1 = MathTex(r"\{ {{A_x}}\} \{ {{B_y}}\} \{ {{C_y}}{{\} = }}{{+1}} * {{+1}} * {{+1}} = +1")
        Prod_2 = MathTex(r"\{ {{A_x}}\} \{ {{B_y}}\} \{ {{C_y}}{{\} = }}{{+1}} * {{-1}} * {{-1}} = +1")
        Prod_3 = MathTex(r"\{ {{A_x}}\} \{ {{B_y}}\} \{ {{C_y}}{{\} = }}{{-1}} * {{+1}} * {{-1}} = +1")
        Prod_4 = MathTex(r"\{ {{A_x}}\} \{ {{B_y}}\} \{ {{C_y}}{{\} = }}{{-1}} * {{-1}} * {{+1}} = +1")
        Prod_5 = MathTex(r"\{ {{A_x}}\} \{ {{B_y}}\} \{ {{C_y}}{{\} = }}+1")

        Prod_0[1].set_color(RED)
        Prod_0[3].set_color(BLUE_E)
        Prod_0[5].set_color(GREEN_A)

        Prod_1[1].set_color(RED)
        Prod_1[3].set_color(BLUE_E)
        Prod_1[5].set_color(GREEN_A)
        Prod_1[7].set_color(RED)
        Prod_1[9].set_color(BLUE_E)
        Prod_1[11].set_color(GREEN_A)

        Prod_2[1].set_color(RED)
        Prod_2[3].set_color(BLUE_E)
        Prod_2[5].set_color(GREEN_A)
        Prod_2[7].set_color(RED)
        Prod_2[9].set_color(BLUE_E)
        Prod_2[11].set_color(GREEN_A)

        Prod_3[1].set_color(RED)
        Prod_3[3].set_color(BLUE_E)
        Prod_3[5].set_color(GREEN_A)
        Prod_3[7].set_color(RED)
        Prod_3[9].set_color(BLUE_E)
        Prod_3[11].set_color(GREEN_A)

        Prod_4[1].set_color(RED)
        Prod_4[3].set_color(BLUE_E)
        Prod_4[5].set_color(GREEN_A)
        Prod_4[7].set_color(RED)
        Prod_4[9].set_color(BLUE_E)
        Prod_4[11].set_color(GREEN_A)

        Prod_5[1].set_color(RED)
        Prod_5[3].set_color(BLUE_E)
        Prod_5[5].set_color(GREEN_A)

        self.play(FadeIn(Prod_0))
        self.wait(6)
        self.play(FadeIn(rect_1), TransformMatchingTex(Prod_0, Prod_1))
        self.wait(3)
        self.play(TransformMatchingTex(Prod_1, Prod_2), TransformMatchingShapes(rect_1, rect_2))   
        self.wait(1)     
        self.play(TransformMatchingTex(Prod_2, Prod_3), TransformMatchingShapes(rect_2, rect_3))
        self.wait(1)
        self.play(TransformMatchingTex(Prod_3, Prod_4), TransformMatchingShapes(rect_3, rect_4))        
        self.wait(3)
        self.play(FadeOut(rect_4), TransformMatchingTex(Prod_4, Prod_5))

class Proof_6(Scene):
    def construct(self):

        sphere = Sphere()
        sphere.set_color(WHITE)
        sphere.set_opacity(.1)

        self.play(Rotate(sphere,axis = RIGHT, angle = PI/2, run_time = .1))
        self.play(FadeOut(sphere))

        sphere_2 = sphere.copy()
        sphere_3 = sphere.copy()

        vec = Vector([0,.5,0])
        vec_2 = Vector([0,.5,0])
        vec_3 = Vector([0,.5,0])

        e1 = Sphere(center= sphere.get_center(), radius=.125)
        e1.set_color(RED)

        e2 = Sphere(center= sphere_2.get_center(), radius=.125)
        e2.set_color(BLUE)

        e3 = Sphere(center= sphere_3.get_center(), radius=.125)
        e3.set_color(GREEN)

        vec.next_to(sphere,UP,0)
        vec_2.next_to(sphere_2, UP, 0)
        vec_3.next_to(sphere_3, UP, 0)

        Stern_1 = VGroup(sphere, vec, e1)
        Stern_2 = VGroup(sphere_2, vec_2, e2)
        Stern_3 = VGroup(sphere_3, vec_3, e3)

        Sterns = VGroup(Stern_1, Stern_2, Stern_3)

        self.play(
            Rotate(Stern_1, -PI/2),
            Rotate(Stern_2, -PI/2),
            Rotate(Stern_3, -PI/2),
        )

        self.play(
            Rotate(Stern_2, axis = UP+[0, 0, .5], angle = -PI/2),
            Rotate(Stern_3, axis = UP+[0, 0, .5], angle = -PI/2))

        self.wait(3)

        self.play(FadeOut(Sterns)) 

        GHZ_xyy = MathTex(
            r"\vert {{GHZ}} \rangle = {{\frac{1}{2}}}(\vert \! {{\uparrow}}{{\uparrow}}{{\uparrow}}\rangle_{ {{x}} {{y}} {{y}} } + \
            \vert \! {{\uparrow}}{{\downarrow}}{{\downarrow}}\rangle_{ {{x}} {{y}} {{y}} } + \
            \vert \! {{\downarrow}}{{\uparrow}}{{\downarrow}}\rangle_{ {{x}} {{y}} {{y}} } + \
            \vert \! {{\downarrow}}{{\downarrow}}{{\uparrow}}\rangle_{ {{x}} {{y}} {{y}} })"
           ).shift(UP*3)
        
        Eq_2 = MathTex(r"\{ {{A_x}}\} \{ {{B_y}}\} \{ {{C_y}}\} = +1")

        Eq_2[1].set_color(RED)
        Eq_2[3].set_color(BLUE_E)
        Eq_2[5].set_color(GREEN_A)

        self.add(GHZ_xyy, Eq_2)
        self.wait(3)

        Sterns.arrange(RIGHT, buff = 2)
        Sterns.move_to(DOWN*2)

        self.play(FadeIn(Sterns), Eq_2.animate.shift(2*UP))
        self.wait(2)
        self.play(
            Rotate(Stern_1, axis = UP + [0, 0, .5], angle = -PI/2),
            Rotate(Stern_2, axis = UP + [0, 0, .5], angle = PI/2)
        )
        self.wait(4)

        GHZ_yxy = MathTex(
            r"\vert {{GHZ}} \rangle = {{\frac{1}{2}}}(\vert \! {{\uparrow}}{{\uparrow}}{{\uparrow}}\rangle_{ {{y}} {{x}} {{y}} } + \
            \vert \! {{\uparrow}}{{\downarrow}}{{\downarrow}}\rangle_{ {{y}} {{x}} {{y}} } + \
            \vert \! {{\downarrow}}{{\uparrow}}{{\downarrow}}\rangle_{ {{y}} {{x}} {{y}} } + \
            \vert \! {{\downarrow}}{{\downarrow}}{{\uparrow}}\rangle_{ {{y}} {{x}} {{y}} })"
           ).shift(UP*3)
        
        self.play(FocusOn(GHZ_xyy[7]))
        self.play(TransformMatchingTex(GHZ_xyy, GHZ_yxy), run_time = 2)
        self.wait(2)

        Eq_3 = MathTex(r"\{ {{A_y}}\} \{ {{B_x}}\} \{ {{C_y}}\} = +1").next_to(Eq_2, DOWN)

        Eq_3[1].set_color(RED_B)
        Eq_3[3].set_color(BLUE)
        Eq_3[5].set_color(GREEN_A)

        self.play(FadeIn(Eq_3))
        self.wait(7)

        GHZ_yyx = MathTex(
            r"\vert {{GHZ}} \rangle = {{\frac{1}{2}}}(\vert \! {{\uparrow}}{{\uparrow}}{{\uparrow}}\rangle_{ {{y}} {{y}} {{x}} } + \
            \vert \! {{\uparrow}}{{\downarrow}}{{\downarrow}}\rangle_{ {{y}} {{y}} {{x}} } + \
            \vert \! {{\downarrow}}{{\uparrow}}{{\downarrow}}\rangle_{ {{y}} {{y}} {{x}} } + \
            \vert \! {{\downarrow}}{{\downarrow}}{{\uparrow}}\rangle_{ {{y}} {{y}} {{x}} })"
           ).shift(UP*3)
        
        self.play(
            Rotate(Stern_2, axis = UP + [0, 0, .5], angle = -PI/2),
            Rotate(Stern_3, axis = UP + [0, 0, .5], angle = PI/2),
            TransformMatchingTex(GHZ_yxy, GHZ_yyx)
        )

        self.wait(2)

        Eq_4 = MathTex(r"\{ {{A_y}}\} \{ {{B_y}}\} \{ {{C_x}}\} = +1").next_to(Eq_3, DOWN)

        Eq_4[1].set_color(RED_B)
        Eq_4[3].set_color(BLUE_E)
        Eq_4[5].set_color(GREEN)

        self.play(FadeIn(Eq_4))
        self.wait(2)

        Eqs = VGroup(Eq_2, Eq_3, Eq_4)

        Eq_1 = MathTex(r"\{ {{A_x}}\} \{ {{B_x}}\} \{ {{C_x}}\} = -1").shift(UP*2)

        Eq_1[1].set_color(RED)
        Eq_1[3].set_color(BLUE)
        Eq_1[5].set_color(GREEN)

        self.play(Eqs.animate.shift(DOWN*(.25 + Eq_2.height)), FadeIn(Eq_1))
        self.wait(2)
        self.play(FadeOut(Sterns))
        self.wait(5)

class Contradiction_1(Scene):
    def construct(self):

        Eq_1 = MathTex(r"\{ {{A_x}}\} \{ {{B_x}}\} \{ {{C_x}}\} = -1").shift(UP*2)

        Eq_1[1].set_color(RED)
        Eq_1[3].set_color(BLUE)
        Eq_1[5].set_color(GREEN)

        Eq_2 = MathTex(r"\{ {{A_x}}\} \{ {{B_y}}\} \{ {{C_y}}\} = +1").next_to(Eq_1, DOWN)

        Eq_2[1].set_color(RED)
        Eq_2[3].set_color(BLUE_E)
        Eq_2[5].set_color(GREEN_A)

        Eq_3 = MathTex(r"\{ {{A_y}}\} \{ {{B_x}}\} \{ {{C_y}}\} = +1").next_to(Eq_2, DOWN)

        Eq_3[1].set_color(RED_B)
        Eq_3[3].set_color(BLUE)
        Eq_3[5].set_color(GREEN_A)

        Eq_4 = MathTex(r"\{ {{A_y}}\} \{ {{B_y}}\} \{ {{C_x}}\} = +1").next_to(Eq_3, DOWN)

        Eq_4[1].set_color(RED_B)
        Eq_4[3].set_color(BLUE_E)
        Eq_4[5].set_color(GREEN)

        Eqs = VGroup(Eq_1, Eq_2, Eq_3, Eq_4)

        GHZ_yyx = MathTex(
            r"\vert {{GHZ}} \rangle = {{\frac{1}{2}}}(\vert \! {{\uparrow}}{{\uparrow}}{{\uparrow}}\rangle_{ {{y}} {{y}} {{x}} } + \
            \vert \! {{\uparrow}}{{\downarrow}}{{\downarrow}}\rangle_{ {{y}} {{y}} {{x}} } + \
            \vert \! {{\downarrow}}{{\uparrow}}{{\downarrow}}\rangle_{ {{y}} {{y}} {{x}} } + \
            \vert \! {{\downarrow}}{{\downarrow}}{{\uparrow}}\rangle_{ {{y}} {{y}} {{x}} })"
           ).shift(UP*3)
        
        self.add(Eqs, GHZ_yyx)
        self.play(FadeOut(GHZ_yyx), Eqs.animate.move_to(ORIGIN))
        self.wait(20)

class Contradiction_2(Scene):
    def construct(self):

        sphere = Sphere()
        sphere.set_color(WHITE)
        sphere.set_opacity(.1)

        self.play(Rotate(sphere,axis = RIGHT, angle = PI/2, run_time = .1))
        self.play(FadeOut(sphere))

        sphere_2 = sphere.copy()

        vec = Vector([0,.5,0])
        vec_2 = Vector([0,.5,0])

        e1 = Sphere(center= sphere.get_center(), radius=.125)
        e1.set_color(RED)

        e2 = Sphere(center= sphere_2.get_center(), radius=.125)
        e2.set_color(BLUE)

        vec.next_to(sphere,UP,0)
        vec_2.next_to(sphere_2, UP, 0)

        Stern_1 = VGroup(sphere, vec, e1)
        Stern_2 = VGroup(sphere_2, vec_2, e2)

        self.play(Stern_1.animate.shift(LEFT*4.5), Stern_2.animate.shift(RIGHT*4.5))
        self.wait(3)

        def signal():
            arc = Arc(radius = 6, start_angle=-.4, angle=0.8, arc_center=sphere.get_center() + 6*LEFT, color = BLUE)
            arc.add_updater(lambda mob, dt: mob.shift(1.5*RIGHT*dt))
            return arc

        signal = signal()

        self.play(e1.animate.shift(DOWN*2))
        self.add(signal)
        self.wait(2)
        self.play(e2.animate.shift(DOWN*2))
        self.wait(15)

class Contradiction_3(Scene):
    def construct(self):

        Eq_1 = MathTex(r"{{ \{A_x\} }}{{ \{B_x\} }}{{ \{C_x\} }}{{ = -1}}").shift(UP*2)

        Eq_1[0][1:-1].set_color(RED)
        Eq_1[1][1:-1].set_color(BLUE)
        Eq_1[2][1:-1].set_color(GREEN)

        Eq_2 = MathTex(r"{{ \{A_x\} }}{{ \{B_y\} }}{{ \{C_y\} }}{{ = +1}}").next_to(Eq_1, DOWN)

        Eq_2[0][1:-1].set_color(RED)
        Eq_2[1][1:-1].set_color(BLUE_E)
        Eq_2[2][1:-1].set_color(GREEN_A)

        Eq_3 = MathTex(r"{{ \{A_y\} }}{{ \{B_x\} }}{{ \{C_y\} }}{{ = +1}}").next_to(Eq_2, DOWN)

        Eq_3[0][1:-1].set_color(RED_B)
        Eq_3[1][1:-1].set_color(BLUE)
        Eq_3[2][1:-1].set_color(GREEN_A)

        Eq_4 = MathTex(r"{{ \{A_y\} }}{{ \{B_y\} }}{{ \{C_x\} }}{{ = +1}}").next_to(Eq_3, DOWN)

        Eq_4[0][1:-1].set_color(RED_B)
        Eq_4[1][1:-1].set_color(BLUE_E)
        Eq_4[2][1:-1].set_color(GREEN)

        Eqs = VGroup(Eq_1, Eq_2, Eq_3, Eq_4).move_to(ORIGIN)
        
        self.add(Eqs)
        self.wait(9)

        Eq_1_Ax = MathTex(r"{{ -1 * }}{{ \{B_x\} }}{{ \{C_x\} }}{{ = -1}}").move_to(Eq_1)

        Eq_1_Ax[0][:2].set_color(RED)
        Eq_1_Ax[1][1:-1].set_color(BLUE)
        Eq_1_Ax[2][1:-1].set_color(GREEN)

        Eq_2_1 = MathTex(r"{{ -1 * }}{{ \{B_y\} }}{{ \{C_y\} }}{{ = +1}}").next_to(Eq_1_Ax, DOWN)

        Eq_2_1[0][:2].set_color(RED)
        Eq_2_1[1][1:-1].set_color(BLUE_E)
        Eq_2_1[2][1:-1].set_color(GREEN_A)

        self.play(TransformMatchingTex(Eq_1, Eq_1_Ax))
        self.play(TransformMatchingTex(Eq_2, Eq_2_1))

        Eq_1_Bx = MathTex(r"{{ -1 * }}{{ -1 * }}{{ \{C_x\} }}{{ = -1}}").move_to(Eq_1_Ax)

        Eq_1_Bx[0][:2].set_color(RED)
        Eq_1_Bx[1][:2].set_color(BLUE)
        Eq_1_Bx[2][1:-1].set_color(GREEN)

        Eq_3_1 = MathTex(r"{{ \{A_y\} }}{{ * -1 * }}{{ \{C_y\} }}{{ = +1}}").next_to(Eq_2_1, DOWN)

        Eq_3_1[0][1:-1].set_color(RED_B)
        Eq_3_1[1][1:-1].set_color(BLUE)
        Eq_3_1[2][1:-1].set_color(GREEN_A)

        self.play(TransformMatchingTex(Eq_1_Ax, Eq_1_Bx))
        self.play(TransformMatchingTex(Eq_3, Eq_3_1))

        Eq_1_Cx = MathTex(r"{{ -1 * }}{{ -1 * }}{{ -1 }}{{ = -1}}").move_to(Eq_1_Bx)

        Eq_1_Cx[0][:2].set_color(RED)
        Eq_1_Cx[1][:2].set_color(BLUE)
        Eq_1_Cx[2].set_color(GREEN)

        Eq_4_1 = MathTex(r"{{ \{A_y\} }}{{ \{B_y\} }}{{ * -1 }}{{ = +1}}").next_to(Eq_3_1, DOWN)

        Eq_4_1[0][1:-1].set_color(RED_B)
        Eq_4_1[1][1:-1].set_color(BLUE_E)
        Eq_4_1[2][1:].set_color(GREEN)

        self.play(TransformMatchingTex(Eq_1_Bx, Eq_1_Cx))
        self.play(TransformMatchingTex(Eq_4, Eq_4_1))
        
        self.wait(13)

        Eq_2_2 = MathTex(r"{{ -1 * }}{{ -1 * }}{{ \{C_y\} }}{{ = +1}}").next_to(Eq_1_Ax, DOWN)

        Eq_2_2[0][:2].set_color(RED)
        Eq_2_2[1][:-1].set_color(BLUE_E)
        Eq_2_2[2][1:-1].set_color(GREEN_A)

        Eq_4_2 = MathTex(r"{{ \{A_y\} }}{{ * -1 }}{{ * -1 }}{{ = +1}}").next_to(Eq_3_1, DOWN)

        Eq_4_2[0][1:-1].set_color(RED_B)
        Eq_4_2[1][1:].set_color(BLUE_E)
        Eq_4_2[2][1:].set_color(GREEN)

        self.play(TransformMatchingTex(Eq_2_1, Eq_2_2))
        self.play(TransformMatchingTex(Eq_4_1, Eq_4_2))

        Eq_2_3 = MathTex(r"{{ -1 * }}{{ -1 * }}{{ +1 }}{{ = +1}}").next_to(Eq_1_Ax, DOWN)

        Eq_2_3[0][:2].set_color(RED)
        Eq_2_3[1][:-1].set_color(BLUE_E)
        Eq_2_3[2].set_color(GREEN_A)

        Eq_3_2 = MathTex(r"{{ \{A_y\} }}{{ * -1 * }}{{ +1 }}{{ = +1}}").next_to(Eq_2_1, DOWN)

        Eq_3_2[0][1:-1].set_color(RED_B)
        Eq_3_2[1][1:-1].set_color(BLUE)
        Eq_3_2[2].set_color(GREEN_A)

        self.play(TransformMatchingTex(Eq_2_2, Eq_2_3))
        self.play(TransformMatchingTex(Eq_3_1, Eq_3_2))
        self.wait(10)

        Eq_3_3 = MathTex(r"{{ -1 }}{{ * -1 * }}{{ +1 }}{{ = +1}}").next_to(Eq_2_1, DOWN)

        Eq_3_2[0].set_color(RED_B)
        Eq_3_2[1][1:-1].set_color(BLUE)
        Eq_3_2[2].set_color(GREEN_A)

        Eq_4_3 = MathTex(r"{{ +1 }}{{ * -1 }}{{ * -1 }}{{ = +1}}").next_to(Eq_3_1, DOWN)

        Eq_4_2[0].set_color(RED_B)
        Eq_4_2[1][1:].set_color(BLUE_E)
        Eq_4_2[2][1:].set_color(GREEN)

        self.play(TransformMatchingTex(Eq_3_2, Eq_3_3))
        self.play(TransformMatchingTex(Eq_4_2, Eq_4_3))
        self.wait(10)

class Contradiction_3(Scene):
    def construct(self):

        Eq_1 = MathTex(r"{{ \{A_x\} }}{{ \{B_x\} }}{{ \{C_x\} }}{{ = -1}}").shift(UP*2)

        Eq_1[0][1:-1].set_color(RED)
        Eq_1[1][1:-1].set_color(BLUE)
        Eq_1[2][1:-1].set_color(GREEN)

        Eq_2 = MathTex(r"{{ \{A_x\} }}{{ \{B_y\} }}{{ \{C_y\} }}{{ = +1}}").next_to(Eq_1, DOWN)

        Eq_2[0][1:-1].set_color(RED)
        Eq_2[1][1:-1].set_color(BLUE_E)
        Eq_2[2][1:-1].set_color(GREEN_A)

        Eq_3 = MathTex(r"{{ \{A_y\} }}{{ \{B_x\} }}{{ \{C_y\} }}{{ = +1}}").next_to(Eq_2, DOWN)

        Eq_3[0][1:-1].set_color(RED_B)
        Eq_3[1][1:-1].set_color(BLUE)
        Eq_3[2][1:-1].set_color(GREEN_A)

        Eq_4 = MathTex(r"{{ \{A_y\} }}{{ \{B_y\} }}{{ \{C_x\} }}{{ = +1}}").next_to(Eq_3, DOWN)

        Eq_4[0][1:-1].set_color(RED_B)
        Eq_4[1][1:-1].set_color(BLUE_E)
        Eq_4[2][1:-1].set_color(GREEN)

        Eqs = VGroup(Eq_1, Eq_2, Eq_3, Eq_4).move_to(ORIGIN)
        
        self.add(Eqs)
        self.wait(9)

        Eq_1_Ax = MathTex(r"{{ -1 * }}{{ \{B_x\} }}{{ \{C_x\} }}{{ = -1}}").move_to(Eq_1)

        Eq_1_Ax[0][:2].set_color(RED)
        Eq_1_Ax[1][1:-1].set_color(BLUE)
        Eq_1_Ax[2][1:-1].set_color(GREEN)

        Eq_2_1 = MathTex(r"{{ -1 * }}{{ \{B_y\} }}{{ \{C_y\} }}{{ = +1}}").next_to(Eq_1_Ax, DOWN)

        Eq_2_1[0][:2].set_color(RED)
        Eq_2_1[1][1:-1].set_color(BLUE_E)
        Eq_2_1[2][1:-1].set_color(GREEN_A)

        self.play(TransformMatchingTex(Eq_1, Eq_1_Ax))
        self.play(TransformMatchingTex(Eq_2, Eq_2_1))

        Eq_1_Bx = MathTex(r"{{ -1 * }}{{ -1 * }}{{ \{C_x\} }}{{ = -1}}").move_to(Eq_1_Ax)

        Eq_1_Bx[0][:2].set_color(RED)
        Eq_1_Bx[1][:2].set_color(BLUE)
        Eq_1_Bx[2][1:-1].set_color(GREEN)

        Eq_3_1 = MathTex(r"{{ \{A_y\} }}{{ * -1 * }}{{ \{C_y\} }}{{ = +1}}").next_to(Eq_2_1, DOWN)

        Eq_3_1[0][1:-1].set_color(RED_B)
        Eq_3_1[1][1:-1].set_color(BLUE)
        Eq_3_1[2][1:-1].set_color(GREEN_A)

        self.play(TransformMatchingTex(Eq_1_Ax, Eq_1_Bx))
        self.play(TransformMatchingTex(Eq_3, Eq_3_1))

        Eq_1_Cx = MathTex(r"{{ -1 * }}{{ -1 * }}{{ -1 }}{{ = -1}}").move_to(Eq_1_Bx)

        Eq_1_Cx[0][:2].set_color(RED)
        Eq_1_Cx[1][:2].set_color(BLUE)
        Eq_1_Cx[2].set_color(GREEN)

        Eq_4_1 = MathTex(r"{{ \{A_y\} }}{{ \{B_y\} }}{{ * -1 }}{{ = +1}}").next_to(Eq_3_1, DOWN)

        Eq_4_1[0][1:-1].set_color(RED_B)
        Eq_4_1[1][1:-1].set_color(BLUE_E)
        Eq_4_1[2][1:].set_color(GREEN)

        self.play(TransformMatchingTex(Eq_1_Bx, Eq_1_Cx))
        self.play(TransformMatchingTex(Eq_4, Eq_4_1))
        
        self.wait(13)

        Eq_2_2 = MathTex(r"{{ -1 * }}{{ -1 * }}{{ \{C_y\} }}{{ = +1}}").next_to(Eq_1_Ax, DOWN)

        Eq_2_2[0][:2].set_color(RED)
        Eq_2_2[1][:-1].set_color(BLUE_E)
        Eq_2_2[2][1:-1].set_color(GREEN_A)

        Eq_4_2 = MathTex(r"{{ \{A_y\} }}{{ * -1 }}{{ * -1 }}{{ = +1}}").next_to(Eq_3_1, DOWN)

        Eq_4_2[0][1:-1].set_color(RED_B)
        Eq_4_2[1][1:].set_color(BLUE_E)
        Eq_4_2[2][1:].set_color(GREEN)

        self.play(TransformMatchingTex(Eq_2_1, Eq_2_2))
        self.play(TransformMatchingTex(Eq_4_1, Eq_4_2))

        Eq_2_3 = MathTex(r"{{ -1 * }}{{ -1 * }}{{ +1 }}{{ = +1}}").next_to(Eq_1_Ax, DOWN)

        Eq_2_3[0][:2].set_color(RED)
        Eq_2_3[1][:-1].set_color(BLUE_E)
        Eq_2_3[2].set_color(GREEN_A)

        Eq_3_2 = MathTex(r"{{ \{A_y\} }}{{ * -1 * }}{{ +1 }}{{ = +1}}").next_to(Eq_2_1, DOWN)

        Eq_3_2[0][1:-1].set_color(RED_B)
        Eq_3_2[1][1:-1].set_color(BLUE)
        Eq_3_2[2].set_color(GREEN_A)

        self.play(TransformMatchingTex(Eq_2_2, Eq_2_3))
        self.play(TransformMatchingTex(Eq_3_1, Eq_3_2))
        self.wait(10)

        Eq_3_3 = MathTex(r"{{ -1 }}{{ * -1 * }}{{ +1 }}{{ = +1}}").next_to(Eq_2_1, DOWN)

        Eq_3_3[0].set_color(RED_B)
        Eq_3_3[1][1:-1].set_color(BLUE)
        Eq_3_3[2].set_color(GREEN_A)

        Eq_4_3 = MathTex(r"{{ +1 }}{{ * -1 }}{{ * -1 }}{{ = +1}}").next_to(Eq_3_1, DOWN)

        Eq_4_3[0].set_color(RED_B)
        Eq_4_3[1][1:].set_color(BLUE_E)
        Eq_4_3[2][1:].set_color(GREEN)

        self.play(TransformMatchingTex(Eq_3_2, Eq_3_3))
        self.play(TransformMatchingTex(Eq_4_2, Eq_4_3))
        self.wait(5)

        Eqs_Final = VGroup(Eq_1_Cx, Eq_2_3, Eq_3_3, Eq_4_3)

        self.play(Eqs_Final.animate.shift(RIGHT*100))


class Contradiction_4(Scene):
    def construct(self):

        Eq_1 = MathTex(r"{{ \{A_x\} }}{{ \{B_x\} }}{{ \{C_x\} }}{{ = -1}}").shift(UP*2)

        Eq_1[0][1:-1].set_color(RED)
        Eq_1[1][1:-1].set_color(BLUE)
        Eq_1[2][1:-1].set_color(GREEN)

        Eq_2 = MathTex(r"{{ \{A_x\} }}{{ \{B_y\} }}{{ \{C_y\} }}{{ = +1}}").next_to(Eq_1, DOWN)

        Eq_2[0][1:-1].set_color(RED)
        Eq_2[1][1:-1].set_color(BLUE_E)
        Eq_2[2][1:-1].set_color(GREEN_A)

        Eq_3 = MathTex(r"{{ \{A_y\} }}{{ \{B_x\} }}{{ \{C_y\} }}{{ = +1}}").next_to(Eq_2, DOWN)

        Eq_3[0][1:-1].set_color(RED_B)
        Eq_3[1][1:-1].set_color(BLUE)
        Eq_3[2][1:-1].set_color(GREEN_A)

        Eq_4 = MathTex(r"{{ \{A_y\} }}{{ \{B_y\} }}{{ \{C_x\} }}{{ = +1}}").next_to(Eq_3, DOWN)

        Eq_4[0][1:-1].set_color(RED_B)
        Eq_4[1][1:-1].set_color(BLUE_E)
        Eq_4[2][1:-1].set_color(GREEN)

        Eqs = VGroup(Eq_1, Eq_2, Eq_3, Eq_4).move_to(ORIGIN)
        
        self.add(Eqs)
        self.wait(9)

        Eq_1_Ax = MathTex(r"{{ -1 * }}{{ \{B_x\} }}{{ \{C_x\} }}{{ = -1}}").move_to(Eq_1)

        Eq_1_Ax[0][:2].set_color(RED)
        Eq_1_Ax[1][1:-1].set_color(BLUE)
        Eq_1_Ax[2][1:-1].set_color(GREEN)

        Eq_2_1 = MathTex(r"{{ -1 * }}{{ \{B_y\} }}{{ \{C_y\} }}{{ = +1}}").next_to(Eq_1_Ax, DOWN)

        Eq_2_1[0][:2].set_color(RED)
        Eq_2_1[1][1:-1].set_color(BLUE_E)
        Eq_2_1[2][1:-1].set_color(GREEN_A)

        self.play(TransformMatchingTex(Eq_1, Eq_1_Ax))
        self.play(TransformMatchingTex(Eq_2, Eq_2_1))

        Eq_1_Bx = MathTex(r"{{ -1 * }}{{ +1 * }}{{ \{C_x\} }}{{ = -1}}").move_to(Eq_1_Ax)

        Eq_1_Bx[0][:2].set_color(RED)
        Eq_1_Bx[1][:2].set_color(BLUE)
        Eq_1_Bx[2][1:-1].set_color(GREEN)

        Eq_3_1 = MathTex(r"{{ \{A_y\} }}{{ * +1 * }}{{ \{C_y\} }}{{ = +1}}").next_to(Eq_2_1, DOWN)

        Eq_3_1[0][1:-1].set_color(RED_B)
        Eq_3_1[1][1:-1].set_color(BLUE)
        Eq_3_1[2][1:-1].set_color(GREEN_A)

        self.play(TransformMatchingTex(Eq_1_Ax, Eq_1_Bx))
        self.play(TransformMatchingTex(Eq_3, Eq_3_1))

        Eq_1_Cx = MathTex(r"{{ -1 * }}{{ +1 * }}{{ +1 }}{{ = -1}}").move_to(Eq_1_Bx)

        Eq_1_Cx[0][:2].set_color(RED)
        Eq_1_Cx[1][:2].set_color(BLUE)
        Eq_1_Cx[2].set_color(GREEN)

        Eq_4_1 = MathTex(r"{{ \{A_y\} }}{{ \{B_y\} }}{{ * +1 }}{{ = +1}}").next_to(Eq_3_1, DOWN)

        Eq_4_1[0][1:-1].set_color(RED_B)
        Eq_4_1[1][1:-1].set_color(BLUE_E)
        Eq_4_1[2][1:].set_color(GREEN)

        self.play(TransformMatchingTex(Eq_1_Bx, Eq_1_Cx))
        self.play(TransformMatchingTex(Eq_4, Eq_4_1))
        
        self.wait(13)

        Eq_2_2 = MathTex(r"{{ -1 * }}{{ -1 * }}{{ \{C_y\} }}{{ = +1}}").next_to(Eq_1_Ax, DOWN)

        Eq_2_2[0][:2].set_color(RED)
        Eq_2_2[1][:-1].set_color(BLUE_E)
        Eq_2_2[2][1:-1].set_color(GREEN_A)

        Eq_4_2 = MathTex(r"{{ \{A_y\} }}{{ * -1 }}{{ * +1 }}{{ = +1}}").next_to(Eq_3_1, DOWN)

        Eq_4_2[0][1:-1].set_color(RED_B)
        Eq_4_2[1][1:].set_color(BLUE_E)
        Eq_4_2[2][1:].set_color(GREEN)

        self.play(TransformMatchingTex(Eq_2_1, Eq_2_2))
        self.play(TransformMatchingTex(Eq_4_1, Eq_4_2))

        Eq_2_3 = MathTex(r"{{ -1 * }}{{ -1 * }}{{ +1 }}{{ = +1}}").next_to(Eq_1_Ax, DOWN)

        Eq_2_3[0][:2].set_color(RED)
        Eq_2_3[1][:-1].set_color(BLUE_E)
        Eq_2_3[2].set_color(GREEN_A)

        Eq_3_2 = MathTex(r"{{ \{A_y\} }}{{ * +1 * }}{{ +1 }}{{ = +1}}").next_to(Eq_2_1, DOWN)

        Eq_3_2[0][1:-1].set_color(RED_B)
        Eq_3_2[1][1:-1].set_color(BLUE)
        Eq_3_2[2].set_color(GREEN_A)

        self.play(TransformMatchingTex(Eq_2_2, Eq_2_3))
        self.play(TransformMatchingTex(Eq_3_1, Eq_3_2))
        self.wait(5)

        Eq_3_3 = MathTex(r"{{ +1  }}{{ * +1 * }}{{ +1 }}{{ = +1}}").next_to(Eq_2_1, DOWN)

        Eq_3_3[0].set_color(RED_B)
        Eq_3_3[1][1:-1].set_color(BLUE)
        Eq_3_3[2].set_color(GREEN_A)

        Eq_4_3 = MathTex(r"{{ -1 }}{{ * -1 }}{{ * +1 }}{{ = +1}}").next_to(Eq_3_1, DOWN)

        Eq_4_3[0].set_color(RED_B)
        Eq_4_3[1][1:].set_color(BLUE_E)
        Eq_4_3[2][1:].set_color(GREEN)

        self.play(TransformMatchingTex(Eq_3_2, Eq_3_3))
        self.wait(2)
        self.play(TransformMatchingTex(Eq_4_2, Eq_4_3))
        self.wait(10) 

class Conclusion(Scene):
    def construct(self):

        Option_1_title = Tex(r"Option 1: Non-Locality")
        Option_1_ul = Underline(Option_1_title)
        Option_1 = VGroup(Option_1_title, Option_1_ul).shift(UP*3)

        Option_2_title = Tex(r"Option 2: Value Indefiniteness")
        Option_2_ul = Underline(Option_2_title)
        Option_2 = VGroup(Option_2_title, Option_2_ul)

        self.play(Write(Option_1))
        self.wait(5)
        self.play(Write(Option_2))
        self.wait(25)


class SuperDeterminism(Scene):
    def construct(self):
        
        Ludwig = ImageMobject(r"media\images\external_images\laser_wittgenstein.jpeg").scale(2)
        vt = ValueTracker(0)
        Ludwig.set_opacity(vt.get_value()) 

        Opacer = always_redraw(lambda: Ludwig.become(Ludwig.set_opacity(min(1, vt.get_value()))))
        vt.add_updater(lambda mob, dt: mob.increment_value(dt/500))

        self.add(Opacer, vt) #Slowly fade in Lasers Ludwig

        Hooft = ImageMobject(r"media\images\external_images\Gerard_'t_Hooft.jpg").shift(LEFT*3).scale(.5)
        Hossenfelder = ImageMobject(r"media\images\external_images\Sabine_Hossenfelder.jpg").shift(RIGHT*3)

        Hossenfelder.height, Hossenfelder.width = Hooft.height, Hooft.width

        self.play(FadeIn(Hooft, Hossenfelder))
        self.wait(5)
        self.play(FadeOut(Hooft, Hossenfelder))

        
        Eq_1 = MathTex(r"{{ \{A_x\} }}{{ \{B_x\} }}{{ \{C_x\} }}{{ = -1}}").shift(UP*2)

        Eq_1[0][1:-1].set_color(RED)
        Eq_1[1][1:-1].set_color(BLUE)
        Eq_1[2][1:-1].set_color(GREEN)

        Eq_2 = MathTex(r"{{ \{A_x\} }}{{ \{B_y\} }}{{ \{C_y\} }}{{ = +1}}").next_to(Eq_1, DOWN)

        Eq_2[0][1:-1].set_color(RED)
        Eq_2[1][1:-1].set_color(BLUE_E)
        Eq_2[2][1:-1].set_color(GREEN_A)

        Eq_3 = MathTex(r"{{ \{A_y\} }}{{ \{B_x\} }}{{ \{C_y\} }}{{ = +1}}").next_to(Eq_2, DOWN)

        Eq_3[0][1:-1].set_color(RED_B)
        Eq_3[1][1:-1].set_color(BLUE)
        Eq_3[2][1:-1].set_color(GREEN_A)

        Eq_4 = MathTex(r"{{ \{A_y\} }}{{ \{B_y\} }}{{ \{C_x\} }}{{ = +1}}").next_to(Eq_3, DOWN)

        Eq_4[0][1:-1].set_color(RED_B)
        Eq_4[1][1:-1].set_color(BLUE_E)
        Eq_4[2][1:-1].set_color(GREEN)

        Eqs = VGroup(Eq_1, Eq_2, Eq_3, Eq_4).move_to(ORIGIN)
        
        self.play(FadeIn(Eqs))
        self.wait(5)

        nEq_1 = MathTex(r"{{ \{A_x\} }}{{ \{B_x\} }}{{ \{C_x\} }}{{ = +1}}").shift(UP*2)

        nEq_1[0][1:-1].set_color(RED)
        nEq_1[1][1:-1].set_color(BLUE)
        nEq_1[2][1:-1].set_color(GREEN)

        nEq_2 = MathTex(r"{{ \{A_x\} }}{{ \{B_y\} }}{{ \{C_y\} }}{{ = -1}}").next_to(nEq_1, DOWN)

        nEq_2[0][1:-1].set_color(RED)
        nEq_2[1][1:-1].set_color(BLUE_E)
        nEq_2[2][1:-1].set_color(GREEN_A)

        nEq_3 = MathTex(r"{{ \{A_y\} }}{{ \{B_x\} }}{{ \{C_y\} }}{{ = -1}}").next_to(nEq_2, DOWN)

        nEq_3[0][1:-1].set_color(RED_B)
        nEq_3[1][1:-1].set_color(BLUE)
        nEq_3[2][1:-1].set_color(GREEN_A)

        nEq_4 = MathTex(r"{{ \{A_y\} }}{{ \{B_y\} }}{{ \{C_x\} }}{{ = -1}}").next_to(nEq_3, DOWN)

        nEq_4[0][1:-1].set_color(RED_B)
        nEq_4[1][1:-1].set_color(BLUE_E)
        nEq_4[2][1:-1].set_color(GREEN)

        Eqs_2 = VGroup(nEq_1, nEq_2, nEq_3, nEq_4).move_to(ORIGIN).set_opacity(.5)

        Eqs_both = VGroup(Eqs, Eqs_2)

        self.play(FadeIn(Eqs_2), Eqs_both.animate.arrange(RIGHT, buff = 1))
        self.wait(2)

        rect_1 = SurroundingRectangle(nEq_1)
        self.play(Write(rect_1))
        self.wait(13)

        rect_2 = SurroundingRectangle(Eq_2)
        self.play(Transform(rect_1, rect_2))
        self.wait(5)

        self.play(FadeOut(rect_1, Eqs_both))

        self.wait(8)

        apple_body = Circle(radius = .25, color = RED)
        apple_body.set_fill(RED, opacity = 1)
        apple_stem = Line(start = apple_body.get_top(), end = apple_body.get_top() + [0, .15, 0], color = DARK_BROWN)
        apple_leaf = Ellipse(width = .125, height = .0625, color = GREEN).move_to(apple_stem.get_center() + [.0625, 0, 0])
        apple_leaf.set_fill(GREEN, opacity = 1)

        apple = VGroup(apple_body, apple_stem, apple_leaf)

        head = Circle(radius=.4, color = WHITE)
        body = Line(start = head.get_bottom(), end = head.get_bottom() - [0, 1, 0])
        arms = Line(start = (1/3)*(2*body.get_top() + body.get_bottom()) - [.5, 0, 0], end = (1/3)*(2*body.get_top() + body.get_bottom()) - [-.5, 0, 0]) 
        left_leg = Line(start = body.get_bottom() , end = body.get_bottom() - [.5, .5, 0])
        right_leg = Line(start = body.get_bottom() , end = body.get_bottom() - [-.5, .5, 0])

        Me = VGroup(head, body, arms, left_leg, right_leg)
        Me.shift(LEFT*2)
        Me.scale(1)

        apple.move_to(arms.get_right())

        Question = Tex(r"?").next_to(head, RIGHT)

        self.play(FadeIn(Me, apple))
        self.wait(3)
        self.play(apple.animate.shift(UP*25))
        self.play(FadeIn(Question))
        self.play(Wiggle(Question))

        self.wait(10)

class Conclusion_2(Scene):
    def construct(self):

        Option_1_title = Tex(r"Option 1: Non-Locality")
        Option_1_ul = Underline(Option_1_title)
        Option_1 = VGroup(Option_1_title, Option_1_ul).shift(UP*3)

        Option_2_title = Tex(r"Option 2: Value Indefiniteness")
        Option_2_ul = Underline(Option_2_title)
        Option_2 = VGroup(Option_2_title, Option_2_ul)

        Option_3_title = Tex(r"Option 3: SuperDeterminism")
        Option_3_ul = Underline(Option_3_title)
        Option_3 = VGroup(Option_3_title, Option_3_ul)

        self.add(Option_1)
        self.add(Option_2)

        self.wait(10)
        self.play(Option_2.animate.shift(UP*1.5), FadeIn(Option_3))
        self.wait(10)







        


