import customtkinter as ctk
from ..styles.colors import Colors

class BaseComponent:
     def __init__(self, parent, colors=None):
          self.parent = parent
          self.colors = Colors()
          self.frame = None
          
     def create(self):
          """Override this method in child components"""
          raise NotImplementedError
          
     def get_frame(self):
          return self.frame