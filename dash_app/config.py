import os

from dash import Dash
from flask_caching import Cache


def get_cache_client(dash_app: Dash) -> Cache:
    cache_client: Cache = Cache(
        dash_app.server,
        config={
            "CACHE_TYPE": "redis",
            "CACHE_REDIS_URL": os.environ.get("REDIS_URL", ""),
        },
    )
    cache_client.set("test", "123")
    return cache_client


app: Dash = Dash(__name__)
cache: Cache = get_cache_client(dash_app=app)
