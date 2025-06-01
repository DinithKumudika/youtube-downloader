import customtkinter as ctk
from .base_component import BaseComponent

class InfoSection(BaseComponent):
     def create(self):
          self.frame = ctk.CTkFrame(
               self.parent,
               fg_color=self.colors.BACKGROUND,
               corner_radius=12,
               border_width=1,
               border_color=self.colors.BORDER,
               height=80
          )
          self.frame.pack(fill="x", padx=40, pady=(20, 0))
          self.frame.pack_propagate(False)

          self.status_label = ctk.CTkLabel(
               self.frame,
               text="Not started yet",
               font=("Segoe UI", 14),
               text_color=self.colors.TEXT_SECONDARY
          )
          self.status_label.pack(expand=True)
          
          return self.frame

     def update_status(self, message, color=None):
          if color is None:
               color = self.colors.TEXT_SECONDARY
          self.status_label.configure(text=message, text_color=color)