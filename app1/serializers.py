from rest_framework import serializers
from .models import My_Model


class My_ModelSerialaizer(serializers.ModelSerializer):
    class Meta:
        model = My_Model
        fields = ('name', 'age', 'date_of_born')
