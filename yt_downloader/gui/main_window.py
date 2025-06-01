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
        emoji_img = ctk.CTkImage(
            light_image=Image.open(
                os.path.join(Config.ASSETS_PATH, "images", "point_down.png")
            ),
            size=(20, 25),
        )
        
        # Create main container frame
        self.main_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.main_frame.pack(expand=True, fill="both", padx=20, pady=20)
        
        self.label_link = ctk.CTkLabel(
            self,
            image=emoji_img,
            text="Paste a Youtube Link here  ",
            compound="right",
            text_color="white",
            font=("Segoe UI", 18),
        )
        self.label_link.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.label_link.pack(padx=10, pady=10)

        # Link input
        self.link_input = ctk.CTkEntry(
            self,
            width=350,
            height=40,
            placeholder_text="Insert link here...",
            placeholder_text_color="gray",
            corner_radius=10,
            textvariable=url,
            font=("Segoe UI", 14)
        )
        self.link_input.pack(padx=10, pady=10)

        self.start_btn = ctk.CTkButton(
            self, 
            text="Start", 
            command= self.on_pressed_start,
            font=("Segoe UI", 16)
        )
        self.start_btn.pack(pady=10)

    def on_pressed_start(self):
        link = self.link_input.get()
        downloader = YTDownloader(link)
        downloader.get_info()