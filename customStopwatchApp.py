from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock

import time

class customStopwatchApp(App):
    def __init__(self):
        super().__init__()
        self.current_counter = time.perf_counter_ns()

    def update_clock(self, instance):
        elapsed_time_ms = (time.perf_counter_ns() - self.current_counter) // 1_000_000
        ms = (elapsed_time_ms % 1000) // 100
        seconds = (elapsed_time_ms // 1000) % 60
        minutes = (elapsed_time_ms // (60 * 1000)) % 60
        hours =  elapsed_time_ms // (3600 * 1000)
        self.stopwatch.text = self.format(hours) + ":" + self.format(minutes) + ":" + self.format(seconds) + "." + str(ms)

    def format(self, number):
        if number < 10:
            return "0" + str(number)
        return str(number)
    def build(self):
        # Main layout
        main_layout = BoxLayout(orientation="vertical")

        # Horizontal layout contains stopwatch and sw control buttons
        h_layout = BoxLayout(orientation="horizontal")

        # Vertical layout contains sw control buttons
        v_layout = BoxLayout(orientation="vertical")
        
        # Stopwatch, which is going to be placed at the left of h_layout
        self.stopwatch = Label(
            text="0",font_size=64
            )
        
        Clock.schedule_interval(self.update_clock, 0.001)

        # Place stopwatch in h_layout
        h_layout.add_widget(self.stopwatch)
        
        # Create button names to be used in double for
        buttons = [
            ["Start/Lap Trabajo", "Start/Lap Pausa"],
            ["Ver Laps"],
            ["Stop"]
        ]

        # Double for to assign names and positions to sw control
        for row in buttons:
            
            # Second horizontal layout contains sw buttons horizontally (it will be placed on v_layout). Respawns again after each row of buttons loop
            h2_layout = BoxLayout()

            for label in row:
                # Button assignment using buttons array of arrays
                button = Button(
                    text=label                    
                )
                # button.bind(on_press=self.increment_clock) 
                #button.bind(on_press=self.on_button_press)
                # Paste sw button to h2_layout
                h2_layout.add_widget(button)
            # Paste h2_layout containing row of sw buttons to v_layout
            v_layout.add_widget(h2_layout)

        # Paste v_layout to h_layout at the right of stopwatch
        h_layout.add_widget(v_layout)

        # Paste h_layout (containing stopwatch and buttons) to main layout
        main_layout.add_widget(h_layout)

        addStopwatch_button = Button(
            text="+", size_hint=(0.1, 0.1)
        )
        #equals_button.bind(on_press=self.on_solution)
        main_layout.add_widget(addStopwatch_button)

        return main_layout


if __name__ == "__main__":
    customStopwatchApp().run()