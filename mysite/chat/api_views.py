from rest_framework import generics
from chat.serializers import ChatSerializer
from chat.models import ChatJSON


class ChatList(generics.ListCreateAPIView):
    queryset = ChatJSON.objects.all()
    serializer_class = ChatSerializer
