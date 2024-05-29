from manim import *

class anim(Scene):
    def construct(self):

        template = TexTemplate()
        template.add_to_preamble(r"\usepackage[siunitx, RPvoltages, american, europeanresistors]{circuitikz}")
        
        stroke = 2
        scale = ValueTracker(0.5)
        vds = ValueTracker(3)
        vds2 = ValueTracker(0.15)
        vds_adj = 0.05
        #jgrpshift = ValueTracker(0)
        #jgrpscale = ValueTracker(1)
        shiftVec = [-5,0,0]
        scaleVec = 0.65
        
        JFET = Rectangle(
            width=4,
            height=6,
            fill_color=BLUE_A,
            fill_opacity=1
        ).set_z_index(1)

        G1 = ArcBetweenPoints(
            start=UP*1.25,
            end = DOWN*1.25,
            angle = -PI/1.25,
            fill_color=RED_A,
            fill_opacity=0.85
        ).align_to(JFET,LEFT).set_z_index(2)

        G2 = ArcBetweenPoints(
            start=UP*1.25,
            end = DOWN*1.25,
            angle = PI/1.25,
            fill_color=RED_A,
            fill_opacity=0.85
        ).align_to(JFET,RIGHT).set_z_index(2)

        g1_t = Rectangle(
            width=0.25,
            height=0.5,
            fill_color=GREY,
            fill_opacity=1,
            stroke_width=1
        ).align_to(G1.get_critical_point(LEFT),RIGHT).set_z_index(1)

        g2_t = Rectangle(
            width=0.25,
            height=0.5,
            fill_color=GREY,
            fill_opacity=1,
            stroke_width=1
        ).align_to(G2.get_critical_point(RIGHT),LEFT).set_z_index(1)

        S = Rectangle(
            width=0.5,
            height=0.25,
            fill_color=GREY,
            fill_opacity=1,
            stroke_width=1
        ).align_to(JFET.get_critical_point(DOWN),UP).set_z_index(1)

        D = Rectangle(
            width=0.5,
            height=0.25,
            fill_color=GREY,
            fill_opacity=1,
            stroke_width=1
        ).align_to(JFET.get_critical_point(UP),DOWN).set_z_index(1)

        P_1 = MathTex(
        "P", 
        stroke_color = BLACK, 
        stroke_width = 0.25,
        stroke_opacity = 1,
        ).align_to(G1, LEFT,).shift(RIGHT*0.1).set_z_index(2)

        P_2 = MathTex(
        "P", 
        stroke_color = BLACK, 
        stroke_width = 0.25,
        stroke_opacity = 1,
        ).align_to(G2, RIGHT).shift(LEFT*0.1).set_z_index(2)

        N_1 = MathTex(
        "N", 
        stroke_color = BLACK, 
        stroke_width = 0.25,
        stroke_opacity = 1,
        ).align_to(JFET.get_critical_point(UL), UL).shift(DR*0.2).set_z_index(2)
        
        Dlab = MathTex(
        "Drain", 
        stroke_color = BLACK, 
        stroke_width = 0.25,
        stroke_opacity = 1,
        ).align_to(D.get_critical_point(UR), DL).shift(DOWN*0.1).set_z_index(1)

        Slab = MathTex(
        "Source", 
        stroke_color = BLACK, 
        stroke_width = 0.25,
        stroke_opacity = 1,
        ).align_to(S.get_critical_point(DR), UL).shift(UP*0.1).set_z_index(1)

        G1lab = MathTex(
        "Gate", 
        stroke_color = BLACK, 
        stroke_width = 0.25,
        stroke_opacity = 1,
        ).align_to(g1_t.get_critical_point(UL), DR).shift(DOWN*0.05).set_z_index(1)

        G2lab = MathTex(
        "Gate", 
        stroke_color = BLACK, 
        stroke_width = 0.25,
        stroke_opacity = 1,
        ).align_to(g2_t.get_critical_point(UR), DL).shift(DOWN*0.05).set_z_index(1)
        dot = Dot(radius=0.05, color = YELLOW).shift(LEFT*0.5, UP*1).set_z_index(2)

        # self.play(DrawBorderThenFill(JFET),#DrawBorderThenFill(dep1),DrawBorderThenFill(dep2),
        #           DrawBorderThenFill(G1),DrawBorderThenFill(G2), DrawBorderThenFill(g1_t),
        #           DrawBorderThenFill(g2_t),DrawBorderThenFill(D),
        #           DrawBorderThenFill(S), Write(P_1), Write(P_2), Write(N_1))
        # self.wait(0.1)
        a11=np.array([-2,1.25,0])*scaleVec+shiftVec
        a12=np.array([-2,2.5,0])*scaleVec+shiftVec
        
        a21=np.array([-1.25, 0.5,0])*scaleVec+shiftVec
        a22=np.array([-0.5,1.75,0])*scaleVec+shiftVec
        
        a31=np.array([-1.25, -0.5,0])*scaleVec+shiftVec
        a32=np.array([-0.75,-0.75,0])*scaleVec+shiftVec
        
        a41=np.array([-2,-1.25,0])*scaleVec+shiftVec
        a42=np.array([-2,-1.5,0])*scaleVec+shiftVec
        
        a1 = always_redraw(lambda:
                ArcBetweenPoints(
                start=interpolate((a11), (a12), alpha=(scale.get_value()+(vds2.get_value()))),
                end=interpolate((a21), (a22), alpha=(scale.get_value()+(vds2.get_value()))),
                angle=-PI/3
            )
        )
        a2 = always_redraw(lambda:
                ArcBetweenPoints(
                start=interpolate((a21), (a22), alpha=(scale.get_value()+(vds2.get_value()))),
                end=interpolate((a31), (a32), alpha=(scale.get_value()+(vds2.get_value()))),
                angle=-PI/3
            )
        )
        a3 = always_redraw(lambda:
                ArcBetweenPoints(
                start=interpolate((a31), (a32), alpha=(scale.get_value()+(vds2.get_value()))),
                end=interpolate((a41), (a42), alpha=(scale.get_value()+(vds2.get_value()))),
                angle=-PI/3.5
            )
        )
        depl_1 = always_redraw(lambda:
            ArcPolygonFromArcs(a1,a2,a3,
        fill_color = GREY_A,
        fill_opacity=0.9).set_z_index(1)
        )
        
        b11=np.array([2,1.25,0])*scaleVec+shiftVec
        b12=np.array([2,2.5,0])*scaleVec+shiftVec
        
        b21=np.array([1.25, 0.5,0])*scaleVec+shiftVec
        b22=np.array([0.5,1.75,0])*scaleVec+shiftVec
        
        b31=np.array([1.25, -0.5,0])*scaleVec+shiftVec
        b32=np.array([0.75,-0.75,0])*scaleVec+shiftVec
        
        b41=np.array([2,-1.25,0])*scaleVec+shiftVec
        b42=np.array([2,-1.5,0])*scaleVec+shiftVec

        b1 = always_redraw(lambda:
                ArcBetweenPoints(
                start=interpolate((b11), (b12), alpha=(scale.get_value()+(vds2.get_value()))),
                end=interpolate((b21), (b22), alpha=(scale.get_value()+(vds2.get_value()))),
                angle=PI/3
            )
        )
        b2 = always_redraw(lambda:
                ArcBetweenPoints(
                start=interpolate((b21), (b22), alpha=(scale.get_value()+(vds2.get_value()))),
                end=interpolate((b31), (b32), alpha=(scale.get_value()+(vds2.get_value()))),
                angle=PI/3
            )
        )
        b3 = always_redraw(lambda:
                ArcBetweenPoints(
                start=interpolate((b31), (b32), alpha=(scale.get_value()+(vds2.get_value()))),
                end=interpolate((b41), (b42), alpha=(scale.get_value()+(vds2.get_value()))),
                angle=PI/3.5
            )
        )
        depl_2 = always_redraw(lambda:
            ArcPolygonFromArcs(b1,b2,b3,
        fill_color = GREY_A,
        fill_opacity=0.9).set_z_index(1)
        )
        
        i_arr = always_redraw(lambda:
           Polygon(       
               (np.array([-0.25,0.5,0])*scaleVec)+shiftVec ,
               (np.array([0.25,0.5,0])*scaleVec)+shiftVec ,
               (np.array([0.25,-0.5,0])*scaleVec)+shiftVec ,
               (np.array([0.65,-0.5,0])*scaleVec)+shiftVec ,
               (np.array([0,-1,0])*scaleVec)+shiftVec ,
               (np.array([-0.65,-0.5,0])*scaleVec)+shiftVec ,
               (np.array([-0.25,-0.5,0])*scaleVec)+shiftVec ,
               (np.array([-0.25,0.5,0])*scaleVec)+shiftVec ,
                color = WHITE,
                fill_color = YELLOW,
                fill_opacity = 0.65,
                stroke_width=2,
           ).scale(1.5-((scale.get_value()+(vds.get_value()*vds_adj)))*0.7).set_z_index(2)
           ) 
        
        JGRP = VGroup(JFET, D, S, g1_t, g2_t, G1, G2, P_1, P_2, N_1, 
                      G2lab, Dlab, Slab, G1lab).shift(LEFT*5).scale(0.65)#, i_arr, depl_1, depl_2)
        
        f = MathTex(
        r"""\draw (-2,0) to[short] ++(3,0)
        node[op amp, noinv input down, anchor=-] (OA){\texttt{}}
        (OA.-) to[short] (0,0) to[short] (0, 1.5) 
        (OA.out) to[short] ++(0.12, 0) coordinate(OAo) to[short] (3.5,1.5)
        (OA.+) to[short] ++(-0.5,0) to[short] (0.5,-2);""",
        r"""\draw (-2,-1.5) node[nmos](nmos){}
                  (-2,0) to [short](nmos.D)
                  (nmos.S) to [short](-2,-2.5)  
                  (nmos.G) to [short](-3,-2.5)  ;""",
        r"""\draw (-2,-2.5) to[short] (-2,-4) node[ground]{};""",
        r"""\draw (-3,-2.5) to[R=$R_5$] (-3,-4) node[ground]{};""",
        r"""\draw (0,1.5) to[R=$R_2$] (3.5,1.5);""",
        r"""\draw (0.5,-2) to [short] (-0.5,-2) to[short] (1.5,-2)
                  (-0.5,-2) to[C=$C_2$] (-0.5,-4)
                  (1.5,-2) to[R=$R_4$] (1.5,-4) 
                  (-0.5,-4) to[short] (0.5,-4) 
                  node[ground]{} to(1.5,-4);""",
        r"""\draw (3.5,-0.5) to[R=$R_3$] (3.5,-2) 
                  (3.5,-2) to[C=$C_1$] (1.5,-2);""",
        stroke_width=stroke,
        fill_opacity=0,
        stroke_opacity=1,
        tex_environment="circuitikz",
        tex_template=template,
        ).scale(0.75).shift(RIGHT*2).set_z_index(1)
        
        g = MathTex(
        r"""\draw (-2,0) to[short] ++(3,0)
        node[op amp, noinv input down, anchor=-] (OA){\texttt{}}
        (OA.-) to[short] (0,0) to[short] (0, 1.5) 
        (OA.out) to[short] ++(0.12, 0) coordinate(OAo) to[short] (3.5,1.5)
        (OA.+) to[short] ++(-0.5,0) to[short] (0.5,-2);""",
        r"""\draw (-2,-1.5) node[nmos](nmos){}
                  (-2,0) to [short](nmos.D)
                  (nmos.S) to [short](-2,-2.5)  
                  (nmos.G) to [short](-3,-2.5)  ;""",
        r"""\draw (-2,-2.5) to[R=$R_1$] (-2,-4) node[ground]{};""",
        r"""\draw (-3,-2.5) to[R=$R_5$] (-3,-4) node[ground]{};""",
        r"""\draw (0,1.5) to[R=$R_2$] (3.5,1.5);""",
        r"""\draw (0.5,-2) to [short] (-0.5,-2) to[short] (1.5,-2)
                  (-0.5,-2) to[C=$C_2$] (-0.5,-4)
                  (1.5,-2) to[R=$R_4$] (1.5,-4) 
                  (-0.5,-4) to[short] (0.5,-4) 
                  node[ground]{} to(1.5,-4);""",
        r"""\draw (3.5,-0.5) to[R=$R_3$] (3.5,-2) 
                  (3.5,-2) to[C=$C_1$] (1.5,-2);""",
        stroke_width=stroke,
        fill_opacity=0,
        stroke_opacity=1,
        tex_environment="circuitikz",
        tex_template=template,
        ).scale(0.75).shift(RIGHT*2).set_z_index(1)
        
        self.play(FadeIn(JGRP), FadeIn(depl_1), FadeIn(depl_2), FadeIn(i_arr), FadeIn(f))
        self.wait(0.1)
        # self.play(vds.animate.set_value(3), vds2.animate.set_value(0.15), scale.animate.set_value(0.5))
        # self.wait(0.1)
        
        d = Dot(radius = 0.05).shift(DOWN*-1.31+LEFT*0.64)
        self.play(FadeIn(d))
        
        JFETs = [-0.64, -1.06, 0]
        JFETd = [-0.64, 1.31, 0]
        JFETg = [-1.68, -0.28, 0]
        g1LEFT = g1_t.get_critical_point(LEFT)
        g2RIGHT = g2_t.get_critical_point(RIGHT)
        sDOWN = S.get_critical_point(DOWN)
        dUP = D.get_critical_point(UP)
        
        l1 = Line(
            start= g2_t.get_critical_point(RIGHT),
            end = [g2RIGHT[0]+0.51, g2RIGHT[1] ,0],
            stroke_width=stroke
        )
        l2 = Line(
            start= g2_t.get_critical_point(RIGHT),
            end = [g1LEFT[0]-0.51, g1LEFT[1] ,0],
            stroke_width=stroke
        )
        l3 = Line(
            start= [g2RIGHT[0]+0.5, g2RIGHT[1] ,0],
            end = [g2RIGHT[0]+0.5, JFETg[1]+0.01 ,0],
            stroke_width=stroke           
        )
        l4 = Line(
            start= [g1LEFT[0]-0.5, g1LEFT[1] ,0],
            end = [g1LEFT[0]-0.5, JFETg[1]+0.01 ,0],
            stroke_width=stroke
        )
        l5 = Line(
            start = [g2RIGHT[0]+0.5, JFETg[1] ,0],
            end = [JFETg[0], JFETg[1], 0],
            stroke_width=stroke
        )
        l6 = Line(
            start= [g1LEFT[0]-0.5, JFETg[1] ,0],
            end = [g2RIGHT[0]+0.5, JFETg[1] ,0],
            stroke_width=stroke
        )
        d1 = Dot([g2RIGHT[0]+0.5, JFETg[1] ,0], radius = 0.05, color = WHITE, fill_opacity = 1)
        d2 = Dot([JFETg[0], JFETg[1], 0], radius = 0.05, color = WHITE, fill_opacity = 1)

        l7 = Line(
            start= dUP,
            end = [dUP[0], dUP[1] + 0.5 ,0],
            stroke_width=stroke
        )
        l8 = Line(
            start= sDOWN,
            end = [sDOWN[0], sDOWN[1] - 0.5,0],
            stroke_width=stroke
        )
        l9 = Line(
            start= [dUP[0]-0.01, dUP[1] + 0.5 ,0],
            end = [JFETd[0], dUP[1] + 0.5 ,0],
            stroke_width=stroke
        )
        l10 = Line(
            start= [sDOWN[0]-0.01, sDOWN[1] - 0.5,0],
            end = [g2RIGHT[0]+0.5, sDOWN[1] - 0.5,0],
            stroke_width=stroke
        )
        l11 = Line(
            start= [JFETd[0], dUP[1] + 0.51 ,0],
            end = JFETd,
            stroke_width=stroke
        )
        d3 = Dot(JFETd, radius = 0.05, color = WHITE, fill_opacity = 1)

        l12 = Line(
            start= [g2RIGHT[0]+0.5, sDOWN[1] - 0.5,0],
            end = [g2RIGHT[0]+0.5, JFETs[1],0],
            stroke_width=stroke
        )
        
        l13 = Line(
            start= [g2RIGHT[0]+0.5, JFETs[1],0],
            end = JFETs,
            stroke_width=stroke
        )
        d4 = Dot(JFETs, radius = 0.05, color = WHITE, fill_opacity = 1)
        aniline = Line(
            start= l11.get_start(),
            end = [JFETd[0], sDOWN[1] - 1,0],
            stroke_width=0
        )
        self.play(LaggedStart(Create(l1),Create(l2),Create(l7),Create(l8),Create(l3),Create(l4),Create(l9),Create(l10),
                              Create(l5),Create(d2),Create(l11),Create(d3),Create(l6),
                              Create(l12),Create(d1),Create(l13),Create(d4),lag_ratio=0.2)
                 )
        self.wait(0.1)
        self.add(aniline)
        self.play(vds.animate.set_value(3), vds2.animate.set_value(0.15), scale.animate.set_value(0))
        self.wait(0.1)
        
        animdot=Dot(radius=0).move_to(aniline.get_start()) 
               
        i_arr2 = always_redraw(lambda:
           Polygon(       
               (np.array([-0.25,0.5,0])*scaleVec)+animdot.get_center() ,
               (np.array([0.25,0.5,0])*scaleVec)+animdot.get_center() ,
               (np.array([0.25,-0.5,0])*scaleVec)+animdot.get_center() ,
               (np.array([0.65,-0.5,0])*scaleVec)+animdot.get_center() ,
               (np.array([0,-1,0])*scaleVec)+animdot.get_center() ,
               (np.array([-0.65,-0.5,0])*scaleVec)+animdot.get_center() ,
               (np.array([-0.25,-0.5,0])*scaleVec)+animdot.get_center() ,
               (np.array([-0.25,0.5,0])*scaleVec)+animdot.get_center() ,
                color = WHITE,
                fill_color = YELLOW,
                fill_opacity = 0.65,
                stroke_width=2,
           ).scale(1.5-((scale.get_value()+(vds.get_value()*vds_adj)))*0.7).set_z_index(2)
           ) 
        
        path=VGroup(l8,l10,l12)
        self.play(FadeTransform(f,g))
        self.wait(0.1)
        self.play(FadeTransform(i_arr.copy(), i_arr2))
        self.wait(0.1)
        self.play(MoveAlongPath(animdot, aniline), run_time=2)
        self.wait(0.1)
        self.play(FadeOut(i_arr2), animdot.animate.move_to(aniline.get_start()))
        self.wait(0.1)
        
        VGS_text = MathTex("V_{GS}=").scale(0.6).next_to(G2lab).shift(UP*0.1)
        number1 = always_redraw(lambda:DecimalNumber(
                 (0-(scale.get_value()*3)), 
                 show_ellipsis=False, 
                 num_decimal_places=1
                 ).scale(0.6).next_to(VGS_text, RIGHT))
        
        VS_text = MathTex("V_{S}=").scale(0.6).next_to(d4).shift(LEFT*0.15)
        number2 = always_redraw(lambda:DecimalNumber(
                 ((scale.get_value()*3)), 
                 show_ellipsis=False, 
                 num_decimal_places=1
                 ).scale(0.6).next_to(VS_text, RIGHT))
        
        VG_text = MathTex("V_{G}=").scale(0.6).next_to(G2lab).shift(DOWN*1).shift(LEFT*0.25)
        number3 = always_redraw(lambda:DecimalNumber(0,show_ellipsis=False, 
                 num_decimal_places=0).scale(0.6).next_to(VG_text, RIGHT))
        
        i_arr3 = always_redraw(lambda:
           Polygon(       
               (np.array([-0.25,0.5,0])*scaleVec)+animdot.get_center() ,
               (np.array([0.25,0.5,0])*scaleVec)+animdot.get_center() ,
               (np.array([0.25,-0.5,0])*scaleVec)+animdot.get_center() ,
               (np.array([0.65,-0.5,0])*scaleVec)+animdot.get_center() ,
               (np.array([0,-1,0])*scaleVec)+animdot.get_center() ,
               (np.array([-0.65,-0.5,0])*scaleVec)+animdot.get_center() ,
               (np.array([-0.25,-0.5,0])*scaleVec)+animdot.get_center() ,
               (np.array([-0.25,0.5,0])*scaleVec)+animdot.get_center() ,
                color = WHITE,
                fill_color = YELLOW,
                fill_opacity = 0.65,
                stroke_width=2,
           ).scale(1.5-((scale.get_value()+(vds.get_value()*vds_adj)))).set_z_index(2)
           )
        anilinehalf = Line(
            start= aniline.get_start(),
            end = aniline.get_center(),
            stroke_width=0
        )
        anilinehalf2 = Line(
            start= aniline.get_center(),
            end = aniline.get_end(),
            stroke_width=0
        )
        anilineq1 = Line(
            start= anilinehalf.get_start(),
            end = anilinehalf.get_center(),
            stroke_width=0
        )
        anilineq2 = Line(
            start= anilinehalf.get_center(),
            end = aniline.get_center(),
            stroke_width=0
        )
        anilineq3 = Line(
            start= anilinehalf2.get_start(),
            end = anilinehalf2.get_center(),
            stroke_width=0
        )
        anilineq4 = Line(
            start= anilinehalf2.get_center(),
            end = aniline.get_end(),
            stroke_width=0
        )
        self.play(FadeTransform(i_arr.copy(), i_arr3), FadeIn(VGS_text), FadeIn(number1), FadeIn(VS_text), FadeIn(number2), FadeIn(VG_text), FadeIn(number3))
        self.wait(0.1)
        self.play(MoveAlongPath(animdot, aniline), scale.animate.set_value(0.7), run_time=5)
        self.wait(0.1)
        self.play(i_arr3.animate.set_opacity(0), animdot.animate.move_to(aniline.get_start()))
        self.wait(0.1)
        self.play(MoveAlongPath(animdot, aniline), scale.animate.set_value(0.3), run_time=5)
        self.wait(0.1)
        self.play(i_arr3.animate.set_opacity(0), animdot.animate.move_to(aniline.get_start()))
        self.wait(0.1)
        self.play(MoveAlongPath(animdot, anilineq1), scale.animate.set_value(0.65), run_time=2, rate_func=linear)
        self.play(MoveAlongPath(animdot, anilineq2), scale.animate.set_value(0.38), run_time=2, rate_func=linear)
        self.play(MoveAlongPath(animdot, anilineq3), scale.animate.set_value(0.54), run_time=2, rate_func=linear)
        self.play(MoveAlongPath(animdot, anilineq4), scale.animate.set_value(0.49), run_time=2, rate_func=linear)
        self.wait(0.1)
        self.play(FadeOut(i_arr3), animdot.animate.move_to(aniline.get_start()), scale.animate.set_value(0))
        self.wait(0.1)

        COLOR = BLUE_A

        gain_text = MathTex("G=1+", color=(COLOR)).scale(1).shift(LEFT*3.5+UP*3.25).set_z_index(1)
        
        t2 = MathTex("\\_\\_", color=(COLOR), stroke_color = WHITE).move_to(gain_text.get_critical_point(RIGHT)+[0.5,-0.0275,0]).set_z_index(1)
        t1 = MathTex("R_2", color=(COLOR), stroke_color = WHITE).move_to(t2.get_critical_point(DOWN)+[0,0.3,0]).set_z_index(1)
        t3 = MathTex("R_1", color=(COLOR), stroke_color = WHITE).move_to(t2.get_critical_point(DOWN)+[0,-0.3,0]).set_z_index(1)
        t2_2 = MathTex("\\_\\_\\_\\_", color=(COLOR), stroke_color = WHITE).move_to(gain_text.get_critical_point(RIGHT)+[0.9,-0.0275,0]).set_z_index(1)
        t1_2 = MathTex("R_2", color=(COLOR), stroke_color = WHITE).move_to(t2_2.get_critical_point(DOWN)+[0,0.3,0]).set_z_index(1)
        t4 = MathTex("R_1+", color=(COLOR), stroke_color = WHITE).move_to(t2_2.get_critical_point(DOWN)+[-0.35,-0.3,0]).set_z_index(1)
        t5 = MathTex("R_{JF}", color=(COLOR), stroke_color = WHITE).move_to(t4.get_critical_point(RIGHT)+[0.5,-0.0250,0]).set_z_index(1)
        # dot = Dot(gain_text.get_critical_point(RIGHT))
        # self.play(FadeIn(dot))
        trimmer = 550
        gnum = always_redraw(lambda:DecimalNumber(
                 (200+(scale.get_value()*trimmer)), 
                 show_ellipsis=False, 
                 num_decimal_places=0,
                 color=(COLOR), stroke_color = WHITE
                 ).scale(1).move_to(t4.get_critical_point(RIGHT)+[0.750,0 ,0]).set_z_index(1)
        )

        gainGRP = VGroup(t2,t1,gnum)
        self.play(FadeIn(gain_text), FadeIn(t2),FadeIn(t1),FadeIn(t3))
        self.wait(0.1)
        self.play(FadeTransform(t3, t4), FadeTransform(t2, t2_2), FadeTransform(t1, t1_2), FadeIn(t5, run_time = 1.5))
        self.wait(1)
        #self.play()
        #self.wait(0.1)

        t2_3 = MathTex("\\_\\_\\_\\_\\_\\_", color=(COLOR), stroke_color = WHITE).move_to(gain_text.get_critical_point(RIGHT)+[1.25,-0.0275,0]).set_z_index(2)
        t1_3 = MathTex("20k", color=(COLOR), stroke_color = WHITE).move_to(t2_3.get_critical_point(DOWN)+[0,0.3,0]).set_z_index(2)
        t4_2 = MathTex("9.5k+", color=(COLOR), stroke_color = WHITE).move_to(t2_3.get_critical_point(DOWN)+[-0.5,-0.3,0]).set_z_index(2)

        t6 = MathTex("=", color=(COLOR), stroke_color = WHITE).move_to(t2_3.get_critical_point(RIGHT)+[0.45,0,0]).set_z_index(2)

        
        gnum2 = always_redraw(lambda:DecimalNumber(
                 (1+(20000/(9500+(200+(scale.get_value()*trimmer))))), 
                 show_ellipsis=False, 
                 num_decimal_places=2,
                 color=(COLOR), stroke_color = WHITE
                 ).scale(1).move_to(t6.get_critical_point(RIGHT)+[0.50,0 ,0]).set_z_index(2)
        )
        i_arr4 = always_redraw(lambda:
           Polygon(       
               (np.array([-0.25,0.5,0])*scaleVec)+animdot.get_center() ,
               (np.array([0.25,0.5,0])*scaleVec)+animdot.get_center() ,
               (np.array([0.25,-0.5,0])*scaleVec)+animdot.get_center() ,
               (np.array([0.65,-0.5,0])*scaleVec)+animdot.get_center() ,
               (np.array([0,-1,0])*scaleVec)+animdot.get_center() ,
               (np.array([-0.65,-0.5,0])*scaleVec)+animdot.get_center() ,
               (np.array([-0.25,-0.5,0])*scaleVec)+animdot.get_center() ,
               (np.array([-0.25,0.5,0])*scaleVec)+animdot.get_center() ,
                color = WHITE,
                fill_color = YELLOW,
                fill_opacity = 0.65,
                stroke_width=2,
           ).scale(1.5-((scale.get_value()+(vds.get_value()*vds_adj)))).set_z_index(1)
           )
        
        self.play(FadeTransform(t1_2, t1_3), FadeTransform(t2_2, t2_3), FadeTransform(t4, t4_2), FadeIn(t6),FadeTransform(t5, gnum), FadeIn(gnum2))
        self.wait(0.1)
        self.play(FadeTransform(i_arr.copy(), i_arr4))
        self.wait(0.1)
        self.play(MoveAlongPath(animdot, anilineq1), scale.animate.set_value(0.65), run_time=2, rate_func=linear)
        self.play(MoveAlongPath(animdot, anilineq2), scale.animate.set_value(0.38), run_time=2, rate_func=linear)
        self.play(MoveAlongPath(animdot, anilineq3), scale.animate.set_value(0.54), run_time=2, rate_func=linear)
        self.play(MoveAlongPath(animdot, anilineq4), scale.animate.set_value(0.505), run_time=2, rate_func=linear)
        self.wait(0.1)
        