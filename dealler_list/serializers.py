from rest_framework.serializers import ModelSerializer
from dealler_list.models import models


class mytableSerializer(ModelSerializer):
    class Meta:
        model = models
        fields = '__all__'

