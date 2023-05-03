'''
Serializers allow complex data such as querysets and model instances to be
converted to native Python datatypes that can then be easily rendered
into JSON, XML or other content types.
Serializers also provide deserialization, allowing parsed data to be
converted back into complex types, after first validating the incoming data.
'''

from rest_framework import serializers
from mainapp.models import PodcastModel, PodcasterModel, ContactModel

class PodcastSerializer(serializers.ModelSerializer):
    class Meta:
        model = PodcastModel
        fields = '__all__'
        
class PodcasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = PodcasterModel
        fields = '__all__'

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactModel
        fields = ('id', 'firstname', 'lastname', 'email', 'subject', 'message', 'sendtime')