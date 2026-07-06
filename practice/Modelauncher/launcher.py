"""
Launching logic, kept fully separate from any UI code.

Resolves configured apps to real executable paths and opens them,
or opens URLs in the default browser. Never raises — every failure
is reported back as a LaunchResult instead.
"""

import os
import shutil
import subprocess
import webbrowser
from dataclasses import dataclass
from typing import Callable, List, Optional

from config import LaunchItem, APP_PATHS


@dataclass
class LaunchResult:
    name: str
    success: bool
    message: str


class Launcher:
    """Resolves and launches configured items (apps or URLs)."""

    def launch_items(
        self, items: List[LaunchItem], on_result: Callable[[LaunchResult], None]
    ) -> None:
        """Launches each item in order, reporting one result at a time."""
        for item in items:
            result = self._launch_single(item)
            on_result(result)

    def _launch_single(self, item: LaunchItem) -> LaunchResult:
        try:
            if item.kind == "url":
                webbrowser.open(item.target)
                return LaunchResult(item.name, True, f"Opened {item.name}")

            if item.kind == "app":
                path = self._resolve_app_path(item.target)
                if path is None:
                    return LaunchResult(
                        item.name, False, f"{item.name} not found on this system"
                    )
                subprocess.Popen([path])
                return LaunchResult(item.name, True, f"Launched {item.name}")

            return LaunchResult(item.name, False, f"Unknown launch type for {item.name}")

        except Exception as exc:
            return LaunchResult(item.name, False, f"Could not launch {item.name}: {exc}")

    def _resolve_app_path(self, app_key: str) -> Optional[str]:
        """Tries each configured candidate path, then falls back to PATH lookup."""
        for candidate in APP_PATHS.get(app_key, []):
            if candidate and os.path.isfile(candidate):
                return candidate

        return shutil.which(app_key)
