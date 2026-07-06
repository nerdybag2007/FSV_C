from config import WORKSPACES
from ui.workspace_page import WorkspacePage


class CodingPage(WorkspacePage):
    """Coding workspace: VS Code, Brave, and coding-related websites."""

    def __init__(self, master, on_back, **kwargs):
        super().__init__(master, WORKSPACES["coding"], on_back, **kwargs)
