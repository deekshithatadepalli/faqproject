import redis
import ssl
# Create an SSL context
ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE  # Disable certificate verification if needed

# Use the Redis URL with SSL
r = redis.StrictRedis.from_url(
    'rediss://:p82f6a2e589572606c5b497ff19ce30ce289d1a601adf16eb59c3f368f0684f77@ec2-44-195-160-84.compute-1.amazonaws.com:28610',
    ssl_context=ssl_context
)
# Try setting a test key
r.set('test_key', 'test_value')
# Retrieve and print the test value
print(r.get('test_key'))

