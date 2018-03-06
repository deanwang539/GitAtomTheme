import sublime
import sublime_plugin

import os
import sys

# Append module directory on PYTHONPATH
sys.path.append(os.path.join(os.path.dirname(__file__), "modules"))


try:
	from .modules import is_work_tree, GitRepo
except ImportError:
    # Failed to import at least one module.
    # This can happen after upgrade due to internal structure changes.
    sublime.message_dialog(
        "GitAtomTheme failed to reload some of its modules.\n"
        "Please restart Sublime Text!")

repo = GitRepo("C:/Users/Dean/AppData/Roaming/Sublime Text 3/Packages/GitAtomTheme")
# print(repo.is_clean())
# print(repo.add_del)
# print(repo.modified)

class ExampleCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		self.view.insert(edit, 0, str(repo.is_clean()))
