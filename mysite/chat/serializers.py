from rest_framework import serializers
from chat.models import ChatJSON


class ChatSerializer(serializers.ModelSerializer):
    version = serializers.DecimalField(max_digits=6, decimal_places=2, coerce_to_string=False)

    class Meta:
        model = ChatJSON
        fields = ('id', 'version', 'script_as_json')
