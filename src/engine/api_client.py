from curl_cffi import request as rq

import asyncio
import random

class FetchData:
    def __init__(self):
        self.session = rq.Session(impersonate="chrome110")

    async def get_rq(self, url, payload, headers):
        try:
            response = await self.session.get(
                url,
                headers=headers,
                params=payload,
                timeout=random.randint(10, 15)
            )

            if await response.status_code != 200:
                return response.status_code
            else:
                return response
            
        except Exception as e:
            raise Exception(e)

    async def post_rq(self, url, payload, headers):
        try:
            response = await self.session.post(
                url,
                headers=headers,
                params=payload,
                timeout=random.randint(10, 15)
            )

            if await response.status_code != 200:
                return response.status_code
            else:
                return response
            
        except Exception as e:
            raise Exception(e)