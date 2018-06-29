# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Low, Medium, High, Severe
class Process(models.Model):
	name = models.CharField(
		max_length=30,
		blank=True
	)

	def __unicode__(self):
		return '{0}'.format(self.name)

class User(models.Model):

	first_name = models.CharField(
		max_length=30,
		blank=True
	)

	last_name = models.CharField(
		max_length=30,
		blank=True
	)

	email = models.EmailField(
		unique=True,
		max_length=255
	)

	phone = models.CharField(
		max_length=400,
		null=True,
		blank=True,
	)

	def __unicode__(self):
		return '{0}'.format(self.first_name)

# Start, Normal, Complete, Denied, Cancelled
class StateType(models.Model):
	#eg. Severe - Get CEO approval
	name = models.CharField(
		max_length=30,
		blank=True
	)
	def __unicode__(self):
		return '{0}'.format(self.name)

# Get CEO Approval, get Author Approval, ect
class State(models.Model):
	#eg. Severe - Get CEO approval
	name = models.CharField(
		max_length=30,
		blank=True
	)

	# Is the state complete
	is_complete = models.BooleanField(
		default=False,
	)

	process = models.ForeignKey(Process)
	state_type = models.ForeignKey(StateType)

	def __unicode__(self):
		return '{0}'.format(self.name)


# Create your models here.
class Request(models.Model):

	title = models.CharField(
		max_length=700,
	)

	summary = models.TextField(
		max_length=6000,
	)

	author = models.ForeignKey(User)
	process = models.ForeignKey(Process)
	current_state = models.ForeignKey(State)

	def __unicode__(self):
		return '{0}'.format(self.title)

class Transition(models.Model):
	process = models.ForeignKey(Process)
	current_state = models.ForeignKey(State, related_name='transition_current')
	next_state = models.ForeignKey(State, related_name='transition_next')

	def __unicode__(self):
		return '{0}->{1}'.format(self.current_state.name, self.next_state.name)

# Approve, Deny, Cancel, Restart, Resolve
class ActionType(models.Model):
	process = models.ForeignKey(Process)
	name = models.CharField(
		max_length=30,
		blank=True
	)

	def __unicode__(self):
		return '{0}'.format(self.name)

class Action(models.Model):
	process = models.ForeignKey(Process)
	action_type = models.ForeignKey(ActionType)
	transition_action = models.ManyToManyField(Transition)

	name = models.CharField(
		max_length=30,
		blank=True
	)
	description = models.CharField(
		max_length=30,
		blank=True
	)


	def __unicode__(self):
		return '{0}'.format(self.name)

class Group(models.Model):
	process = models.ForeignKey(Process)
	name = models.CharField(
		max_length=30,
		blank=True
	)
	group_member = models.ManyToManyField(User)

	def __unicode__(self):
		return '{0}'.format(self.name)

class ActionTarget(models.Model):
	action = models.ForeignKey(Action)
	# Fkey to user

	user = models.ForeignKey(User)
	group = models.ForeignKey(Group)

class RequestAction(models.Model):
	request = models.ForeignKey(Request)
	action = models.ForeignKey(Action)
	transition = models.ForeignKey(Transition)

	is_active = models.BooleanField(
		default=True,
	)

	is_complete = models.BooleanField(default=False)

class UserAction(models.Model):
	request = models.ForeignKey(Request)
	action = models.ForeignKey(Action)
	user = models.ForeignKey(User)
	state = models.ForeignKey(State)
	created_on = models.DateTimeField(auto_now_add=True)

