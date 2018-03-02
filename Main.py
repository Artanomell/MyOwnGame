from kivy.app import App
from kivy.config import Config
Config.set("graphics", "resizable", 1)
Config.set("graphics", "width", 1000)
Config.set("graphics", "height", 600)
'''from kivy.core.window import Window
Window.fullscreen = True'''
from kivy.graphics import Color, Rectangle
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
import openpyxl


class ThemeLabel(Label):
    def __init__(self, **kwargs):
        super(ThemeLabel, self).__init__(**kwargs)
        self.color = [1, 1, 1, 1]
        self.font_size = 20

    def on_size(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(.09, .09, .35, 1)
            Rectangle(pos=self.pos, size=self.size)


class Main(BoxLayout):
    def __init__(self, **kwargs):
        super(Main, self).__init__(**kwargs)
        self.add_widget(Button(text="START", on_press=self.main_window))


    def main_window(self, instance):
        self.clear_widgets()
        self.orientation = "horizontal"

        ThemesLayout = BoxLayout(orientation="vertical",
                                 padding=[5, 5, 2.5, 5],
                                 spacing=5,
                                 size_hint=[.45, 1])
        for i in range(6):
            ThemesLayout.add_widget(ThemeLabel(text=question_table[i][0]))

        PriceLayout = GridLayout(rows=6, cols=5,
                                 padding=[2.5, 5, 5, 5],
                                 spacing=5,
                                 size_hint=[.55, 1])
        for self.i in range(PriceLayout.rows):
            for self.j in range(PriceLayout.cols):
                PriceLayout.add_widget(Button(background_color=[.25, .25, 1, 1],
                                              font_size=20,
                                              id=str(self.i)+str(self.j),
                                              on_press=self.question_window,
                                              text=price_table[self.i][self.j]))

        self.add_widget(ThemesLayout)
        self.add_widget(PriceLayout)

    def question_window(self, instance):
        self.i = int(instance.id[0])
        self.j = int(instance.id[1])
        price_table[self.i][self.j] = ""
        self.clear_widgets()
        self.orientation = "vertical"
        self.add_widget(ThemeLabel(size_hint=[1, .6], text=question_table[self.i][self.j + 1]))
        self.add_widget(Button(background_color=[.25, .25, 1, 1],
                               on_press=self.main_window,
                               size_hint=[1, .4],
                               text="Back"))

    def on_size(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(1, 1, 1, 1)
            Rectangle(pos=self.pos, size=self.size)


class MyOwnGame(App):
    def build(self):
        return Main()


book = openpyxl.load_workbook('Questions.xlsx')
sheet = book.active
question_table = []
price_table = []
letters = ["A", "B", "C", "D", "E", "F"]
for i in range(6):
    question_table.append([])
    for j in range(6):
        question_table[i].append(str(sheet[letters[j] + str(i + 1)].value))
for i in range(6):
    price_table.append([])
    for j in range(5):
        price_table[i].append(str((j + 1) * 100))
MyOwnGame().run()