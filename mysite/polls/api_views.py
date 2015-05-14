from rest_framework import generics
from polls.serializers import QuestionSerializer, ChoiceSerializer
from polls.models import Question, Choice


class QuestionList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class ChoiceList(generics.ListCreateAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
