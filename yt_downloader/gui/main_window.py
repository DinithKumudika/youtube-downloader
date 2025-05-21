import os
import tkinter as tk
import customtkinter as ctk
from yt_downloader.core.config import Config


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Window configuration
        self.title("YouTube Downloader")
        self.geometry("720x480")
        self.resizable(False, False)

        # Set theme
        ctk.set_appearance_mode("System")
        print(Config.THEMES_PATH)
        ctk.set_default_color_theme(Config.THEMES_PATH)
