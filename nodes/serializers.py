from rest_framework import serializers
from .models import Bubble

class BubbleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bubble
        fields = ('id' ,'group', 'radius', 'citing_patents_count')