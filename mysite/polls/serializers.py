from rest_framework import serializers
from polls.models import Question, Choice


class QuestionSerializer(serializers.ModelSerializer):
    choices = serializers.StringRelatedField(many=True)

    class Meta:
        model = Question
        fields = ('id', 'question_text', 'pub_date', 'choices')


class ChoiceSerializer(serializers.ModelSerializer):
    question_text = serializers.ReadOnlyField(source='question.question_text')

    class Meta:
        model = Choice
        fields = ('question', 'question_text', 'choice_text', 'votes')
