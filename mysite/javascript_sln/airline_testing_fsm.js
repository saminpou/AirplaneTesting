var TestType  = {
	'LOW'   	:1,
	'MODERATE'  :2,
	'HIGH'  	:3,
	'SEVERE'	:4,
};

var State  = {
	'BEGIN'						:1,
	'LEVEL_ONE_MANAGER_REVIEW'	:2,
	'ALL_MANAGER_REVIEW'  		:3,
	'CEO_REVIEW'				:4,
	'COMPLETE'					:5,
};

var Actions  = {
	'APPROVE'	:1,
	'RESET'		:2,
};

function enum_name(e,value) 
{
  for (var k in e) if (e[k] == value) return k;
  return null;
}

class Group{
	constructor(name, parent) {
		this.name = name;
		this.parent = parent;
	}
}
class Groups{
	constructor() {
		this.group_names = {};
	}
	add(name, parent_name) {
		var new_group, parent_group;
		if (parent_name === null) {
			new_group = new Group(name, null);
			this.group_names[name] = new_group
		} else if (this.group_names[parent_name] === undefined) {
			console.log("Error finding parent");
		} else {
			parent_group = this.group_names[parent_name];
			new_group = new Group(name, parent_group);
			this.group_names[name] = new_group
		}
	}
	get(name) {
		if (this.group_names[name] === undefined) {
			console.log("Error finding group");
		} else {
			return this.group_names[name];
		}
	}
}



class User{
	constructor (name, email, phone_number, group, uid){
			this.uid = uid
			this.name = name
			this.email = email
			this.phone_number = phone_number
			this.group = group
  	}
  	get_vars(){
			var ret = {'uid':this.uid,'name':this.name,'email':this.email, 'phone_number':this.phone_number, 'group': this.group.name}
			return ret
		}
}

class Users{
	constructor(){
		this.uid_counter = 1
		this.list_users = []
		this.dict_users = {}
	}

	add_user(name, email, phone_number, group){
		var new_user = new User(name, email, phone_number, group, this.uid_counter)
		this.list_users.push(new_user)
		this.dict_users[this.uid_counter] = new_user
		this.uid_counter += 1
	}

	get_users(){
		return this.list_users
	}

	find_user(uid){
		return this.dict_users[uid]
  	}
}




class FSM{
	constructor(test_type, users, author){
		//Level -> { CurrentState -> { Action -> NextState } }
		this.NextState = {
			'1':{
				'1': {'1':'5'}
				},
			'2':{
				'1':{'1':'2'},
				'2':{'1':'5','2':'1'}
				},
			'3':{
				'1':{'1':'3'},
				'3':{'1':'5','2':'1'}
			},
			'4':{
				'1':{'1':'3'},
				'3':{'1':'4','2':'1'},
				'4':{'1':'5','2':'1'}
			}
		}

		this.author = author
		this.test_type = test_type
		this.current_state = State.BEGIN
		this.users_action_log = []
	}

	get_vars(){
		var j = { 'users_action_log': this.users_action_log, 'state': enum_name(State, this.current_state) }
		return j
	}
}

class Request{
	constructor(test_type, users, author, name, description){
		this.name = name
		this.description = description
		this.users = users
		this.fsm = new FSM(test_type, users, author)
	}

	print_request(){
		var request = {'test_type': enum_name(TestType, this.fsm.test_type), 'name': this.name, 'description': this.description}
    var author = this.fsm.author.get_vars()
		var fsm = this.fsm.get_vars()

		request['author'] = author
		request['state_data'] = fsm
		
    request = JSON.stringify(request,null, 4)
		console.log(request)
	}
}

all_groups = new Groups()
all_groups.add('CEO', null)
all_groups.add('Senior Managers','CEO')
all_groups.add('Midlevel Managers','Senior Managers')
all_groups.add('Junior Managers','Midlevel Managers')
all_groups.add('Engineers','Junior Managers')

usrs = new Users()
usrs.add_user('Anna', 'a@a.com', '9055555555', all_groups.get('Engineers'))
usrs.add_user('Bob', 'a@a.com', '9055555555', all_groups.get('Engineers'))
usrs.add_user('Clarise', 'a@a.com', '9055555555', all_groups.get('Junior Managers'))
usrs.add_user('Desmond', 'a@a.com', '9055555555', all_groups.get('Midlevel Managers'))
usrs.add_user('Elis', 'a@a.com', '9055555555', all_groups.get('Senior Managers'))
usrs.add_user('Frank', 'a@a.com', '9055555555', all_groups.get('Senior Managers'))
usrs.add_user('Gomez', 'a@a.com', '9055555555', all_groups.get('CEO'))

var author = usrs.get_users()[0]
var name = "Barrel Roll"
var description = "Do a barrel roll!"

r = new Request(TestType.SEVERE, usrs, author, name, description)
r.fsm.current_state = State.LEVEL_ONE_MANAGER_REVIEW
r.fsm.users_action_log = [{ 'user_name': 'Anna', 'user_group': 'Engineers', 'state': enum_name(State,State.BEGIN), 'action': enum_name(Actions,Actions.APPROVE)}]

r.print_request()




