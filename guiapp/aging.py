# -*- coding: utf-8 -*-
from datetime import datetime
from kivy.app import App
from kivy.config import Config
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.modalview import ModalView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.core.text import LabelBase
from kivy.utils import get_color_from_hex
from kivy.properties import StringProperty, ObjectProperty
from kivy.app import App

Window.clearcolor = (0.2, 0.2, 0.2, 1)

LabelBase.register(name="THSarabunNew",
        fn_regular="THSarabunNew.ttf",
        fn_bold="THSarabunNew_Bold.ttf",
        fn_bolditalic="THSarabunNew_BoldItalic.ttf",
        fn_italic="THSarabunNew_Italic.ttf",
        )


class ScreenManagement(ScreenManager):
    pass

Builder.load_file('menu.kv')
Builder.load_file('statusbar.kv')

class LoginForm(BoxLayout):
    pass

Builder.load_file('login.kv')


class GeneralInfoForm(Popup):
    pass

Builder.load_file('generalinfo.kv')

class DateForm(Popup):
    date = ObjectProperty()
    month = ObjectProperty()
    year = ObjectProperty()
    status = ObjectProperty()

    def save_date(self):
        print('date', self.date.infield.text)
        print('month', self.month.infield.text)
        print('year', self.year.infield.text)

    def clear(self):
        self.date.infield.text = ''
        self.month.infield.text = ''
        self.year.infield.text = ''

    def validate_date(self):
        if not self.date.infield.text or int(self.date.infield.text) > 5:
            print('DateError')
            self.clear()
            self.status.text = '[b]Status[/b] วันที่ไม่ถูกต้อง'
        else:
            self.dismiss()


Builder.load_file('dateform.kv')


class AgingApp(App):
    def build(self):
        return ScreenManagement()

    def login(self):
        self.loginform = LoginForm()
        self.pid = self.loginform.pid.text
        self.loginform.password.text = ''
        print('%s Just logged in...' % self.pid)
        # self.root.ids._dateform_title.text = 'Welcome %s' % self.pid
        self.root.current = 'all_form'

    def logout(self):
        print('Just logged out...')
        self.root.current = 'login'

    def show_dateform(self):
        self.dateform = DateForm()
        today = datetime.today().date()
        self.dateform.date.infield.text = str(today.day)
        self.dateform.month.infield.text = str(today.month)
        self.dateform.year.infield.text = str(today.year)

        self.dateform.open()

    def show_general_info_form(self):
        self.general_info_form = GeneralInfoForm()
        self.general_info_form.open()

    def to_main(self):
        self.root.current = 'all_form'

    def exit_app(self):
        self.get_running_app().stop()

if __name__=='__main__':
    # Config.set("graphics", width=900)
    # Config.set("graphics", height=600)
    AgingApp().run()
