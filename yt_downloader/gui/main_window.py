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

        # URL input container
        self.input_container = ctk.CTkFrame(
            self.main_frame,
            fg_color="transparent",
            width=680,
            height=100
        )
        self.input_container.pack(pady=20)
        self.input_container.pack_propagate(False)

        # Link input
        self.link_input = ctk.CTkEntry(
            self.input_container,
            width=480,
            height=45,
            placeholder_text="Enter youtube url here...",
            font=("Segoe UI", 14),
            textvariable=url,
            border_width=1,
            corner_radius=25
        )
        self.link_input.pack(side="left", padx=(0, 10))

        # Download button with icon
        self.start_btn = ctk.CTkButton(
            self.input_container,
            text="Download",
            width=180,
            height=45,
            command=lambda: self.start(self.link_input.get()),
            font=("Segoe UI", 14, "bold"),
            corner_radius=25,
            compound="right",
            hover=True,
            fg_color="#7C63A6",
            hover_color="#6C5090"
        )
        self.start_btn.pack(side="left")

    def on_pressed_start(self):
        link = self.link_input.get()
        downloader = YTDownloader(link)
        downloader.get_info()