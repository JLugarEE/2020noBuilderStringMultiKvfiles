from kivymd.app import MDApp

from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.utils import platform

if platform == 'android':
    from android.permissions import request_permissions, Permission

from screens.send import SendScreen
from screens.receive import ReceiveScreen

class MainScreen(Screen):
    pass


class MainApp(MDApp):
    def build(self):
        self.sm = ScreenManager()
        self.sm.add_widget(MainScreen(name='main_screen'))
        self.sm.add_widget(SendScreen(name='send_screen'))
        self.sm.add_widget(ReceiveScreen(name='receive_screen'))
        return self.sm

if __name__ == '__main__':
    MainApp().run()
