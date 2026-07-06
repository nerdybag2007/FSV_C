from config import WORKSPACES
from ui.workspace_page import WorkspacePage


class FreedomPage(WorkspacePage):
    """Freedom workspace: placeholder until YouTube/Spotify/etc. are added to config."""

    def __init__(self, master, on_back, **kwargs):
        super().__init__(master, WORKSPACES["freedom"], on_back, **kwargs)
