import users

class Group(object):
	def __init__(self, name, parent):
		self.name = name
		self.parent = parent

class Groups(object):
	def __init__(self):
		self.group_names = {}
	
	def add(self, name, parent_name):
		if parent_name is None:
			new_group = Group(name, None)
			self.group_names[name] = new_group
		elif parent_name not in self.group_names:
			print('Error finding parent')
		else:
			parent_group = self.group_names[parent_name]
			new_group = Group(name, parent_group)
			self.group_names[name] = new_group

	def get(self, name):
		if name not in self.group_names:
			print('Error finding group')
		else:
			return self.group_names[name]



