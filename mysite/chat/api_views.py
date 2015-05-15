import json

from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from chat.serializers import ChatSerializer
from chat.models import ChatJSON


class ChatList(generics.ListCreateAPIView):
    queryset = ChatJSON.objects.all()
    serializer_class = ChatSerializer


class ChatDetail(generics.RetrieveAPIView):
    queryset = ChatJSON.objects.all()
    serializer_class = ChatSerializer
    lookup_field = 'version'


class ChatModule(APIView):

    def get(self, request, guid, version, format=None):
        try:
            chat = ChatJSON.objects.get(version=float(version))
            script = chat.script
        except ChatJSON.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        with open(script.path, 'r') as data_file:
            data = json.load(data_file)

        try:
            response = self.get_guid(guid, data)
        except KeyError:
            return Response(status=status.HTTP_404_NOT_FOUND)

        return Response(response)

    def get_guid(self, guid, data):
        steps = self.get_steps(data['modules'])
        for step in steps:
            if step['guid'] == guid:
                return step
        raise KeyError

    def get_steps(self, modules):
        steps = []
        for module in modules:
            steps += module['steps']
        return steps
