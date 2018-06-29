from tastypie.resources import ModelResource
from dbtest.models import Request

class UserResource(ModelResource):
    class Meta:
        queryset = Request.objects.all()
        resource_name = 'request'