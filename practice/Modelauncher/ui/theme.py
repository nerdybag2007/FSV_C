"""
Shared visual constants: spacing and fonts.

Keeping these in one place means every page stays visually consistent,
and Settings > Theme (future) has one file to change instead of many.
"""

import tkinter.font as tkfont
import customtkinter as ctk

# ---------------------------------------------------------------------------
# Spacing (padding/margins), in pixels. Use these instead of raw numbers.
# ---------------------------------------------------------------------------
SPACE_XS = 6
SPACE_SM = 10
SPACE_MD = 16
SPACE_LG = 24
SPACE_XL = 32

# ---------------------------------------------------------------------------
# Fonts
#
# CustomTkinter can't bundle a font file without extra platform-specific
# registration, so instead we pick the nicest-looking font that is actually
# installed, in order of preference, and fall back to a safe default.
# (To use a real custom .ttf later: drop it in assets/fonts and load it with
# customtkinter.FontManager.load_font() before calling font() below.)
# ---------------------------------------------------------------------------
_PREFERRED_FONT_FAMILIES = ["Segoe UI Variable", "Segoe UI", "Helvetica Neue", "Arial"]
_font_family_cache: str | None = None


def _resolve_font_family() -> str:
    global _font_family_cache
    if _font_family_cache is not None:
        return _font_family_cache

    try:
        available = set(tkfont.families())
    except Exception:
        available = set()

    for family in _PREFERRED_FONT_FAMILIES:
        if family in available:
            _font_family_cache = family
            return _font_family_cache

    _font_family_cache = "TkDefaultFont"
    return _font_family_cache


def font(size: int, weight: str = "normal") -> ctk.CTkFont:
    """Returns a CTkFont using the app's resolved font family."""
    return ctk.CTkFont(family=_resolve_font_family(), size=size, weight=weight)


TITLE_FONT_SIZE = 28
HEADER_FONT_SIZE = 22
BODY_FONT_SIZE = 14
BUTTON_FONT_SIZE = 16
