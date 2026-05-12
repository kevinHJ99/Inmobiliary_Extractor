class Models:
    def __init__(self):
        self.data = {}

    def parse_fincaraiz(self, data_json):
        hits = data_json.get('hits', {}).get('hits', [])
        for hit, i in zip(hits, range(0, len(hits))):
            source = hit[i].get('_source', {})
            self.data[i] = {
                "id": source.get('id'),
                "title": source.get('title'),
                "description": source.get('description'),
                "price": source.get('price'),
                "currency": source.get('currency'),
                "location": source.get('location', {}).get('name'),
                "bedrooms": source.get('bedrooms'),
                "bathrooms": source.get('bathrooms'),
                "area_m2": source.get('area_m2')
            }


    def parse_ciencuadras(self, data_json):
        pass

    def parse_metrocuadrado(self, data_json):
        pass