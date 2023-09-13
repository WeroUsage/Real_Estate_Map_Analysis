import re

URLS = ['https://www.myhome.ge/en/s/?AdTypeID=1&PrTypeID=1&Page=1&Ajax=1',
        'https://www.myhome.ge/en/s/?AdTypeID=1&PrTypeID=2&Page=1&Ajax=1',
        'https://www.myhome.ge/en/s/?AdTypeID=1&PrTypeID=4&Page=1&Ajax=1',
        'https://www.myhome.ge/en/s/?AdTypeID=1&PrTypeID=5&Page=1&Ajax=1',
        'https://www.myhome.ge/en/s/?AdTypeID=1&PrTypeID=7&Page=1&Ajax=1',
        
        'https://www.myhome.ge/en/s/?AdTypeID=2&PrTypeID=1&Page=1&Ajax=1',
        'https://www.myhome.ge/en/s/?AdTypeID=2&PrTypeID=2&Page=1&Ajax=1',
        'https://www.myhome.ge/en/s/?AdTypeID=2&PrTypeID=4&Page=1&Ajax=1',
        'https://www.myhome.ge/en/s/?AdTypeID=2&PrTypeID=5&Page=1&Ajax=1',
        'https://www.myhome.ge/en/s/?AdTypeID=2&PrTypeID=7&Page=1&Ajax=1',

        'https://www.myhome.ge/en/s/?AdTypeID=3&PrTypeID=1&Page=1&Ajax=1',
        'https://www.myhome.ge/en/s/?AdTypeID=3&PrTypeID=2&Page=1&Ajax=1',
        'https://www.myhome.ge/en/s/?AdTypeID=3&PrTypeID=4&Page=1&Ajax=1',
        'https://www.myhome.ge/en/s/?AdTypeID=3&PrTypeID=7&Page=1&Ajax=1',
        
        'https://www.myhome.ge/en/s/?AdTypeID=7&PrTypeID=1&Page=1&Ajax=1',
        'https://www.myhome.ge/en/s/?AdTypeID=7&PrTypeID=2&Page=1&Ajax=1',
        'https://www.myhome.ge/en/s/?AdTypeID=7&PrTypeID=4&Page=1&Ajax=1',
        'https://www.myhome.ge/en/s/?AdTypeID=7&PrTypeID=7&Page=1&Ajax=1',
        
        'https://www.myhome.ge/en/s/?AdTypeID=8&PrTypeID=5&Page=1&Ajax=1'
        ]

def get_categories(url):
    transaction_type_from_AdTypeID = {'1':'for sale','2':'leasehold mortgage',
                                      '3':'for rent','7':'for daily rent', '8':'gaicema ijarit'}
    real_estate_type_from_PrTypeID = {'1':'apartaments', '2':'housing and cottages',
                                      '4':'commercial real estate', '5':'lands', '7':'hotels'}

    AdTypeID = re.search(r'AdTypeID\=(\d)', url).group(1)
    PrTypeID = re.search(r'PrTypeID\=(\d)', url).group(1)

    transaction_type = transaction_type_from_AdTypeID.get(AdTypeID)
    real_estate_type = real_estate_type_from_PrTypeID.get(PrTypeID)

    return transaction_type, real_estate_type


def get_next_url(url):
    current_page = re.search(r'Page\=(\d+)', url).group(1)
    next_page = int(current_page) + 1
    next_url = re.sub(r'Page\=(\d+)', f'Page={next_page}', url)
    return next_url