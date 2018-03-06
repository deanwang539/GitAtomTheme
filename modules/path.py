import os
import sublime

def is_work_tree(path):
	"""Check if 'path' is a valid git working tree.
	A working tree contains a ".git" directory.

	Arguments:
	    path (string): The path to check.

	Returns:
	    bool: True if path contains a ".git"
	"""
	return path and ".git" in os.listdir(path)

def get_active_project_path():
	"""
	Arguments:
		None

	Return:
		str: current project folder path
	"""
	window = sublime.active_window()
	folders = window.folders()
	if len(folders) == 1:
		return folders[0]
	else:
		active_view = window.active_view()
		active_file_name = active_view.file_name() if active_view else None
		if not active_file_name:
			return folders[0] if len(folders) else os.path.expanduser("~")
		for folder in folders:
			if active_file_name.startswith(folder):
				return folder
		return os.path.dirname(active_file_name)
