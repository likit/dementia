# -*- coding: utf-8 -*-
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.core.text import LabelBase
from kivy.utils import get_color_from_hex
from kivy.properties import StringProperty

LabelBase.register(name="THSarabunNew",
        fn_regular="THSarabunNew.ttf",
        fn_bold="THSarabunNew_Bold.ttf",
        fn_bolditalic="THSarabunNew_BoldItalic.ttf",
        fn_italic="THSarabunNew_Italic.ttf",
        )


class ScreenManagement(ScreenManager):
    pass

Builder.load_file('menu.kv')

class AgingApp(App):
    def build(self):
        return ScreenManagement()

    def login(self):
        self.pid = self.root.ids.pid.text
        self.root.ids.password.text = ''
        print('%s Just logged in...' % self.pid)
        self.root.ids._form1_greeting.text = 'Welcome %s' % self.pid
        self.root.current = 'form1'

    def logout(self):
        print('Just logged out...')
        self.root.current = 'login'



if __name__=='__main__':
    # Config.set("graphics", width=900)
    # Config.set("graphics", height=600)
    AgingApp().run()
