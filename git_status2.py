# import sublime
# import sublime_plugin

# # Initialize repo for current working tree
# repo = None
# active_project_path = get_active_project_path()
# print(active_project_path)
# if is_work_tree(active_project_path):
# 	repo = GitRepo(active_project_path)
# else:
#     sublime.message_dialog(
#     	"GitStatus failed to load because this is not a git repository.")

# """
# Main command for showing git info in status bar
# """
# class GitStatusCommand(sublime_plugin.WindowCommand):
# 	def run(self):
# 		# print ("============ test ===============")
# 		# print (str(repo.is_clean()))
# 		# print (repo.add_del)
# 		# print (repo.modified)

# 		"""status bar info"""

# 		# Get current view.
# 		view = sublime.active_window().active_view()

# 		# Clears the named status.
# 		view.erase_status("info")

# 		#The value will be displayed in the status bar, in a comma separated list of all status values, ordered by key.
# 		if repo.is_clean():
# 			view.set_status("info", "git: Clean")
# 		else:
# 			view.set_status("info", "git: Dirty")

# """
# These events are triggered by the buffer underlying the view,
# and thus the method is only called once,
# with the first view as the parameter
# """
# class PluginLoad(sublime_plugin.EventListener):

#     def check(self):
#         git_status = GitStatusCommand(sublime.active_window())
#         git_status.run()

#     def on_new(self, view):
#     	# Called when a new buffer is created.
#     	self.check()

#     def on_clone(self, view):
#     	# Called when a view is cloned from an existing one.
#         self.check()

#     """
#     def on_modified(self, view):
#     	# Called after changes have been made to a view.
#     	self.check()
# 	"""

#     def on_post_save(self, view):
#     	# Called after a view has been saved.
#         self.check()

#     def on_activated(self, view):
#     	# Called when a view gains input focus.
#         self.check()
