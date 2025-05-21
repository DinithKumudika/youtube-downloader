import os
from dotenv import dotenv_values


class Config:
    __config = dotenv_values(".env")
    THEMES_PATH = os.path.join(
        os.getcwd(), "yt_downloader", "gui", __config.get("THEMES_DIR"), "lavender.json"
    )
