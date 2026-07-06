"""Lightweight hover tooltip that can be attached to any CTk widget."""

import customtkinter as ctk


class ToolTip:
    """Shows a small popup with `text` after hovering over `widget` for a moment."""

    def __init__(self, widget, text: str, delay_ms: int = 500):
        self._widget = widget
        self._text = text
        self._delay_ms = delay_ms
        self._after_id: str | None = None
        self._tooltip_window: ctk.CTkToplevel | None = None

        widget.bind("<Enter>", self._schedule_show, add="+")
        widget.bind("<Leave>", self._hide, add="+")

    def _schedule_show(self, _event=None) -> None:
        self._after_id = self._widget.after(self._delay_ms, self._show)

    def _show(self) -> None:
        if self._tooltip_window is not None:
            return

        x = self._widget.winfo_rootx() + 12
        y = self._widget.winfo_rooty() + self._widget.winfo_height() + 8

        self._tooltip_window = ctk.CTkToplevel(self._widget)
        self._tooltip_window.overrideredirect(True)
        self._tooltip_window.geometry(f"+{x}+{y}")
        self._tooltip_window.attributes("-topmost", True)

        ctk.CTkLabel(
            self._tooltip_window,
            text=self._text,
            corner_radius=8,
            fg_color="#2b2b3a",
            text_color="#dddddd",
            padx=10,
            pady=4,
        ).pack()

    def _hide(self, _event=None) -> None:
        if self._after_id is not None:
            self._widget.after_cancel(self._after_id)
            self._after_id = None
        if self._tooltip_window is not None:
            self._tooltip_window.destroy()
            self._tooltip_window = None
