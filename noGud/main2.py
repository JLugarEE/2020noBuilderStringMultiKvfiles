from kivymd.app import MDApp

from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.utils import platform

if platform == 'android':
    from android.permissions import request_permissions, Permission

from screens.send2 import SendScreen
from screens.receive2 import ReceiveScreen

class SendScreen(Screen):
    pass


class ReceiveScreen(Screen):
    pass


class MainScreen(Screen):
    pass

Builder.load_file(os.path.join(path, 'screens\\send2.kv')
Builder.load_file(os.path.join(path, 'screens\\receive2.kv')

class Main2App(MDApp):
    def build(self):
        self.sm = ScreenManager()
        self.sm.add_widget(MainScreen(name='main_screen'))
        self.sm.add_widget(SendScreen(name='send_screen'))
        self.sm.add_widget(ReceiveScreen(name='receive_screen'))
        return self.sm

if __name__ == '__main__':
    Main2App().run()
