"""
Central configuration for Mode Launcher.

Every URL, executable path, and workspace item lives here.
UI and launcher code should never hardcode this information —
they only read it from this file.
"""

import os
from dataclasses import dataclass, field
from typing import List


@dataclass
class LaunchItem:
    """A single thing a workspace can open: either an app or a website."""

    name: str
    kind: str  # "app" or "url"
    target: str  # for "app": key into APP_PATHS. for "url": the actual URL.
    checked_by_default: bool = True


@dataclass
class WorkspaceConfig:
    """A workspace shown as its own page (Coding, Gaming, Freedom, ...)."""

    key: str
    title: str
    items: List[LaunchItem] = field(default_factory=list)


# ---------------------------------------------------------------------------
# Application executable candidates.
# The launcher tries each path in order, then falls back to searching PATH.
# Adjust these if your install locations differ.
# ---------------------------------------------------------------------------
APP_PATHS = {
    "brave": [
        os.path.expandvars(r"%PROGRAMFILES%\BraveSoftware\Brave-Browser\Application\brave.exe"),
        os.path.expandvars(r"%PROGRAMFILES(X86)%\BraveSoftware\Brave-Browser\Application\brave.exe"),
        os.path.expandvars(r"%LOCALAPPDATA%\BraveSoftware\Brave-Browser\Application\brave.exe"),
    ],
    "vscode": [
        os.path.expandvars(r"%LOCALAPPDATA%\Programs\Microsoft VS Code\Code.exe"),
        os.path.expandvars(r"%PROGRAMFILES%\Microsoft VS Code\Code.exe"),
    ],
}


# ---------------------------------------------------------------------------
# Workspace definitions.
# Gaming and Freedom are intentionally empty placeholders for now —
# add LaunchItem entries here later, no UI code changes required.
# ---------------------------------------------------------------------------
WORKSPACES = {
    "coding": WorkspaceConfig(
        key="coding",
        title="Coding Workspace",
        items=[
            LaunchItem("VS Code", "app", "vscode"),
            LaunchItem("Brave Browser", "app", "brave"),
            LaunchItem("ChatGPT", "url", "https://chat.openai.com"),
            LaunchItem("Claude", "url", "https://claude.ai"),
            LaunchItem("GitHub", "url", "https://github.com"),
            LaunchItem("LeetCode", "url", "https://leetcode.com"),
            LaunchItem("HackerRank", "url", "https://www.hackerrank.com"),
        ],
    ),
    "gaming": WorkspaceConfig(
        key="gaming",
        title="Gaming Workspace",
        items=[],  # placeholder — add items when ready
    ),
    "freedom": WorkspaceConfig(
        key="freedom",
        title="Freedom Workspace",
        items=[],  # placeholder — add items when ready
    ),
}

@dataclass
class HomeModeEntry:
    """One button on the home page: which workspace it opens, and its shortcut."""

    key: str
    label: str
    shortcut: str  # keyboard digit that opens this workspace, e.g. "1"
    description: str  # shown in a tooltip on hover


HOME_MODES = [
    HomeModeEntry("coding", "💻 Coding", "1", "VS Code, Brave, and your coding sites"),
    HomeModeEntry("gaming", "🎮 Gaming", "2", "Game launchers and chat, ready to play"),
    HomeModeEntry("freedom", "🌴 Freedom", "3", "YouTube, Spotify, and downtime apps"),
]
