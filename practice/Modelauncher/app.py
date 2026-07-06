"""Main application window: page navigation, theming, icon, centering, and shortcuts."""

import os
import tkinter as tk
from typing import Optional

import customtkinter as ctk

from config import HOME_MODES
from ui.home_page import HomePage
from ui.coding_page import CodingPage
from ui.gaming_page import GamingPage
from ui.freedom_page import FreedomPage

ASSETS_DIR = os.path.join(os.path.dirname(__file__), "assets")
ICON_ICO_PATH = os.path.join(ASSETS_DIR, "icon.ico")
ICON_PNG_PATH = os.path.join(ASSETS_DIR, "icon.png")

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 520


class ModeLauncherApp(ctk.CTk):
    """Switches between the home page and whichever workspace page is active."""

    PAGE_CLASSES = {
        "coding": CodingPage,
        "gaming": GamingPage,
        "freedom": FreedomPage,
    }

    def __init__(self):
        super().__init__()

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        self.title("Mode Launcher")
        self.minsize(520, 440)
        self._center_window(WINDOW_WIDTH, WINDOW_HEIGHT)
        self._set_app_icon()

        self._current_page: Optional[ctk.CTkFrame] = None
        self._home_shortcuts_bound = False
        self._show_home()

    # -- Window setup ---------------------------------------------------

    def _center_window(self, width: int, height: int) -> None:
        self.update_idletasks()
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        self.geometry(f"{width}x{height}+{x}+{y}")

    def _set_app_icon(self) -> None:
        # Icon loading must never crash the app if the file is missing
        # or the platform doesn't support the format.
        try:
            if os.name == "nt" and os.path.isfile(ICON_ICO_PATH):
                self.iconbitmap(ICON_ICO_PATH)
            elif os.path.isfile(ICON_PNG_PATH):
                self._icon_image = tk.PhotoImage(file=ICON_PNG_PATH)
                self.iconphoto(True, self._icon_image)
        except Exception:
            pass

    # -- Page navigation ---------------------------------------------------

    def _show_home(self) -> None:
        self._switch_page(HomePage(self, on_select_mode=self._show_workspace))
        self._bind_home_shortcuts()

    def _show_workspace(self, mode_key: str) -> None:
        page_class = self.PAGE_CLASSES.get(mode_key)
        if page_class is None:
            return
        self._unbind_home_shortcuts()
        self._switch_page(page_class(self, on_back=self._show_home))

    def _switch_page(self, page: ctk.CTkFrame) -> None:
        if self._current_page is not None:
            self._current_page.destroy()
        self._current_page = page
        self._current_page.pack(fill="both", expand=True)

    # -- Keyboard shortcuts (1/2/3 -> workspaces, only active on home page) --

    def _bind_home_shortcuts(self) -> None:
        if self._home_shortcuts_bound:
            return
        for mode in HOME_MODES:
            self.bind(f"<Key-{mode.shortcut}>", self._make_shortcut_handler(mode.key))
        self._home_shortcuts_bound = True

    def _unbind_home_shortcuts(self) -> None:
        if not self._home_shortcuts_bound:
            return
        for mode in HOME_MODES:
            self.unbind(f"<Key-{mode.shortcut}>")
        self._home_shortcuts_bound = False

    def _make_shortcut_handler(self, mode_key: str):
        return lambda _event: self._show_workspace(mode_key)
