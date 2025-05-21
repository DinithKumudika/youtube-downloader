import os
import tkinter as tk
import customtkinter as ctk
from yt_downloader.core.config import Config


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        url = tk.StringVar()

        # Window configuration
        self.title("YouTube Downloader")
        self.geometry("720x480")
        self.resizable(False, False)

        # Set theme
        ctk.set_appearance_mode("System")
        print(Config.THEMES_PATH)
        ctk.set_default_color_theme(Config.THEMES_PATH)

        self.label_link = ctk.CTkLabel(
            self, text="Paste a Youtube Link here 👇", text_color="white"
        )
        self.label_link.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.label_link.pack(padx=10)

        # Link input
        self.link_input = ctk.CTkEntry(
            self,
            width=350,
            height=40,
            placeholder_text="Insert link here...",
            corner_radius=10,
            textvariable=url,
        )
        self.link_input.pack(padx=10, pady=10)
