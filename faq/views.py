import json
import redis
import os
from django.http import JsonResponse
from .models import FAQ
from .serializers import FAQSerializer
from urllib.parse import urlparse

# Parse Redis URL to handle SSL configuration - try REDISCLOUD_URL first
redis_url = os.getenv('REDISCLOUD_URL', os.getenv('REDIS_URL', 'redis://localhost:6380/1'))
url = urlparse(redis_url)

# Configure Redis client
if url.scheme == 'rediss':
    # SSL/TLS connection
    redis_client = redis.Redis(
        host=url.hostname,
        port=url.port,
        username=url.username,
        password=url.password,
        ssl=True,
        ssl_cert_reqs=None,
        decode_responses=True,
        socket_timeout=5,
        socket_connect_timeout=5,
        socket_keepalive=True,
        health_check_interval=30
    )
else:
    # Non-SSL connection
    redis_client = redis.from_url(
        redis_url,
        decode_responses=True,
        socket_timeout=5,
        socket_connect_timeout=5
    )


def faq_list(request):
    """ Fetch FAQs with caching & translation support """
    try:
        lang = request.GET.get('lang', 'en')
        cache_key = f"faqs_{lang}"

        # Check if data is cached in Redis
        cached_data = redis_client.get(cache_key)
        if cached_data:
            return JsonResponse({"faqs": json.loads(cached_data)})

        # If no cache, fetch FAQs from the database
        faqs = FAQ.objects.all()
        serializer = FAQSerializer(faqs, many=True, context={'lang': lang})

        # Cache the result in Redis for 10 minutes (600 seconds)
        redis_client.setex(cache_key, 600, json.dumps(serializer.data))

        return JsonResponse({"faqs": serializer.data})
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)