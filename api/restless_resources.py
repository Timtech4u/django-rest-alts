from restless.dj import DjangoResource
from restless.preparers import FieldsPreparer

from .models import Friend


class FriendResource(DjangoResource):
    preparer = FieldsPreparer(fields={
        'id': 'id',
        'age': 'age',
        'name': 'name',
    })

    # GET /api/v2/friends/
    def list(self):
        return Friend.objects.all()

    # GET /api/v2/friends/<pk>/ 
    def detail(self, pk):
        return Friend.objects.get(id=pk)