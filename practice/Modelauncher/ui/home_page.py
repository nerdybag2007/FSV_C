"""Landing page: one button per workspace, defined entirely in config.HOME_MODES."""

import customtkinter as ctk
from typing import Callable

from config import HOME_MODES
from widgets.mode_button import ModeButton
from widgets.tooltip import ToolTip
from ui import theme


class HomePage(ctk.CTkFrame):
    def __init__(self, master, on_select_mode: Callable[[str], None], **kwargs):
        super().__init__(master, corner_radius=0, **kwargs)
        self._on_select_mode = on_select_mode
        self._build_ui()

    def _build_ui(self) -> None:
        ctk.CTkLabel(
            self, text="Mode Launcher", font=theme.font(theme.TITLE_FONT_SIZE, "bold")
        ).pack(pady=(theme.SPACE_XL + 10, theme.SPACE_LG))

        button_frame = ctk.CTkFrame(self, fg_color="transparent")
        button_frame.pack(expand=True)

        for mode in HOME_MODES:
            button = ModeButton(
                button_frame,
                text=f"{mode.label}   ({mode.shortcut})",
                command=lambda key=mode.key: self._on_select_mode(key),
                width=280,
            )
            button.pack(pady=theme.SPACE_MD)
            ToolTip(button, mode.description)

        ctk.CTkLabel(
            self,
            text="Tip: press 1, 2, or 3 to jump straight into a workspace",
            font=theme.font(theme.BODY_FONT_SIZE - 2),
            text_color="#7a7a8c",
        ).pack(pady=(0, theme.SPACE_LG))
