"""Reusable widgets go here so pages don't redefine the same styled controls."""

import customtkinter as ctk
from typing import Callable

from ui import theme


class ModeButton(ctk.CTkButton):
    """Large rounded button used on the home page to enter a workspace."""

    def __init__(self, master, text: str, command: Callable[[], None], **kwargs):
        super().__init__(
            master,
            text=text,
            command=command,
            corner_radius=16,
            height=64,
            font=theme.font(18, "bold"),
            **kwargs,
        )
