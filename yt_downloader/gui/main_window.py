import os
import tkinter as tk
import customtkinter as ctk
from yt_downloader.core.config import Config
from PIL import Image
from yt_downloader.core.YTDownloader import YTDownloader

from .styles.colors import Colors
from .components.hero_section import HeroSection
from .components.input_section import InputSection
from .components.info_section import InfoSection
from .components.features_section import FeaturesSection


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # Initialize
        self.colors = Colors()
        self._setup_window()
        self._create_components()
        
    def _setup_window(self):
        self.title("YouTube Downloader")
        self.geometry("800x600")
        self.resizable(False, False)
            
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
            
        self.configure(fg_color=self.colors.BACKGROUND)

        # Main container
        self.main_frame = ctk.CTkFrame(
            self,
            fg_color=self.colors.SURFACE,
            corner_radius=20,
            border_width=1,
            border_color=self.colors.BORDER
        )
        self.main_frame.pack(expand=True, fill="both", padx=30, pady=30)
            
    def _create_components(self):
    # Create all UI components
        self.hero_section = HeroSection(self.main_frame, self.colors)
        self.hero_section.create()

        self.input_section = InputSection(
            self.main_frame, 
            self.colors, 
            self.on_pressed_start
        )
        self.input_section.create()

        self.status_section = InfoSection(self.main_frame, self.colors)
        self.status_section.create()

        self.features_section = FeaturesSection(self.main_frame, self.colors)
        self.features_section.create()

    def on_pressed_start(self, url):
        
        if not url:
            self.status_section.update_status(
                "Please enter a YouTube URL", 
                self.colors.ACCENT
            )
            return

        link = self.link_input.get().strip()
        
        self.status_section.update_status(
            "Starting download...", 
            self.colors.PRIMARY
        )
        self.input_section.set_button_state("Downloading...", False)
        
        try:
            downloader = YTDownloader(url)
            downloader.get_info()
            self.status_section.update_status(
                "Download completed successfully!", 
                self.colors.SUCCESS
            )
        except Exception as e:
            self.status_section.update_status(
                f"Error: {str(e)}", 
                self.colors.ERROR
            )
        finally:
            self.input_section.set_button_state("Download", True)