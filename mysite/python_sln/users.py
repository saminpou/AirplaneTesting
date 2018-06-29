import groups


class User(object):
	def __init__(self, name, email, phone_number, group, uid):
		self.uid = uid
		self.name = name
		self.email = email
		self.phone_number = phone_number
		self.group = group

	def get_vars(self):
		ret = vars(self)
		ret['group'] = ret['group'].name
		return ret

class Users(object):
	def __init__(self):
		self.uid_counter = 1
		self.list_users = []
		self.dict_users = {}

	def add_user(self, name, email, phone_number, group):
		new_user = User(name, email, phone_number, group, self.uid_counter)
		self.list_users.append(new_user)
		self.dict_users[self.uid_counter] = new_user
		self.uid_counter += 1

	def get_users(self):
		return self.list_users

	def find_user(self, uid):
		return self.dict_users[uid]
