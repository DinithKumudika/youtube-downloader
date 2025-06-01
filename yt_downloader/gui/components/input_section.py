import customtkinter as ctk
from .base_component import BaseComponent

class InputSection(BaseComponent):
     def __init__(self, parent, colors=None, on_start_callback=None):
          super().__init__(parent, colors)
          self.on_start_callback = on_start_callback
          self.url_var = None
          self.link_input = None
          self.start_btn = None

     def create(self):
          self.frame = ctk.CTkFrame(
               self.parent,
               fg_color="transparent",
               height=100
          )
          self.frame.pack(fill="x", padx=40, pady=20)
          
          # Input label
          self.input_label = ctk.CTkLabel(
               self.frame,
               text="Paste YouTube URL",
               font=("Segoe UI", 14, "bold"),
               text_color=self.colors.TEXT_PRIMARY,
               anchor="w"
          )
          self.input_label.pack(fill="x", pady=(0, 8))

          # Input container
          self.input_container = ctk.CTkFrame(
               self.frame,
               height=55,
               corner_radius=12,
               fg_color=self.colors.BACKGROUND,
               border_width=2,
               border_color=self.colors.BORDER
          )
          self.input_container.pack(fill="x")
          self.input_container.pack_propagate(False)

          # Input field
          self.link_input = ctk.CTkEntry(
               self.input_container,
               placeholder_text="https://www.youtube.com/watch?v=...",
               height=51,
               font=("Segoe UI", 14),
               corner_radius=10,
               border_width=0,
               fg_color="transparent",
               placeholder_text_color=self.colors.TEXT_SECONDARY,
               text_color=self.colors.TEXT_PRIMARY
          )
          self.link_input.pack(side="left", fill="x", expand=True, padx=(15, 5), pady=2)

          # Download button
          self.start_btn = ctk.CTkButton(
               self.input_container,
               text="Start",
               width=120,
               height=47,
               command=self._on_start_clicked,
               font=("Segoe UI", 14, "bold"),
               corner_radius=10,
               fg_color=self.colors.PRIMARY,
               hover_color=self.colors.PRIMARY_HOVER,
               text_color=self.colors.SECONDARY,
               border_width=0
          )
          self.start_btn.pack(side="right", padx=(0, 4), pady=4)

          # Add hover effects
          self._add_hover_effects()
          
          return self.frame

     def _on_start_clicked(self):
          if self.on_start_callback:
               url = self.link_input.get().strip()
               self.on_start_callback(url)

     def _add_hover_effects(self):
          def on_enter_input(event):
               self.input_container.configure(border_color=self.colors.PRIMARY)
               
          def on_leave_input(event):
               self.input_container.configure(border_color=self.colors.BORDER)
               
          self.link_input.bind("<FocusIn>", on_enter_input)
          self.link_input.bind("<FocusOut>", on_leave_input)

     def set_button_state(self, text, enabled=True):
          self.start_btn.configure(text=text, state="normal" if enabled else "disabled")

     def get_url(self):
          return self.link_input.get().strip()

     def clear_input(self):
          self.link_input.delete(0, 'end')