from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivymd.uix.button import MDFlatButton

import socket
import threading
import pathlib
import plyer
from struct import unpack

Builder.load_string("""
<ReceiveScreen>:
    id: receive_screen
    name: 'receive_screen'
    MDRaisedButton:
        text: 'Waiting to Receive File'
        font_style: 'H3'
        elevation: 10
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        on_release: app.sm.current = 'main_screen'

""")

#Builder.load_file('receive.kv')

class ReceiveScreen(Screen):

    def __init__(self, *args, **kwargs):
        super(ReceiveScreen, self).__init__(*args, **kwargs)


