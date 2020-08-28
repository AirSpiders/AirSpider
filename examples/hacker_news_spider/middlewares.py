#!/usr/bin/env python

from airspider import Middleware, Request

middleware = Middleware()


@middleware.request
async def print_on_request(spider_ins, request: Request):
    ua = "airspider user-agent"
    request.headers.update({"User-Agent": ua})
    request.aiohttp_kwargs.update({"proxy": "http://0.0.0.0:8118"})
