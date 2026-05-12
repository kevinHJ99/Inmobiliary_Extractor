from src.core.models import Models
from curl_cffi import request

import asyncio
import time 
import random

class SpiderFR:
    def __init__(self, curl, max_iterations):
        self.curl = curl
        self.max_iterations = max_iterations

    def payload(self, page):
        payload = {
                    "variables": {
                "rows": 21,
                "params": {
                    "page": 4,
                    "order": 2,
                    "bedroomsExactMode": False,
                    "bathroomsExactMode": False,
                    "operation_type_id": 2,
                    "property_type_id": [2],
                    "locations": [{
                        "name": "Medellín",
                        "id": "183f0a11-9452-4160-9089-1b0e7ed45863",
                        "type": "CITY",
                        "slug": ["city-colombia-05-001"],
                        "estate": {
                            "name": "Antioquia",
                            "id": "2d63ee80-421b-488f-992a-0e07a3264c3e",
                            "slug": "state-colombia-05-antioquia"
                        }
                    }],
                    "currencyID": 4,
                    "m2Currency": 4
                },
                "page": page,
                "source": 10
            },
            "query": ""
        }

        return payload        

    async def find_content(self, client, models: Models):
        headers = {
            "accept": "*/*",
            "accept-language": "es-MX,es;q=0.9,en-GB;q=0.8,en;q=0.7,es-419;q=0.6",
            "content-type": "application/json",
            "x-origin": "www.fincaraiz.com.co",
            "referer": "https://www.fincaraiz.com.co/arriendo/apartamentos/medellin/antioquia/pagina4",
            "sec-ch-ua": '"Google Chrome";v="147", "Not.A/Brand";v="8", "Chromium";v="147"',
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site"
        }
        try:
            for i in range(1, self.max_iterations+1):
                response = await client.post_rq(self.curl, self.payload(i), headers)
                if response.status_code == 200:
                    # Process the successful response
                    models.parse_fincaraiz(response.json())
                else:
                    # Handle the error response
                    print(f"Error: Received status code {response.status_code} for page {i}")  
        except Exception as e:
            print(f"An error occurred: {e}")