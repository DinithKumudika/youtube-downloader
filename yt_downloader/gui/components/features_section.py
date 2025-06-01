import customtkinter as ctk
from .base_component import BaseComponent

class FeaturesSection(BaseComponent):
     def create(self):
          self.frame = ctk.CTkFrame(
               self.parent,
               fg_color="transparent",
               height=120
          )
          self.frame.pack(fill="x", padx=40, pady=(20, 40))

          features = [
               ("🎥", "High Quality", "Download videos in HD"),
               ("⚡", "Fast Speed", "Quick and efficient downloads"),
               ("🔒", "Safe & Secure", "No malware or ads")
          ]

          for i, (icon, title, desc) in enumerate(features):
               feature_frame = ctk.CTkFrame(
                    self.frame,
                    fg_color=self.colors.BACKGROUND,
                    corner_radius=8,
                    border_width=1,
                    border_color=self.colors.BORDER
               )
               feature_frame.pack(side="left", fill="both", expand=True, 
                              padx=(0 if i == 0 else 5, 0))
               
               icon_label = ctk.CTkLabel(
                    feature_frame,
                    text=icon,
                    font=("Segoe UI", 20)
               )
               icon_label.pack(pady=(15, 5))
               
               title_label = ctk.CTkLabel(
                    feature_frame,
                    text=title,
                    font=("Segoe UI", 12, "bold"),
                    text_color=self.colors.TEXT_PRIMARY
               )
               title_label.pack()
               
               desc_label = ctk.CTkLabel(
                    feature_frame,
                    text=desc,
                    font=("Segoe UI", 10),
                    text_color=self.colors.TEXT_SECONDARY
               )
               desc_label.pack(pady=(2, 15))
               
          return self.frame