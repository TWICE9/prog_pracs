from kivy.app import App
from kivy.uix.label import Label
from kivy.lang import Builder


class TestApp(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ["Im Nayeon", 'Yoo Jeongyeon', 'Hirai Momo']

    def build(self):
        self.root = Builder.load_file('final_test.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        for name in self.names:
            temp_label = Label(text=name, id=name)
            self.root.ids.output_box.add_widget(temp_label)


TestApp().run()
