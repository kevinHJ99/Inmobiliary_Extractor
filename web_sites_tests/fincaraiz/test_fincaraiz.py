import json
from curl_cffi import requests

url = "https://search-service.fincaraiz.com.co/api/v1/properties/search"

# Headers extraídos de tu fetch
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
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36"
}

# Payload exacto como string para evitar errores de serialización
payload_raw = {
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
        "page": 1,
        "source": 10
    },
    "query": ""
}

# Usamos data=json.dumps() para asegurar el formato más estricto
response = requests.post(
    url, 
    headers=headers, 
    json=payload_raw, 
    impersonate="chrome110"
    )
if response.status_code == 200:
    print(f"Status: {response.status_code}")
    print(f"Content-Type recibido: {response.headers.get('Content-Type')}")
    print(f"Content: {response.json().get('hits', {}).get('hits', [])[0].get('_source', {})}")
else:
    print(f"Status: {response.status_code}")
    print(f"Respuesta error: {response.text}")