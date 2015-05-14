from rest_framework import serializers
from chat.models import ChatJSON


class ChatSerializer(serializers.ModelSerializer):

    class Meta:
        model = ChatJSON
        fields = ('id', 'version', 'script_as_json')
