import redis

redis_host = "localhost"
redis_port = 6379
redis_password = ""

class RedisURL:
    def __init__(self):
        self.redis_db = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)

    def set_url(self, url):
        self.redis_db.lpush("urls", url)

    def get_urls(self):
        return self.redis_db.lrange("urls", 0, -1)
