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

Builder.load_file(os.path.join(path, 'screens\receive2.kv')
#os.path.join(path, nameFile+".mat")
class ReceiveScreen(Screen):

    def __init__(self, *args, **kwargs):
        super(ReceiveScreen, self).__init__(*args, **kwargs)


