from rest_framework import serializers
from accounts.models import CustomUser
from gait.models import Gaitdata

class GaitdataSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    created_date = serializers.ReadOnlyField()
    class Meta:
        model = Gaitdata
        fields = ('id', 'created_date', 'data_json', 'owner')


class UserSerializer(serializers.ModelSerializer):
    gaitdata = serializers.PrimaryKeyRelatedField(many=True, queryset=Gaitdata.objects.all())

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'gaitdata')
