from typing import Optional

import customtkinter as ctk


class StatusBar(ctk.CTkFrame):
    """Thin bar showing the current status on a workspace page.

    Supports a simple animated "Launching..." state while background work
    is happening, and a final colored message once it's done.
    """

    SUCCESS_COLOR = "#98c379"
    ERROR_COLOR = "#e06c75"
    INFO_COLOR = "#61afef"
    _LOADING_FRAMES = ["", ".", "..", "..."]
    _ANIMATION_INTERVAL_MS = 400

    def __init__(self, master, **kwargs):
        super().__init__(master, corner_radius=12, **kwargs)
        self._label = ctk.CTkLabel(self, text="Ready", anchor="w")
        self._label.pack(fill="x", padx=12, pady=8)

        self._loading_job: Optional[str] = None
        self._loading_base_text = ""
        self._loading_frame_index = 0

    def set_message(self, message: str, is_error: bool = False) -> None:
        """Stops any loading animation and shows a final status message."""
        self._stop_loading_animation()
        color = self.ERROR_COLOR if is_error else self.SUCCESS_COLOR
        self._label.configure(text=message, text_color=color)

    def start_loading(self, base_text: str = "Launching") -> None:
        """Starts an animated '...' cycle to show background work is in progress."""
        self._stop_loading_animation()
        self._loading_base_text = base_text
        self._loading_frame_index = 0
        self._label.configure(text_color=self.INFO_COLOR)
        self._animate_loading()

    def _animate_loading(self) -> None:
        dots = self._LOADING_FRAMES[self._loading_frame_index % len(self._LOADING_FRAMES)]
        self._label.configure(text=f"{self._loading_base_text}{dots}")
        self._loading_frame_index += 1
        self._loading_job = self.after(self._ANIMATION_INTERVAL_MS, self._animate_loading)

    def _stop_loading_animation(self) -> None:
        if self._loading_job is not None:
            self.after_cancel(self._loading_job)
            self._loading_job = None
