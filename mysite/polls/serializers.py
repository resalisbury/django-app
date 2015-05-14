from rest_framework import serializers
from polls.models import Question, Choice


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'question_text', 'pub_date')


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('question', 'choice_text', 'votes')
