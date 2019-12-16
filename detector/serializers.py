from .models import Black, White
from rest_framework import serializers

class BlackSerializer(serializers.HyperlinkedModelSerializer) : 
    class Meta : 
        model = Black
        fields = ['black_id', 'url']
        lookup_field='url'

class WhiteSerializer(serializers.HyperlinkedModelSerializer) :
    class Meta :
        model = White
        fields = ['url']
        lookup_field='url'