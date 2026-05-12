from src.core.models import Models
from src.engine.api_client import FetchData
from src.sites.fincaraiz import SpiderFR
import config

def main():
    client = FetchData()
    scraper_fr = SpiderFR(config.CURL_FR, config. MAX_ITERATION)
    models = Models()

    scraper_fr.find_content(client, models)