import sys
from enum import Enum
import copy
import json
import groups
import users
import enums

class FSM(object):
	def __init__(self, test_type, users, author):
		self.NextState = {
			'1':{
				'1': {'1':'5'}
				},
			'2':{
				'1':{'1':'2'},
				'2':{'1':'5','2':'1'}
				},
			#High
			'3':{
				'1':{'1':'3'},
				'3':{'1':'5','2':'1'}
			},
			#Severe
			'4':{
				'1':{'1':'3'},
				'3':{'1':'4','2':'1'},
				'4':{'1':'5','2':'1'}
			}
		}

		self.author = author
		self.test_type = test_type
		self.current_state = enums.State.BEGIN
		self.users_approved = []

		# Sets used for conditional fsm procedures
		self.lvl_one_mgr_set = set([])
		self.all_mgr_set = set([])
		self.cur_mgr_set = set([])
		self.ceo_set = set([])

		for usr in users.get_users():
			if usr.group is self.author.group - 1:
				self.lvl_one_mgr_set.add(usr.uid)
			elif usr.group > self.author.group:
				self.all_mgr_set.add(usr.uid)
				self.cur_mgr_set.add(usr.uid)
			elif usr.group is 1:
				self.ceo_set.add(usr.uid)

	def isAuthorized(cur, nxt, user):
		self.users_approved.append({ 'user_name': user.name, 'user_group': user.group, state: enums.State(cur).name}, )
		if cur == 1 and (nxt == 2 or nxt == 3):
			if user.uid == self.author.uid:
				return True
			return False

		if cur == 2 and nxt == 5:
			if user.uid in self.lvl_one_mgr_set:
				self.users_approved.append({ 'user_name': user.name, 'user_group': user.group, state: enums.State(cur).name})
				return True
			return False

		if cur == 3 and (nxt == 4 or nxt == 5):
			if user.uid in self.cur_mgr_set:
				self.users_approved.append({ 'user_name': user.name, 'user_group': user.group, state: enums.State(cur).name})
				self.cur_mgr_set.remove(user.uid)
			if len(self.cur_mgr_set.union(self.all_mgr_set)) is 0:
				return True
			return False

		if cur == 4 and nxt == 5:
			if user.uid in self.ceo_set:
				self.users_approved.append({ 'user_name': user.name, 'user_group': user.group, state: enums.State(cur).name})
				return True
			return False

		if nxt == 1:
			self.cur_mgr_set = copy.deepcopy(self.all_mgr_set)
			self.users_approved = []
			return true

	def get_json(self):
		j = { 'users_approved': self.users_approved, 'state': self.current_state }
		return j
		#return json.dumps(j, cls=enums.EnumEncoder)

class Request(object):
	def __init__(self, test_type, users, author, name, description):
		self.author = author
		self.test_type = test_type
		self.name = name
		self.description = description
		self.users = users
		self.fsm = FSM(test_type, users, author)

	def print_request(self):
		request = {'test_type': self.test_type.name, 'name': self.name, 'description': self.description}
		author = vars(self.author)
		fsm = self.fsm.get_json()

		request['author'] = author
		request['approval_data'] = fsm
		
		r = json.dumps(request, cls=enums.EnumEncoder)
		print(r)

def main():

	all_groups = groups.Groups()
	all_groups.add('CEO', None)
	all_groups.add('Senior Managers','CEO')
	all_groups.add('Midlevel Managers','Senior Managers')
	all_groups.add('Junior Managers','Midlevel Managers')
	all_groups.add('Engineers','Junior Managers')

	usrs = users.Users()
	usrs.add_user('Anna', 'a@a.com', '9055555555', all_groups.get('Engineers'))
	usrs.add_user('Bob', 'a@a.com', '9055555555', all_groups.get('Engineers'))
	usrs.add_user('Clarise', 'a@a.com', '9055555555', all_groups.get('Junior Managers'))
	usrs.add_user('Desmond', 'a@a.com', '9055555555', all_groups.get('Midlevel Managers'))
	usrs.add_user('Elis', 'a@a.com', '9055555555', all_groups.get('Senior Managers'))
	usrs.add_user('Frank', 'a@a.com', '9055555555', all_groups.get('Senior Managers'))
	usrs.add_user('Gomez', 'a@a.com', '9055555555', all_groups.get('CEO'))

	author = usrs.get_users()[0]
	name = "Barrel Roll"
	description = "Do a barrel roll!"

	r = Request(enums.TestType.SEVERE, usrs, author, name, description)
	r.print_request()


if __name__ == "__main__":
    sys.exit(main())



