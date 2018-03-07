"""
GitAtomTheme modules.

Define all API classes here, which need to be exported to sublime plugin.
"""

from .path import is_work_tree, get_active_project_path
from .git_repo import GitRepo
from .manipulate import status_manipulate, handle_message_dialog
