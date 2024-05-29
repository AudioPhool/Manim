from manim import *

class anim(Scene):
    def construct(self):
        # Create boxes and labels
        sysclk_box = Rectangle(width=3.5, height=1.5,fill_color = ORANGE, fill_opacity=0.7, stroke_width = 4, stroke_color = YELLOW).shift(LEFT*5.25)
        sysclk_label = Text("SYSCLK = 8MHz").scale(0.5).move_to(sysclk_box)
        prescaler_box = Rectangle(width=3.5, height=1.5,fill_color = TEAL, fill_opacity=0.7, stroke_width = 4, stroke_color = YELLOW).next_to(sysclk_box, RIGHT, buff=1.5)
        prescaler_label = Text("PRESCALER").scale(0.5).move_to(prescaler_box)
        counter_box = Rectangle(width=3.5, height=1.5,fill_color = PURPLE, fill_opacity=0.7, stroke_width = 4, stroke_color = YELLOW).next_to(prescaler_box, RIGHT, buff=1.5)
        counter_label = Text("COUNTER").scale(0.5).move_to(counter_box)
        prescaler_display = DecimalNumber(0, num_decimal_places=0).scale(1).next_to(prescaler_box, DOWN)
        counter_display = DecimalNumber(0, num_decimal_places=0).scale(1).next_to(counter_box, DOWN)
        final_msg = Tex("TIMER\_PERIOD\_ELAPSED",color = RED_C).scale(0.5).next_to(counter_display, DOWN)
        timer_label = Text("TIME (ms)").scale(0.5).next_to(prescaler_box, UL)
        timer_display = DecimalNumber(0, num_decimal_places=4).scale(1).next_to(timer_label, RIGHT)

        # Add boxes and labels to scene
        self.play(Create(sysclk_box),Write(sysclk_label),Create(prescaler_box),Write(prescaler_label),Write(prescaler_display),Write(timer_label),Write(timer_display),Create(counter_box),Write(counter_label),Write(counter_display))

        # Add arrows
        arrow1 = Arrow(sysclk_box.get_right(), prescaler_box.get_left(), buff=0.1)
        arrow2 = Arrow(prescaler_box.get_right(), counter_box.get_left(), buff=0.1)
        self.play(Create(arrow1),Create(arrow2))

        # Add loop to update counter
        counter = ValueTracker(0)
        counter_value = ValueTracker(0)
        time = ValueTracker(0)
        sec = 0
        elap = 0
        
        while elap == 0:
            # Update counter value
            #counter_value.set_value(str(counter))
            curr = counter_value.get_value() 
            tim = time.get_value()
            counter_value.set_value(curr + 312)
            time.set_value(tim + 0.03900487)

            # Wrap around counter if it reaches 7999
            if counter_value.get_value() >= 7999:
                counter_value.set_value(0)
                time.set_value(sec+1)
                sec+=1
                count = counter.get_value()
                if count < 9:
                    counter.set_value(count + 1)
                else :
                    counter.set_value(0)
                    elap = 1
                    
            
            prescaler_display.set_value(int(counter_value.get_value()))
            timer_display.set_value((time.get_value()))
            if elap == 0:
                counter_display.set_value((counter.get_value()))
            else :
                counter_display.set_value(0)
            
            # Wait for a short time to simulate clock cycle
            self.wait(0.1)
        self.add(final_msg)
        self.wait()



