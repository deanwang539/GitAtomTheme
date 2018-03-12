import sublime
import sublime_plugin

import os
import sys


# Append module directory on PYTHONPATH
sys.path.append(os.path.join(os.path.dirname(__file__), "modules"))
try:
	from .modules import is_work_tree, get_active_project_path, GitRepo, status_manipulate
except ImportError:
    # Failed to import at least one module.
    # This can happen after upgrade due to internal structure changes.
    sublime.message_dialog(
        "GitStatus failed to reload some of its modules.\n"
        "Please restart Sublime Text!")


class GitStatusCommand():
	def __init__(self):
		self.view = sublime.active_window().active_view()
		self.my_repo = get_repo()
		self.is_clean = status_manipulate(self.my_repo.get_git_status())[1] if self.my_repo else None

	def run(self):
		if self.my_repo:
			# Clears the named status.
			self.view.erase_status("info")
			#The value will be displayed in the status bar, in a comma separated list of all status values, ordered by key.
			if self.is_clean:
				self.view.set_status("info", self.my_repo.branch + ": Clean")
			else:
				self.view.set_status("info", self.my_repo.branch + ": Dirty")


class SeeStatusCommand(sublime_plugin.WindowCommand):
	# shortcuts
	def run(self):
		my_repo = get_repo()
		if my_repo:
			git_status_info = my_repo.get_git_status()
			msg = status_manipulate(git_status_info)[0]
			sublime.message_dialog(msg)
		else:
			sublime.message_dialog(
				"GitStatus failed to load because this is not a git project!")


class StatusBarHandler(sublime_plugin.EventListener):
	def check(self):
		GitStatusCommand().run()

	def on_activated_async(self, view):
	# Called when a view gains input focus.
		self.check()

	# def on_clone_async(self, view):
	# # Called when a view is cloned from an existing one.
	# 	self.check()

	# def on_load_async(self, view):
	# 	# Called when the file is finished loading.
	# 	self.check()

	# def on_new_async(self, view):
	# 	# Called when a new buffer is created.
	# 	self.check()

	def on_post_save_async(self, view):
	# Called after a view has been saved.
		self.check()


def get_repo():
	# Init repo object
	repo = None
	path = os.path.normpath(get_active_project_path())
	if is_work_tree(path):
		repo = GitRepo(path)
	return repo


def plugin_loaded():
	# Show initital status
	view = sublime.active_window().active_view()
	my_repo = get_repo()
	if my_repo:
		is_clean = status_manipulate(my_repo.get_git_status())[1]

		# Clears the named status.
		view.erase_status("info")

		#The value will be displayed in the status bar, in a comma separated list of all status values, ordered by key.
		if is_clean:
			view.set_status("info", my_repo.branch + ": Clean")
		else:
			view.set_status("info", my_repo.branch + ": Dirty")
