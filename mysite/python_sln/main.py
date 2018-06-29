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
		self.users_action_log = []

	def get_vars(self):
		j = { 'users_action_log': self.users_action_log, 'state': self.current_state }
		return j

class Request(object):
	def __init__(self, test_type, users, author, name, description):
		self.name = name
		self.description = description
		self.users = users
		self.fsm = FSM(test_type, users, author)

	def print_request(self):
		request = {'test_type': self.fsm.test_type.name, 'name': self.name, 'description': self.description}
		author = self.fsm.author.get_vars()
		fsm = self.fsm.get_vars()

		request['author'] = author
		request['state_data'] = fsm
		
		r = json.dumps(request, indent=4, sort_keys=True, cls=enums.EnumEncoder)
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
	r.fsm.current_state = enums.State(2).name
	r.fsm.users_action_log = [{ 'user_name': 'Anna', 'user_group': 'Engineers', 'state': enums.State(1).name, 'action': enums.Actions(1).name}]

	r.print_request()


if __name__ == "__main__":
    sys.exit(main())



