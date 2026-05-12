import json
from curl_cffi import requests

url = "https://api-backend.ciencuadras.com/prod/search-results/v1"

headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "es-MX,es;q=0.9,en-GB;q=0.8,en;q=0.7,es-419;q=0.6",
    "authorization": "Bearer eyJraWQiOiJSNDBGb0R1OFRKYVJjYUgzRlhQMzBhZXlvb09LSWgxS2tWUUxHMkZSQlJNPSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiIzcGJhNGk2ZjMzOGJndXZlOXF2c2g3amRxdSIsInRva2VuX3VzZSI6ImFjY2VzcyIsInNjb3BlIjoiY2llbmN1YWRyYXMtcHJvZC1hcGktc2VydmVyXC9yZWFkIiwiYXV0aF90aW1lIjoxNzc3Mzg4MTcyLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAudXMtZWFzdC0xLmFtYXpvbmF3cy5jb21cL3VzLWVhc3QtMV9WMlhkQWJibW4iLCJleHAiOjE3NzczOTE3NzIsImlhdCI6MTc3NzM4ODE3MiwidmVyc2lvbiI6MiwianRpIjoiNTM5MTJkZmUtZWU2MC00NWM1LTlhOTctODdlNjllNDZlMDZmIiwiY2xpZW50X2lkIjoiM3BiYTRpNmYzMzhiZ3V2ZTlxdnNoN2pkcXUifQ.Pe6fC_3yb_caLKnf1fraiOuIp-8c0Jm_DoaFgTywkv66j2mVRqjF2k9PFkn0kmjciallgexmzdiK6Hp_HTO-JbUvg_v4xNs-zr18CsyIpE7DK6-riICo8vrt5fEwNJXRTOVw4qEGRdJFaafrasMtxRsfMRobYpZ_3y8OMY97AfjQSRaQh4VEGXV9j6FaO3Vp2fqlUGPyHKvkp6pQ0b8kp1Xnpr4aiwFPctePa0Wiv0mh34E5LltinXvKW-kr89iN8nopxkn-0k1C2u5wUM-C-twtz7GRX301IC3jjT03ahGcLSVoOJQeadnNSQzDk7JgQ03AJLCkZImH8E-FcDXAlw",
    "cache-control": "no-cache",
    "content-type": "application/json",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "sec-ch-ua": "\"Google Chrome\";v=\"147\", \"Not.A/Brand\";v=\"8\", \"Chromium\";v=\"147\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "x-ciencuadras-scope": "private",
    "Referer": "https://www.ciencuadras.com/"
}

data = {
     "radio": "2km",
    "size": 10,
    "sizeMap": 70,
    "transactionType": "arriendo",
    "typeDevice": "mobile",
    "fromNear": 0,
    "from": 0, 
    "sizeNear": 20,
    "project": False,
    "offer": 0,
    "requestId": "80e0c37d-a12c-829d-9630-4bc635636dd6",
    "department": "antioquia",
    "city": "medellín",
    "sortOrder": "desc",
    "colombiansAbroad": False,
    "expandSearch": False,
    "realEstateType": ["apartamento"],
    "hasDevolution": False
}

# Usamos data=json.dumps() para asegurar el formato más estricto
response = requests.post(
    url, 
    headers=headers, 
    json=data,
    impersonate="chrome110"
    )

if response.status_code == 200:
    print(f"Status: {response.status_code}")
    print(f"Content-Type recibido: {response.headers.get('Content-Type')}")
    # print(f"Content: {response.content}")
else:
    print(f"Status: {response.status_code}")
    print(f"Respuesta error: {response.text}")