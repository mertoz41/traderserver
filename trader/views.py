from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

from django.http import HttpResponse
from django.contrib.auth.models import User

def index(request):
    return HttpResponse("Hello world, this is the beginning of a trader app")

@api_view(['POST'])
def create_new_user(request):
    parsed = JSONParser().parse(request)
    user = User.objects.create(
        first_name=parsed["user"]["firstName"], 
        last_name=parsed["user"]["lastName"],
        email=parsed["user"]["email"],
        password=parsed["user"]["password"]
        )
    print(user)
    return Response({"new_user": user})