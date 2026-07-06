from config import WORKSPACES
from ui.workspace_page import WorkspacePage


class GamingPage(WorkspacePage):
    """Gaming workspace: placeholder until Steam/Epic/Discord etc. are added to config."""

    def __init__(self, master, on_back, **kwargs):
        super().__init__(master, WORKSPACES["gaming"], on_back, **kwargs)
