from manim import *

class anim(Scene):
    def construct(self):
    
        template = TexTemplate()
        template.add_to_preamble(r"\usepackage[siunitx, RPvoltages, american, europeanresistors]{circuitikz}")

        stroke = 2
        scale = ValueTracker(0)
        vds = ValueTracker(3)
        vds2 = ValueTracker(0.15)
        vds_adj = 0.05
        jgrpshift = ValueTracker(0)
        jgrpscale = ValueTracker(1)

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

        dot = Dot(radius=0.05, color = YELLOW).shift(LEFT*0.5, UP*1).set_z_index(2)

        self.play(DrawBorderThenFill(JFET),#DrawBorderThenFill(dep1),DrawBorderThenFill(dep2),
                  DrawBorderThenFill(G1),DrawBorderThenFill(G2), DrawBorderThenFill(g1_t),
                  DrawBorderThenFill(g2_t),DrawBorderThenFill(D),
                  DrawBorderThenFill(S), Write(P_1), Write(P_2), Write(N_1))
        self.wait(0.1)
        
        vDS = MathTex(
        r"""\draw(0,0) to[V]  (0,2);""",
        stroke_width=stroke,
        fill_opacity=0,
        stroke_opacity=1,
        tex_environment="circuitikz",
        tex_template=template,
        ).shift(RIGHT*4.5)

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
        ).align_to(g1_t.get_critical_point(DL), UR).shift(DOWN*0.05).set_z_index(1)

        G2lab = MathTex(
        "Gate", 
        stroke_color = BLACK, 
        stroke_width = 0.25,
        stroke_opacity = 1,
        ).align_to(g2_t.get_critical_point(DR), UL).shift(DOWN*0.05).set_z_index(1)

        vds_line1 = Line(
            start=vDS.get_critical_point(UP),
            end=(vDS.get_critical_point(UP)+[0,2.31,0]),
            stroke_width=stroke
        )
        vds_line2 = Line(
            start=(vDS.get_critical_point(UP)+[0.01,2.3,0]),
            end=(vDS.get_critical_point(UP)+[-4.51,2.3,0]),
            stroke_width=stroke
        )
        vds_line3 = Line(
            start=(vDS.get_critical_point(UP)+[-4.5,2.3,0]),
            end=(D.get_critical_point(UP)),
            stroke_width=stroke
        )
        vds_line4 = Line(
            start=vDS.get_critical_point(DOWN),
            end=(vDS.get_critical_point(DOWN)+[0,-2.31,0]),
            stroke_width=stroke
        )
        vds_line5 = Line(
            start=(vDS.get_critical_point(DOWN)+[0.01,-2.3,0]),
            end=(vDS.get_critical_point(DOWN)+[-4.51,-2.3,0]),
            stroke_width=stroke
        )
        vds_line6 = Line(
            start=(vDS.get_critical_point(DOWN)+[-4.5,-2.3,0]),
            end=(S.get_critical_point(DOWN)),
            stroke_width=stroke
        )


        self.play(Write(G2lab),Write(Dlab),Write(Slab),Write(G1lab))
        self.wait(0.1)
        self.play(LaggedStart(Create(vDS),Create(vds_line1),Create(vds_line4),Create(vds_line2),
                              Create(vds_line5),Create(vds_line3),Create(vds_line6),lag_ratio=0.4)
                 )
        self.wait(0.1)

        vGS = MathTex(
        r"""\draw(0,0) to[V]  (0,2);""",
        stroke_width=stroke,
        fill_opacity=0,
        stroke_opacity=1,
        tex_environment="circuitikz",
        tex_template=template,
        ).shift(LEFT*5+DOWN*1.75)

        vgsUP = vGS.get_critical_point(UP)
        vgsDOWN = vGS.get_critical_point(DOWN)
        g1LEFT = g1_t.get_critical_point(LEFT)
        g2RIGHT = g2_t.get_critical_point(RIGHT)
        sDOWN = S.get_critical_point(DOWN)

        vgs_line1 = Line(
            start=vGS.get_critical_point(UP),
            end=([vgsUP[0], g1LEFT[1], 0]),
            stroke_width=stroke
        )
        vgs_line2 = Line(
            start=([vgsUP[0]-0.01, g1LEFT[1], 0]),
            end=(g1LEFT),
            stroke_width=stroke
        )
        of = 0.65
        vgs_line3 = Line(
            start=([g1LEFT[0]-of,  g1LEFT[1], 0]),
            end=([g1LEFT[0]-of,  g1LEFT[1]+of, 0]),
            stroke_width=stroke
        )
        vgs_line7 = Line(
            start=([g1LEFT[0]-of,  g1LEFT[1]+of, 0]),
            end=([g2RIGHT[0]+of,  g2RIGHT[1]+of, 0]),
            stroke_width=stroke
        )
        vgs_line8 = Line(
            start=([g2RIGHT[0]+of,  g2RIGHT[1]+of, 0]),
            end=([g2RIGHT[0]+of,  g2RIGHT[1], 0]),
            stroke_width=stroke
        )
        vgs_line9 = Line(
            start=([g2RIGHT[0]+of,  g2RIGHT[1], 0]),
            end=(g2RIGHT),
            stroke_width=stroke
        )
        offs = 0.46
        vgs_line4 = Line(
            start=vgsDOWN,
            end=([vgsDOWN[0], sDOWN[1]-offs, 0]),
            stroke_width=stroke
        )
        vgs_line5 = Line(
            start=([vgsDOWN[0], sDOWN[1]-offs, 0]),
            end=([sDOWN[0], sDOWN[1]-offs, 0]),
            stroke_width=stroke
        )
        vgs_line6 = Line(
            start=([sDOWN[0], sDOWN[1]-offs, 0]),
            end=([sDOWN[0], sDOWN[1], 0]),
            stroke_width=stroke
        )
        d = Dot([g1LEFT[0]-of,  g1LEFT[1], 0], radius = 0.05, color = WHITE, fill_opacity = 1)
        self.play(LaggedStart(Create(vGS),Create(vgs_line1), Create(vgs_line4), Create(vgs_line2),
                             Create(vgs_line5), Create(d),Create(vgs_line3),Create(vgs_line6),Create(vgs_line7),
                             Create(vgs_line8),Create(vgs_line9),lag_ratio=0.4)
                 )
        self.wait(0.1)



        a1 = always_redraw(lambda:
                ArcBetweenPoints(
                start=interpolate(np.array([-2,1.25,0])     , np.array([-2,2.5,0])      , alpha=(scale.get_value()+(vds2.get_value()))),
                end=interpolate(np.array([-1.25, 0.5,0])  , np.array([-0.5,1.75,0])     , alpha=(scale.get_value()+(vds2.get_value()))),
                angle=-PI/3
            )
        )
        a2 = always_redraw(lambda:
                ArcBetweenPoints(
                start=interpolate(np.array([-1.25, 0.5,0])  , np.array([-0.5,1.75,0])    , alpha=(scale.get_value()+(vds2.get_value()))),
                end=interpolate(np.array([-1.25, -0.5,0]) , np.array([-0.75,-0.75,0])    , alpha=(scale.get_value()+(vds2.get_value()))),
                angle=-PI/3
            )
        )
        a3 = always_redraw(lambda:
                ArcBetweenPoints(
                start=interpolate(np.array([-1.25, -0.5,0]) , np.array([-0.75,-0.75,0])  , alpha=(scale.get_value()+(vds2.get_value()))),
                end=interpolate(np.array([-2,-1.25,0])    , np.array([-2,-1.5,0])        , alpha=(scale.get_value()+(vds2.get_value()))),
                angle=-PI/3.5
            )
        )
        depl_1 = always_redraw(lambda:
            ArcPolygonFromArcs(a1,a2,a3,
        fill_color = GREY_A,
        fill_opacity=0.9).set_z_index(1).scale(jgrpscale.get_value()).align_to(JFET, LEFT)
        )

        b1 = always_redraw(lambda:
                ArcBetweenPoints(
                start=interpolate(np.array([2,1.25,0])     , np.array([2,2.5,0])      , alpha=(scale.get_value()+(vds2.get_value()))),
                end=interpolate(np.array([1.25, 0.5,0])    , np.array([0.5,1.75,0])   , alpha=(scale.get_value()+(vds2.get_value()))),
                angle=PI/3
            )
        )
        b2 = always_redraw(lambda:
                ArcBetweenPoints(
                start=interpolate(np.array([1.25, 0.5,0])  , np.array([0.5,1.75,0])   , alpha=(scale.get_value()+(vds2.get_value()))),
                end=interpolate(np.array([1.25, -0.5,0])   , np.array([0.75,-0.75,0]) , alpha=(scale.get_value()+(vds2.get_value()))),
                angle=PI/3
            )
        )
        b3 = always_redraw(lambda:
                ArcBetweenPoints(
                start=interpolate(np.array([1.25, -0.5,0]) , np.array([0.75,-0.75,0]) , alpha=(scale.get_value()+(vds2.get_value()))),
                end=interpolate(np.array([2,-1.25,0])      , np.array([2,-1.5,0])     , alpha=(scale.get_value()+(vds2.get_value()))),
                angle=PI/3.5 
            )
        )
        depl_2 = always_redraw(lambda:
            ArcPolygonFromArcs(b1,b2,b3,
        fill_color = GREY_A,
        fill_opacity=0.9).set_z_index(1).scale(jgrpscale.get_value()).shift(LEFT*jgrpshift.get_value())
        ).scale(jgrpscale.get_value()).align_to(JFET, LEFT)

        VGS_text = MathTex("V_{GS} = ").scale(0.7).next_to(vGS)
        number = always_redraw(lambda:DecimalNumber(
                 (0-(scale.get_value()*3)), 
                 show_ellipsis=False, 
                 num_decimal_places=1
                 ).scale(0.7).next_to(VGS_text, RIGHT))

        VDS_text = MathTex("V_{DS} = ").next_to(vDS).shift(LEFT*0.2).scale(0.7)
        number2 = always_redraw(lambda:DecimalNumber(
                 vds.get_value(), 
                 show_ellipsis=False, 
                 num_decimal_places=1
                 ).scale(0.7).next_to(VDS_text, RIGHT))

        i_arr = always_redraw(lambda:
        #    Arrow( start = UP*(1),#+np.sin(3*e.get_value())),
        #           end = DOWN*(1),#+np.sin(3*e.get_value())),
        #           color = YELLOW,
        #           stroke_width=5,
           Polygon(       
               [-0.25,0.5,0],[0.25,0.5,0],[0.25,-0.5,0],[0.65,-0.5,0],[0,-1,0],[-0.65,-0.5,0],[-0.25,-0.5,0],[-0.25,0.5,0],
                color = WHITE,
                fill_color = YELLOW,
                fill_opacity = 0.65,
                stroke_width=2,
           ).scale(1.5-((scale.get_value()+(vds.get_value()*vds_adj)))*0.7).set_z_index(2).scale(jgrpscale.get_value()).shift(LEFT*jgrpshift.get_value())
           ) 
        
        self.play(FadeIn(depl_1), FadeIn(depl_2), FadeIn(VGS_text), FadeIn(number), FadeIn(VDS_text), FadeIn(number2), FadeIn(i_arr))
        self.wait(0.1)
        self.play(scale.animate.set_value(0.7), run_time = 5)
        self.wait(0.1)
        self.play(scale.animate.set_value(0.3), run_time = 5)
        self.wait(0.1)
        self.play(scale.animate.set_value(0.5), run_time = 5)
        self.wait(0.1)
        self.play(vds.animate.set_value(4), vds2.animate.set_value(0.2), run_time = 2) 
        self.wait(0.1)
        self.play(vds.animate.set_value(2), vds2.animate.set_value(0.1), run_time = 2)
        self.wait(0.1)
        self.play(vds.animate.set_value(3), vds2.animate.set_value(0.15), run_time = 2)
        self.wait(0.1)
        self.play(scale.animate.set_value(0.75), run_time = 2)
        self.wait(0.1)
        self.play(vds.animate.set_value(8), vds2.animate.set_value(0.55), run_time = 3)
        self.wait(0.1)
        self.play(vds.animate.set_value(3), vds2.animate.set_value(0.15), run_time = 3)
        self.wait(0.1)
        self.play(scale.animate.set_value(0.5), run_time = 2)
        self.wait(0.1)

        JGRP = VGroup(JFET, D, S, g1_t, g2_t, G1, G2, G2lab, Dlab, Slab, G1lab, P_1, P_2, N_1,i_arr, depl_1, depl_2)
        J2 = VGroup(i_arr, depl_1, depl_2)
        REMOVE = VGroup(VGS_text, number,number2,VDS_text,vGS,vgs_line1,vgs_line2,vgs_line3,vgs_line4,vgs_line5,vgs_line6,vgs_line7,vgs_line8,vgs_line9,
                        vDS,vds_line1,vds_line2,vds_line3,vds_line4,vds_line5,vds_line6, d)
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
        ).scale(0.75).shift(RIGHT*2)

        self.play(FadeTransform(REMOVE, f), JGRP.animate.scale(0.65).shift(LEFT*5))        
        self.wait(1)
        
        
        