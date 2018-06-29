# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from dbtest.models import Process,User,StateType,State,Request,Transition,ActionType,Action,Group,ActionTarget,RequestAction, UserAction

# Register your models here.

admin.site.register(Process)
admin.site.register(User)
admin.site.register(StateType)
admin.site.register(State)
admin.site.register(Request)
admin.site.register(Transition)
admin.site.register(ActionType)
admin.site.register(Action)
admin.site.register(Group)
admin.site.register(ActionTarget)
admin.site.register(RequestAction)
admin.site.register(UserAction)

