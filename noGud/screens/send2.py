from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.utils import platform

from kivymd.uix.button import MDFlatButton
from main import MainScreen

import socket
import pathlib
from struct import pack


class SendScreen(Screen):
    
    def __init__(self, *args, **kwargs):
        super(SendScreen, self).__init__(*args, **kwargs)

    
