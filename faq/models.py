from django.db import models
from django.core.cache import cache
from googletrans import Translator
from ckeditor.fields import RichTextField


class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()

    # Fields for various language translations
    question_hi = models.TextField(blank=True, null=True)  # Hindi
    question_bn = models.TextField(blank=True, null=True)  # Bengali
    question_ta = models.TextField(blank=True, null=True)  # Tamil
    question_te = models.TextField(blank=True, null=True)  # Telugu
    question_mr = models.TextField(blank=True, null=True)  # Marathi
    question_gu = models.TextField(blank=True, null=True)  # Gujarati
    question_ml = models.TextField(blank=True, null=True)  # Malayalam
    question_kn = models.TextField(blank=True, null=True)  # Kannada
    question_pa = models.TextField(blank=True, null=True)  # Punjabi
    question_ur = models.TextField(blank=True, null=True)  # Urdu
    question_or = models.TextField(blank=True, null=True)  # Odia

    def translate_question(self, lang):
        """Retrieve cached translation or generate a new one."""
        cache_key = f'faq_{self.id}_{lang}'
        translation = cache.get(cache_key)

        if not translation:
            try:
                # Using Google Translator for language translation
                translator = Translator()
                translated_text = translator.translate(self.question, dest=lang).text
                cache.set(cache_key, translated_text, timeout=86400)  # Cache for 1 day
                translation = translated_text
            except Exception as e:
                print(f"Error while translating: {e}")
                return self.question  # Fallback to the original question
        return translation

    def get_question_in_language(self, lang):
        """Return translated question based on language preference."""
        # First, check for the cached translation
        translation = self.translate_question(lang)
        # If translation is not available in cache, fallback to default question or language-specific fields
        if not translation:
            if lang == 'hi' and self.question_hi:
                return self.question_hi
            elif lang == 'bn' and self.question_bn:
                return self.question_bn
            elif lang == 'ta' and self.question_ta:
                return self.question_ta
            elif lang == 'te' and self.question_te:
                return self.question_te
            elif lang == 'mr' and self.question_mr:
                return self.question_mr
            elif lang == 'gu' and self.question_gu:
                return self.question_gu
            elif lang == 'ml' and self.question_ml:
                return self.question_ml
            elif lang == 'kn' and self.question_kn:
                return self.question_kn
            elif lang == 'pa' and self.question_pa:
                return self.question_pa
            elif lang == 'ur' and self.question_ur:
                return self.question_ur
            elif lang == 'or' and self.question_or:
                return self.question_or
            else:
                return self.question  # Fallback to default question

        return translation

    def save(self, *args, **kwargs):
        """Automatically generate translations when saving."""
        translator = Translator()

        # Generate translations only if they are empty
        if not self.question_hi:
            try:
                self.question_hi = translator.translate(self.question, dest='hi').text
            except Exception as e:
                print(f"Error while translating to Hindi: {e}")
        if not self.question_bn:
            try:
                self.question_bn = translator.translate(self.question, dest='bn').text
            except Exception as e:
                print(f"Error while translating to Bengali: {e}")
        if not self.question_ta:
            try:
                self.question_ta = translator.translate(self.question, dest='ta').text
            except Exception as e:
                print(f"Error while translating to Tamil: {e}")
        if not self.question_te:
            try:
                self.question_te = translator.translate(self.question, dest='te').text
            except Exception as e:
                print(f"Error while translating to Telugu: {e}")
        if not self.question_mr:
            try:
                self.question_mr = translator.translate(self.question, dest='mr').text
            except Exception as e:
                print(f"Error while translating to Marathi: {e}")
        if not self.question_gu:
            try:
                self.question_gu = translator.translate(self.question, dest='gu').text
            except Exception as e:
                print(f"Error while translating to Gujarati: {e}")
        if not self.question_ml:
            try:
                self.question_ml = translator.translate(self.question, dest='ml').text
            except Exception as e:
                print(f"Error while translating to Malayalam: {e}")
        if not self.question_kn:
            try:
                self.question_kn = translator.translate(self.question, dest='kn').text
            except Exception as e:
                print(f"Error while translating to Kannada: {e}")
        if not self.question_pa:
            try:
                self.question_pa = translator.translate(self.question, dest='pa').text
            except Exception as e:
                print(f"Error while translating to Punjabi: {e}")
        if not self.question_ur:
            try:
                self.question_ur = translator.translate(self.question, dest='ur').text
            except Exception as e:
                print(f"Error while translating to Urdu: {e}")
        if not self.question_or:
            try:
                self.question_or = translator.translate(self.question, dest='or').text
            except Exception as e:
                print(f"Error while translating to Odia: {e}")

        super().save(*args, **kwargs)

    def __str__(self):
        return self.question
