import os
from dotenv import load_dotenv

dirname = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path=os.path.join(dirname, "..", ".env"))
except FileNotFoundError:
    pass

DATABASE_FILENAME = os.getenv("DATABASE_FILENAME") or "database.sqlite"
DATABASE_FILE_PATH = os.path.join(dirname, "..", "data", DATABASE_FILENAME)

COLOR_SCHEME = os.getenv("COLOR_SCHEME") or "orange"
colors = {"bg":"", "text":"", "button":""}
match COLOR_SCHEME:
    case "orange":
        colors["bg"] = "#FAB12F"
        colors["text"] = "#FEF3E2"
        colors["button"] = "#FA4032"
    case "cherry":
        colors["bg"] = "#FFCCE1"
        colors["text"] = "#FFFFFF"
        colors["button"] = "#E195AB"
    case "green":
        colors["bg"] = "#5A6C57"
        colors["text"] = "#D3F1DF"
        colors["button"] = "#85A98F"
    case _:
        # Defaults to orange
        colors["bg"] = "#E5C3A7"
        colors["text"] = "#FFFFFF"
        colors["button"] = "#E5A970"
