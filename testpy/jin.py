from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class CalculatorApp(App):
    def build(self):
        # Create the main layout
        main_layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        # Create the text input for display
        display = TextInput(font_size=32, readonly=True, halign='right', multiline=False)

        # Create the button grid
        button_grid = BoxLayout(orientation='vertical', spacing=5)

        # Define button rows
        rows = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', '=', '+']
        ]

        # Create buttons and add them to the grid
        for row in rows:
            h_layout = BoxLayout(spacing=5)
            for label in row:
                button = Button(text=label, on_press=self.on_button_press)
                h_layout.add_widget(button)
            button_grid.add_widget(h_layout)

        # Add widgets to the main layout
        main_layout.add_widget(display)
        main_layout.add_widget(button_grid)

        return main_layout
    def on_button_press(self, instance):
        # Find the TextInput widget for display
        display = None
        for widget in self.root.walk():
            if isinstance(widget, TextInput):
                display = widget
                break

        if display is None:
            print("Error: TextInput widget not found.")
            return

        current_text = display.text
        button_text = instance.text

        if button_text == '=':
            try:
                result = str(eval(current_text))
                display.text = result
            except Exception as e:
                display.text = 'Error'
        else:
            display.text += button_text


if __name__ == '__main__':
    CalculatorApp().run()
