from tastypie.resources import ModelResource
from .models import Friend


class FriendResource(ModelResource):
    class Meta:
        queryset = Friend.objects.all()

