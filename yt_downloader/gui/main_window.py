import os
import tkinter as tk
import customtkinter as ctk
from yt_downloader.core.config import Config
from PIL import Image
from yt_downloader.core.YTDownloader import YTDownloader


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
        ctk.set_default_color_theme(Config.THEMES_PATH)

        # Create main container frame
        self.main_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.main_frame.pack(expand=True, fill="both", padx=20, pady=20)

        # URL input container with white background and shadow
        self.input_container = ctk.CTkFrame(
            self.main_frame,
            fg_color="white",
            width=680,
            height=60,
            corner_radius=30,
            border_width=1,
            border_color="#E5E5E5"
        )
        self.input_container.pack(pady=20)
        self.input_container.pack_propagate(False)

        # Link input without border (since container has the border)
        self.link_input = ctk.CTkEntry(
            self.input_container,
            width=460,
            height=40,
            placeholder_text="Enter youtube url here...",
            font=("Segoe UI", 14),
            textvariable=url,
            border_width=0,
            fg_color="transparent"
        )
        self.link_input.pack(side="left", padx=(20, 0))

        # Download button
        self.start_btn = ctk.CTkButton(
            self.input_container,
            text="Download",
            width=160,
            height=40,
            command=self.on_pressed_start,
            font=("Segoe UI", 14, "bold"),
            corner_radius=25,
            fg_color="#7C63A6",
            hover_color="#6C5090"
        )
        self.start_btn.pack(side="right", padx=10)

    def on_pressed_start(self):
        link = self.link_input.get()
        downloader = YTDownloader(link)
        downloader.get_info()