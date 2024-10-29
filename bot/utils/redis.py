from redis.asyncio import Redis

from core.config import settings


redis = Redis(
    host=settings.redis.host,
    port=settings.redis.port,
    decode_responses=settings.redis.decode_responses,
)
