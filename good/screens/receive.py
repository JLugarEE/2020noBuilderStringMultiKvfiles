from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.utils import platform

from kivymd.uix.button import MDFlatButton

import socket
import pathlib
from struct import pack

Builder.load_string("""

<SendScreen>:
    id: send_screen
    name: 'send_screen'
    MDRaisedButton:
        text: "Select File to Send"
        elevation: 10
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        on_release: app.sm.current = 'main_screen'
""")

#Builder.load_file('send.kv')


class SendScreen(Screen):

    def __init__(self, *args, **kwargs):
        super(SendScreen, self).__init__(*args, **kwargs)

