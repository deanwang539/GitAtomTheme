
''' git status info manipulate'''

def status_manipulate(msg):

	modified_files = []
	deleted_files = []
	added_files = []

	modified_tag = "modified:"
	deleted_tag = "deleted:"
	added_tag = "Untracked files:"
	end_tag = "no changes added"

	#msg = msg.replace("\n", "")
	msg = msg.replace("\t", " ")

	if modified_tag in msg:
	# collect modified files
		mod_msg = msg.split(modified_tag)
		for i in range(len(mod_msg)):
			if i != 0 and i != len(mod_msg) - 1:
				modified_files.append(mod_msg[i].strip())
			elif i == len(mod_msg) - 1:
			# collect last one
				if deleted_tag in mod_msg[i]:
					modified_files.append(mod_msg[i].split(deleted_tag)[0].strip())
				elif added_tag in mod_msg[i]:
					modified_files.append(mod_msg[i].split(added_tag)[0].strip())
				else:
					modified_files.append(mod_msg[i].split(end_tag)[0].strip())

				msg = mod_msg[i]

	if deleted_tag in msg:
	# collect deleted files
		del_msg = msg.split(deleted_tag)
		for i in range(len(del_msg)):
			if i != 0 and i != len(del_msg) - 1:
				deleted_files.append(del_msg[i])
			elif i == len(del_msg) - 1:
			# collect last one
				if added_tag in del_msg[i]:
					deleted_files.append(del_msg[i].split(added_tag)[0].strip())
				else:
					deleted_files.append(del_msg[i].split(end_tag)[0].strip())
				msg = del_msg[i]

	if added_tag in msg:
	# collect untracked files
		add_msg = msg.split(added_tag)[1].split("be committed)")[1].split(end_tag)[0].split("\n")
		for i in range(2):
			del(add_msg[0])
			del(add_msg[len(add_msg)-1])

		for j in range(len(add_msg)):
			added_files.append(add_msg[j].strip())

	return handle_message_dialog(modified_files, deleted_files, added_files)



def handle_message_dialog(m_mod, m_del, m_add):
	print (m_mod)
	print (m_del)
	print (m_add)

	message = 'Git Status:\n\n'
	if len(m_mod) != 0:
		message = message + "modified:\n"
	for i in range(len(m_mod)):
		message = message + '\t' + m_mod[i] + '\n'

	if len(m_del) != 0:
		message = message + "\ndeleted:\n"
	for i in range(len(m_del)):
		message = message + '\t' + m_del[i] + '\n'

	if len(m_add) != 0:
		message = message + "\nuntracked:\n"
	for i in range(len(m_add)):
		message = message + '\t' + m_add[i] + '\n'

	if len(m_mod) == 0 and len(m_del) == 0 and len(m_add) == 0:
		message = message + 'nothing to commit, working tree clean'

	return message

