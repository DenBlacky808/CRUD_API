from rest_framework import viewsets
from .models import Client
from .serializers import UserSerializer
from .permissions import IsOwnerOrReadOnly


class UserViewset(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsOwnerOrReadOnly,)
