from scrapy.utils.misc import load_object

# Default values.
REDIS_URL = None
REDIS_HOST = 'localhost'
REDIS_PORT = 6379


def from_settings(settings):
    if settings.get('REDIS_CONNECTION_POOL_INSTANCE', None):
        ri = load_object(settings.get('REDIS_CONNECTION_POOL_INSTANCE'))
        ri.getConn()
    else:
        import redis
        url = settings.get('REDIS_URL',  REDIS_URL)
        host = settings.get('REDIS_HOST', REDIS_HOST)
        port = settings.get('REDIS_PORT', REDIS_PORT)

        # REDIS_URL takes precedence over host/port specification.
        if url:
            return redis.from_url(url)
        else:
            return redis.Redis(host=host, port=port)
