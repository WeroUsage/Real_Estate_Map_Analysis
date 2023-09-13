import scrapy
import json
from ..utils import URLS, get_next_url, get_categories

class SpidaddySpider(scrapy.Spider):
    name = "spidaddy"
    allowed_domains = ["www.myhome.ge"]
    start_urls = URLS

    def parse(self, response):
        page_exists = ('The page is not found' not in response.text)
        if page_exists:
            json_resp = json.loads(response.text)
            transaction_type, real_estate_type = get_categories(response.url)
            items1 = json_resp.get('Data').get('MapData').get('Points')
            items2 = json_resp.get('Data').get('Prs')

            for item1, item2 in zip(items1, items2):
                product_id1 = item1.get('product_id')
                product_id2 = item2.get('product_id')
                if product_id1 == product_id2:

                    yield {
                        'product_id':product_id1,
                        'transaction_type':transaction_type,
                        'real_estate_type':real_estate_type,

                        'content_url':item1.get('href'),
                        'price':item1.get('price').get('amount'),
                        'currency_id':item1.get('price').get('currency'),

                        'area_size':item2.get('area_size'),
                        'latitude':item2.get('map_lat'),
                        'longitude':item2.get('map_lon'),
                        'address':eval(item2.get('pathway_json')).get('en'),
                    }
                else:
                    yield {'url':response.url}
                
            
            next_url = get_next_url(response.url)
            yield response.follow(next_url, callback=self.parse)
    
