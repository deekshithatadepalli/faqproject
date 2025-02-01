import json
import redis
import os
from django.http import JsonResponse
from .models import FAQ
from .serializers import FAQSerializer  # Import the serializer

# Connect to Redis (for Heroku)
redis_url = os.getenv('REDIS_URL', 'redis://127.0.0.1:6379/1')
redis_client = redis.from_url(redis_url)

def faq_list(request):
    """ Fetch FAQs with caching & translation support """
    lang = request.GET.get('lang', 'en')  # Default language is English
    cache_key = f"faqs_{lang}"  # Generate cache key

    # Check if data is cached
    cached_data = redis_client.get(cache_key)
    if cached_data:
        return JsonResponse({"faqs": json.loads(cached_data)})

    # If not cached, fetch from DB
    faqs = FAQ.objects.all()

    # Initialize the FAQ serializer with the language parameter in the context
    serializer = FAQSerializer(faqs, many=True, context={'lang': lang})

    # Cache the result in Redis (timeout: 10 minutes)
    redis_client.setex(cache_key, 600, json.dumps(serializer.data))

    return JsonResponse({"faqs": serializer.data})
