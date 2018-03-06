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

#repo = GitRepo("C:/Users/Dean/AppData/Roaming/Sublime Text 3/Packages/GitAtomTheme")
repo = GitRepo("/Users/Hao/Library/Application Support/Sublime Text 3/Packages/GitStatus")

class GitStatusCommand(sublime_plugin.WindowCommand): #sublime_plugin.TextCommand):
	def run(self, view): #, edit):
		#self.view.insert(edit, 0, str(repo.is_clean()))
		print ("============ test ===============")
		print (str(repo.is_clean()))
		print (repo.get_untracked_files())
		print (repo.get_unstaged_files())
		print (repo.get_staged_files())
		print ("------------")
		print (repo.add_del)
		print (repo.modified)


		"""status bar info"""

		# Clears the named status.
		view.erase_status("info")

		#The value will be displayed in the status bar, in a comma separated list of all status values, ordered by key.
		if repo.is_clean():
			view.set_status("info", "git: Clean")
		else:
			view.set_status("info", "git: Dirty")


"""
These events are triggered by the buffer underlying the view,
and thus the method is only called once,
with the first view as the parameter
"""
class EventListener(sublime_plugin.EventListener):

    def check(self, view):
        git_status = GitStatusCommand(sublime.active_window())
        git_status.run(view)

    def on_new(self, view):
    	# Called when a new buffer is created.
    	self.check(view)

    def on_clone(self, view):
    	# Called when a view is cloned from an existing one.
        self.check(view)

    """
    def on_modified(self, view):
    	# Called after changes have been made to a view.
    	self.check()
	"""

    def on_post_save(self, view):
    	# Called after a view has been saved.
        self.check(view)


    def on_activated(self, view):
    	# Called when a view gains input focus.
        self.check(view)
