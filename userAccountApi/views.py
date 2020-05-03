from rest_framework import viewsets

from userAccountApi.models import User
from userAccountApi.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
view rawviews.py hosted with ❤ by GitHub