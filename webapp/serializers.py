from rest_framework import serializers
from .models import clients
from .models import projects


class clientsSerializer(serializers.ModelSerializer):

    class Meta:
        model = clients
        fields='__all__'

class projectsSerializer(serializers.ModelSerializer):

    class Meta:
        model = projects
        fields='__all__'