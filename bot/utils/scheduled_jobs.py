from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.interval import IntervalTrigger

from .jetton_utils import transfer_jettons

from redis.asyncio import Redis

scheduler = AsyncIOScheduler()


def add_jobs(redis: Redis) -> None:
    scheduler.add_job(
        transfer_jettons,
        trigger=IntervalTrigger(minutes=2),
        args=(redis,),
    )
