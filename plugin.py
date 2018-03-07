import sublime
import sublime_plugin

import os
import sys

# Append module directory on PYTHONPATH
sys.path.append(os.path.join(os.path.dirname(__file__), "modules"))
try:
	from .modules import is_work_tree, get_active_project_path, GitRepo
except ImportError:
    # Failed to import at least one module.
    # This can happen after upgrade due to internal structure changes.
    sublime.message_dialog(
        "GitStatus failed to reload some of its modules.\n"
        "Please restart Sublime Text!")


class GitStatusCommand(sublime_plugin.WindowCommand):
	def __init__(self, view):
		self.view = view

		# Check if the project folder is a valid git repository
		path = os.path.normpath(get_active_project_path())
		if is_work_tree(path):
			self.repo = GitRepo(path)
		else:
			sublime.message_dialog(
				"GitStatus failed to load because this is not a git repository.")

	def run(self):
		# print ("============ test ===============")
		# print (str(repo.is_clean()))
		# print (repo.add_del)
		# print (repo.modified)

		# Clears the named status.
		self.view.erase_status("info")

		#The value will be displayed in the status bar, in a comma separated list of all status values, ordered by key.
		if self.repo.is_clean():
			self.view.set_status("info", self.repo.branch + ": Clean")
		else:
			self.view.set_status("info", self.repo.branch + ": Dirty")



class StatusBarHandler(sublime_plugin.EventListener):
	def check(self):
		git_status = GitStatusCommand(sublime.active_window().active_view())
		git_status.run()

	def on_activated_async(self, view):
	# Called when a view gains input focus.
		self.check()

	def on_clone_async(self, view):
	# Called when a view is cloned from an existing one.
		self.check()

	def on_post_save_async(self, view):
	# Called after a view has been saved.
		self.check()
		# New view
		createdView = sublime.active_window().new_file()
		createdView.run_command("insert",{"characters": "Hello"})
