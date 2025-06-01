import customtkinter as ctk
from .base_component import BaseComponent

class HeroSection(BaseComponent):
     def create(self):
          self.frame = ctk.CTkFrame(
               self.parent,
               fg_color="transparent",
               height=120
          )
          self.frame.pack(fill="x", padx=40, pady=(40, 20))
          self.frame.pack_propagate(False)

          # Logo
          self.logo_frame = ctk.CTkFrame(
               self.frame,
               width=60,
               height=60,
               corner_radius=30,
               fg_color=self.colors.PRIMARY
          )
          self.logo_frame.pack(pady=(0, 15))
          self.logo_frame.pack_propagate(False)

          self.logo_text = ctk.CTkLabel(
               self.logo_frame,
               text="YT",
               font=("Segoe UI", 24, "bold"),
               text_color=self.colors.SECONDARY
          )
          self.logo_text.place(relx=0.5, rely=0.5, anchor="center")

          # Title
          self.title_label = ctk.CTkLabel(
               self.frame,
               text="YouTube Downloader",
               font=("Segoe UI", 32, "bold"),
               text_color=self.colors.TEXT_PRIMARY
          )
          self.title_label.pack()

          # Subtitle
          self.subtitle_label = ctk.CTkLabel(
               self.frame,
               text="Download your favorite videos in high quality",
               font=("Segoe UI", 16),
               text_color=self.colors.TEXT_SECONDARY
          )
          self.subtitle_label.pack(pady=(5, 0))
          
          return self.frame