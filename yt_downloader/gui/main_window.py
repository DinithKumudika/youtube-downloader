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
        self.geometry("800x600")
        self.resizable(False, False)

        # Set theme
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        
        self.colors = {
            'primary': '#6366f1',      # Modern indigo
            'primary_hover': '#4f46e5',
            'secondary': '#f8fafc',
            'background': '#0f172a',   # Dark slate
            'surface': '#1e293b',      # Lighter slate
            'text_primary': '#f1f5f9',
            'text_secondary': '#94a3b8',
            'accent': '#06b6d4',       # Cyan accent
            'success': '#10b981',
            'border': '#334155'
        }
        
        self.configure(fg_color=self.colors['background'])

        # Create main container frame
        self.main_frame = ctk.CTkFrame(
            self, 
            fg_color=self.colors['surface'],
            corner_radius=20,
            border_width=1,
            border_color=self.colors['border']
        )
        self.main_frame.pack(expand=True, fill="both", padx=30, pady=30)
        
        # Hero section
        self.hero_frame = ctk.CTkFrame(
            self.main_frame,
            fg_color="transparent",
            height=120
        )
        self.hero_frame.pack(fill="x", padx=40, pady=(40, 20))
        self.hero_frame.pack_propagate(False)
        
        # App icon/logo placeholder
        self.logo_frame = ctk.CTkFrame(
            self.hero_frame,
            width=60,
            height=60,
            corner_radius=30,
            fg_color=self.colors['primary']
        )
        self.logo_frame.pack(pady=(0, 15))
        self.logo_frame.pack_propagate(False)
        
        # Logo text
        self.logo_text = ctk.CTkLabel(
            self.logo_frame,
            text="YT",
            font=("Segoe UI", 24, "bold"),
            text_color=self.colors['secondary']
        )
        self.logo_text.place(relx=0.5, rely=0.5, anchor="center")
        
        # Main title
        self.title_label = ctk.CTkLabel(
            self.hero_frame,
            text="YouTube Downloader",
            font=("Segoe UI", 32, "bold"),
            text_color=self.colors['text_primary']
        )
        self.title_label.pack()
        
        # Subtitle
        self.subtitle_label = ctk.CTkLabel(
            self.hero_frame,
            text="Download your favorite videos in high quality",
            font=("Segoe UI", 16),
            text_color=self.colors['text_secondary']
        )
        self.subtitle_label.pack(pady=(5, 0))
        
        # Input Section
        self.input_section = ctk.CTkFrame(
            self.main_frame,
            fg_color="transparent",
            height=100
        )
        self.input_section.pack(fill="x", padx=40, pady=20)
        
        # Input label
        self.input_label = ctk.CTkLabel(
            self.input_section,
            text="Paste YouTube URL",
            font=("Segoe UI", 14, "bold"),
            text_color=self.colors['text_primary'],
            anchor="w"
        )
        self.input_label.pack(fill="x", pady=(0, 8))
        
        # Input container
        self.seamless_container = ctk.CTkFrame(
            self.input_section,
            height=55,
            corner_radius=12,
            fg_color=self.colors['background'],
            border_width=2,
            border_color=self.colors['border']
        )
        self.seamless_container.pack(fill="x")
        self.seamless_container.pack_propagate(False)
        
        # Input field
        self.link_input = ctk.CTkEntry(
            self.seamless_container,
            placeholder_text="https://www.youtube.com/watch?v=...",
            height=51,
            font=("Segoe UI", 14),
            textvariable=url,
            corner_radius=10,
            border_width=0,
            fg_color="transparent",
            placeholder_text_color=self.colors['text_secondary'],
            text_color=self.colors['text_primary']
        )
        self.link_input.pack(side="left", fill="x", expand=True, padx=(15, 5), pady=2)
        
        
        # Download button
        self.start_btn = ctk.CTkButton(
            self.seamless_container,
            text="Download",
            width=120,
            height=47,
            command=self.on_pressed_start,
            font=("Segoe UI", 14, "bold"),
            corner_radius=10,
            fg_color=self.colors['primary'],
            hover_color=self.colors['primary_hover'],
            text_color=self.colors['secondary'],
            border_width=0
        )
        self.start_btn.pack(side="right", padx=(0, 4), pady=4)
        
        # Status/Info section
        self.status_frame = ctk.CTkFrame(
            self.main_frame,
            fg_color=self.colors['background'],
            corner_radius=12,
            border_width=1,
            border_color=self.colors['border'],
            height=80
        )
        self.status_frame.pack(fill="x", padx=40, pady=(20, 0))
        self.status_frame.pack_propagate(False)

        self.status_label = ctk.CTkLabel(
            self.status_frame,
            text="Ready to download",
            font=("Segoe UI", 14),
            text_color=self.colors['text_secondary']
        )
        self.status_label.pack(expand=True)
        
        # Features section
        self.features_frame = ctk.CTkFrame(
            self.main_frame,
            fg_color="transparent",
            height=120
        )
        self.features_frame.pack(fill="x", padx=40, pady=(20, 40))

        # Feature items
        features = [
            ("🎥", "High Quality", "Download videos in HD"),
            ("⚡", "Fast Speed", "Quick and efficient downloads"),  
            ("🔒", "Safe & Secure", "No malware or ads")
        ]
        
        self.feature_items = []
        for i, (icon, title, desc) in enumerate(features):
            feature_frame = ctk.CTkFrame(
                self.features_frame,
                fg_color=self.colors['background'],
                corner_radius=8,
                border_width=1,
                border_color=self.colors['border']
            )
            feature_frame.pack(side="left", fill="both", expand=True, padx=(0 if i == 0 else 5, 0))
            
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
                text_color=self.colors['text_primary']
            )
            title_label.pack()
            
            desc_label = ctk.CTkLabel(
                feature_frame,
                text=desc,
                font=("Segoe UI", 10),
                text_color=self.colors['text_secondary']
            )
            desc_label.pack(pady=(2, 15))

        # Add hover effects
        self.add_hover_effects()
        

    def add_hover_effects(self):
        """Add modern hover effects"""
        def on_enter_input(event):
            self.seamless_container.configure(border_color=self.colors['primary'])
            
        def on_leave_input(event):
            self.seamless_container.configure(border_color=self.colors['border'])
            
        self.link_input.bind("<FocusIn>", on_enter_input)
        self.link_input.bind("<FocusOut>", on_leave_input)

    def update_status(self, message, color=None):
        """Update status message"""
        if color is None:
            color = self.colors['text_secondary']
        self.status_label.configure(text=message, text_color=color)

    def on_pressed_start(self):
        link = self.link_input.get().strip()
        
        if not link:
            self.update_status("Please enter a YouTube URL", self.colors['accent'])
            return
        
        self.update_status("Starting download...", self.colors['primary'])
        self.start_btn.configure(text="Downloading...", state="disabled")
        
        try:
            downloader = YTDownloader(link)
            downloader.get_info()
            self.update_status("Download completed successfully!", self.colors['success'])
        except Exception as e:
            self.update_status(f"Error: {str(e)}", "#ef4444")
        finally:
            self.start_btn.configure(text="Download", state="normal")