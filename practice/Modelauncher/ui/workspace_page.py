"""
Generic workspace page.

Every workspace (Coding, Gaming, Freedom, and future ones) shares this exact
UI and behavior. What differs is only the WorkspaceConfig passed in — so
adding a new workspace never requires touching this file.
"""

import threading
from typing import Callable, Dict, List, Tuple

import customtkinter as ctk

from config import WorkspaceConfig, LaunchItem
from launcher import Launcher, LaunchResult
from widgets.status_bar import StatusBar
from widgets.tooltip import ToolTip
from ui import theme


class WorkspacePage(ctk.CTkFrame):
    """Shows a checklist of items for one workspace plus a Launch button."""

    def __init__(
        self,
        master,
        workspace: WorkspaceConfig,
        on_back: Callable[[], None],
        **kwargs,
    ):
        super().__init__(master, corner_radius=0, **kwargs)
        self._workspace = workspace
        self._on_back = on_back
        self._launcher = Launcher()
        self._checkbox_vars: Dict[str, ctk.BooleanVar] = {}

        self._build_ui()
        self._bind_escape_to_back()

    # -- UI construction ---------------------------------------------------

    def _build_ui(self) -> None:
        self._build_header()
        self._build_item_list()
        self._build_launch_button()

        self._status_bar = StatusBar(self)
        self._status_bar.pack(fill="x", padx=theme.SPACE_LG, pady=(theme.SPACE_XS, theme.SPACE_LG))

    def _build_header(self) -> None:
        header = ctk.CTkFrame(self, fg_color="transparent")
        header.pack(fill="x", padx=theme.SPACE_LG, pady=(theme.SPACE_LG, theme.SPACE_SM))

        back_button = ctk.CTkButton(
            header,
            text="← Back",
            width=80,
            corner_radius=10,
            font=theme.font(theme.BODY_FONT_SIZE),
            command=self._on_back,
        )
        back_button.pack(side="left")
        ToolTip(back_button, "Return to home (Esc)")

        ctk.CTkLabel(
            header, text=self._workspace.title, font=theme.font(theme.HEADER_FONT_SIZE, "bold")
        ).pack(side="left", padx=theme.SPACE_MD)

    def _build_item_list(self) -> None:
        items_frame = ctk.CTkFrame(self, corner_radius=16)
        items_frame.pack(fill="both", expand=True, padx=theme.SPACE_LG, pady=theme.SPACE_SM)

        if not self._workspace.items:
            ctk.CTkLabel(
                items_frame,
                text="No items configured yet for this workspace.",
                font=theme.font(theme.BODY_FONT_SIZE),
            ).pack(pady=theme.SPACE_LG)
            return

        for item in self._workspace.items:
            var = ctk.BooleanVar(value=item.checked_by_default)
            self._checkbox_vars[item.name] = var
            checkbox = ctk.CTkCheckBox(
                items_frame,
                text=item.name,
                variable=var,
                corner_radius=8,
                font=theme.font(theme.BODY_FONT_SIZE),
            )
            checkbox.pack(anchor="w", padx=theme.SPACE_LG, pady=theme.SPACE_SM)
            ToolTip(checkbox, self._describe_item(item))

    @staticmethod
    def _describe_item(item: LaunchItem) -> str:
        if item.kind == "url":
            return item.target
        return f"Application: {item.target}"

    def _build_launch_button(self) -> None:
        self._launch_button = ctk.CTkButton(
            self,
            text="Launch Workspace",
            corner_radius=14,
            height=48,
            font=theme.font(theme.BUTTON_FONT_SIZE, "bold"),
            command=self._launch_selected,
            state="normal" if self._workspace.items else "disabled",
        )
        self._launch_button.pack(pady=(theme.SPACE_XS, theme.SPACE_XS))

    def _bind_escape_to_back(self) -> None:
        self.master.bind("<Escape>", lambda _event: self._on_back())

    # -- Launch behavior -----------------------------------------------------

    def _launch_selected(self) -> None:
        selected_items = [
            item for item in self._workspace.items if self._checkbox_vars[item.name].get()
        ]
        if not selected_items:
            self._status_bar.set_message("Select at least one item to launch.", is_error=True)
            return

        self._launch_button.configure(state="disabled", text="Launching...")
        self._status_bar.start_loading("Launching workspace")

        thread = threading.Thread(target=self._run_launch, args=(selected_items,), daemon=True)
        thread.start()

    def _run_launch(self, items: List[LaunchItem]) -> None:
        # Runs on a background thread. Only self.after() calls touch the UI.
        results: List[LaunchResult] = []

        def collect_result(result: LaunchResult) -> None:
            results.append(result)

        self._launcher.launch_items(items, collect_result)
        self.after(0, self._launch_finished, results)

    def _launch_finished(self, results: List[LaunchResult]) -> None:
        self._launch_button.configure(state="normal", text="Launch Workspace")
        message, is_error = self._build_summary_message(results)
        self._status_bar.set_message(message, is_error=is_error)

    @staticmethod
    def _build_summary_message(results: List[LaunchResult]) -> Tuple[str, bool]:
        failed_names = [result.name for result in results if not result.success]
        succeeded_count = len(results) - len(failed_names)

        if not failed_names:
            return f"Launched {succeeded_count}/{len(results)} items successfully.", False

        failed_list = ", ".join(failed_names)
        message = f"Launched {succeeded_count}/{len(results)} items. Couldn't open: {failed_list}."
        return message, True
