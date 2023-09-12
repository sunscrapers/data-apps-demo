import os

from dash import Dash
from flask_caching import Cache
from redis.exceptions import ConnectionError as RedisConnectionError


def get_cache_client(dash_app: Dash) -> Cache:
    cache_client: Cache = Cache(
        dash_app.server,
        config={
            "CACHE_TYPE": "redis",
            "CACHE_REDIS_URL": os.environ.get("REDIS_URL", ""),
        },
    )

    try:
        cache_client.set("ping", "XYZ", timeout=1)
    except RedisConnectionError:
        return Cache(dash_app.server, config={"CACHE_TYPE": "SimpleCache"})
    return cache_client


app: Dash = Dash(__name__)
cache: Cache = get_cache_client(dash_app=app)
