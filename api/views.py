from django.shortcuts import render

# Create your views here.


from jsonview.decorators import json_view


@json_view
def my_api_view(request):
    return {
        'foo': 'bar',
    }