import json
from curl_cffi import requests

# url = "https://www.metrocuadrado.com"
url = "https://www.metrocuadrado.com/rest-search/search"

headers = {
    "accept": "application/json", 
    "accept-language": "es-MX,es;q=0.9",
    "x-api-key": "P1MfFHfQMOtL16Zpg36NcntJYCLFm8FqFfudnavl",
    # "referer": "https://metrocuadrado.com",
    "cookie": "utag_main_vapi_domain=metrocuadrado.com; _fbp=fb.1.1776706253642.384808455948833373; _ga=GA1.1.936515281.1776706254; _gcl_au=1.1.1831045114.1776706254; disclaimerCookies=true; _hjSessionUser_3298791=eyJpZCI6IjdjM2VkYWFhLTdlMGUtNWEwYi05ZDZhLWYxOTQyYTc1OTk1ZSIsImNyZWF0ZWQiOjE3NzY3MDYyNTI3NDEsImV4aXN0aW5nIjp0cnVlfQ==; split_segmentation=FAB; split_segmentation_50=less FAB_SUS_50; at_check=true; canary_param=false; utag_main__sn=8; utag_main_v_id=019dcf8f88200021e158601b5a4e0506f004806700876; utag_main_dc_visit=1; FCCDCF=%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B%5B32%2C%22%5B%5C%22ce784db5-9cb8-487d-9a79-89b038a6127b%5C%22%2C%5B1776706254%2C17000000%5D%5D%22%5D%5D%5D; mbox=PC#b9d73045021547b2aced0d323dbe93d5.34_0#1840549340|session#3f2494bb754044b8ac6cc0c9675a4857#1777306400; cto_bundle=aqjYe193cE1OOXVuRWFLUWFIbVZnNW50d2l1NSUyQlUxJTJCY1hKNmliZCUyRlBVOU5lTlZ6Vk9pNjVNME92JTJCUVglMkJ1ZUF6eCUyQlZXN25WZ0NWYjFUMVBqJTJCU3pWa21kTGJzOGElMkZVWXNHVFNKc08lMkIlMkZ1ZlBobks5MFFZUXFiTmVlSjMyRXlFcmYlMkZlTkRQM0tqSmVBaEtDJTJGT3RjbmVmclNzdkElM0QlM0Q; FCNEC=%5B%5B%22AKsRol9Cbmp3PyLi2IcTTUNhDTcguSlN1P5-3K2uGVKUgZNVkrTNiDfl6gOUCWILSvFl7cH6eSMuMR2OpgptqTR1F5HFSOuKCLccPB5BWxljdYLtAIf5v-FhaCGt_TL0XxwUddoa1ObyFKeglEAEJRbA6BeHZNcrgA%3D%3D%22%5D%5D; _ga_02LQXVPQF9=GS2.1.s1777303784$o8$g1$t1777304660$j60$l0$h0; AWSALB=d+w2zN/7fRLe7/YUnUnSAJ7YZRmcpNEUI0o1WwuzcSNNqQ2H+2IMvkXybw1xYGHbKiHvKQdU+PqIpvSVdvoSBxhVVHxC7N0t86i0GxutFX8mv/gLjVQk+N7QvwDBUZJHnaB1lzK8rUH3cOgGq6tzZG9f7oXlzVdzPhxarQrZSPzuN5S+owPqlKVd8e2Nmw==; __gads=ID=9fdb8737e3248851:T=1776706253:RT=1777313186:S=ALNI_Mbwnpv1q8iEnFoKetreEh8whveX5w; __gpi=UID=0000136205fa6a21:T=1776706253:RT=1777313186:S=ALNI_MaF7ql_CGj3uBiPW9PJUGdBs0mQ0Q; __eoi=ID=1d3bc6a1a9f9b617:T=1776706253:RT=1777313186:S=AA-AfjaXDx4_h-g2MHHl4_PrcKnY",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "Referer": "https://www.metrocuadrado.com/apartamento/arriendo/medellin/?search=form"
}

params = {
    "size": "50",
    "from": "0",  # Cambia esto de 50 en 50 para paginar
    "realEstateTypeList": "apartamento",
    "realEstateBusinessList": "arriendo",
    "city": "medellin"
}

response = requests.get(
    url, 
    headers=headers, 
    params=params,
    impersonate="chrome110"
    )

if response.status_code == 200:
    print(f"Status: {response.status_code}")
    print(f"Content-Type recibido: {response.headers.get('Content-Type')}")
    # print(f"Content: {response.content}")
else:
    print(f"Status: {response.status_code}")
    print(f"Respuesta error: {response.text}")