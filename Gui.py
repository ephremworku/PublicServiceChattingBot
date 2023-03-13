from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import Gui_Bot

gui = Gui_Bot


class SayHello(App):
    def build(self):
        # returns a window object with all it's widgets
        self.window = GridLayout()
        self.window.cols = 0.8

        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}

        # image widget
        self.window.add_widget(Image(source="welcom.png"))

        # label widget
        self.greeting = Label(
            text="What Can I Help",
            font_size=18,
            color='#00FFCE'
        )
        self.window.add_widget(self.greeting)
        # label widget
        self.greeting2 = Label(
            text="-----------",
            font_size=18,
            color='#00FFCE'
        )
        self.window.add_widget(self.greeting2)

        # text input widget
        self.user = TextInput(
            multiline=False,
            padding_y=(10, 10),
            size_hint=(1, 0.5)
        )

        self.window.add_widget(self.user)

        # button widget
        self.button = Button(
            text="Ask",
            size_hint=(1, 0.5),
            bold=True,
            background_color='#c8c2c0',
            # remove darker overlay of background colour
            # background_normal = ""
        )
        self.button.bind(on_press=self.callback)
        self.window.add_widget(self.button)

        return self.window

    def callback(self, instance):
        # change label text to "Hello + user name!"
        response = gui.send(self.user.text)
        self.greeting.text = "Bot: " + response + "!"
        self.greeting2.text = "You:  " + self.user.text + "!"


# run Say Hello App Calss
if __name__ == "__main__":
    SayHello().run()
