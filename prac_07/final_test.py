from kivy.app import App

from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.properties import ListProperty

Builder.load_string("""<Test>:
    Label:
        text:root.label_value[0]
    Label:
        text:root.label_value[1]""")


class Test(BoxLayout):
    label_value = ListProperty(["Im Nayeon", 'Yoo Jeongyeon'])

    def __init__(self, **kwargs):
        super(Test, self).__init__(**kwargs)
        self.label_value = ["Im Nayeon", 'Yoo Jeongyeon', 'Hirai Momo']


class TestApp(App):
    def build(self):
        self.root = Builder.load_file('final_test.kv')
        return Test()


TestApp().run()
