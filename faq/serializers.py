from rest_framework import serializers
from .models import FAQ


class FAQSerializer(serializers.ModelSerializer):
    # Translate question and answer dynamically based on the language
    class Meta:
        model = FAQ
        fields = ['id', 'question', 'answer', 'question_hi', 'question_bn']

    def to_representation(self, instance):
        """Override to_representation to add language translation support."""
        representation = super().to_representation(instance)
        lang = self.context.get('lang', 'en')
        # Get the language parameter from the context

        # Get the translated question and answer based on the language
        translated_question = instance.get_question_in_language(lang)
        translated_answer = instance.answer
        # Assume answer is always in English

        if lang != 'en':
            translated_answer = instance.translate_question(lang)
            # Translate answer if needed

        # Modify the representation
        representation['question'] = translated_question
        representation['answer'] = translated_answer

        return representation
