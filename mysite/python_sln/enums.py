from enum import Enum
import json

class TestType(Enum):
	LOW = 1
	MODERATE = 2
	HIGH = 3
	SEVERE = 4

class State(Enum):
	BEGIN = 1
	LEVEL_ONE_MANAGER_REVIEW = 2
	ALL_MANAGER_REVIEW = 3
	CEO_REVIEW = 4
	COMPLETE = 5

class Actions(Enum):
	APPROVE = 1
	RESET = 2

class EnumEncoder(json.JSONEncoder):
	def default(self, obj):
	    if isinstance(obj, Enum):
	        return obj.name
	    return json.JSONEncoder.default(self, obj)

def serialize(obj):
    if isinstance(obj, Enum):
        serial = obj.isoformat()
        return serial

    if isinstance(obj, time):
        serial = obj.isoformat()
        return serial

    return obj.__dict__	