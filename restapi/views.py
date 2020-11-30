from gait.models import Gaitdata
from restapi.serializers import GaitdataSerializer, UserSerializer
from rest_framework import generics
from accounts.models import CustomUser
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.utils import timezone

class GaitDataList(generics.ListCreateAPIView):
    serializer_class = GaitdataSerializer

#    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return Gaitdata.objects.filter(owner=user)

    def perform_create(self, serializer):
        print("trying to create item...")
        serializer.save(owner=self.request.user, created_date=timezone.now())


class GaitDataDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GaitdataSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return Gaitdata.objects.filter(owner=user)


class UserList(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)

class UserDetail(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)
