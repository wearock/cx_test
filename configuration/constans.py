class ShortUrlConstants:
    def __init__(self):
        pass

    POST_SHORT_URL = 'https://stg.ib4.me'
    POST_SHORT_URL_HEADERS = {'content-type': "application/json",
                                  'Authorization': 'Bearer ' + '8900D215-88A9-DBC9-8C50-290A89UU53C6'}
    POST_SHORT_URL_BODY = '{ \"original_url\":\"https://www.google.com\" }'
    POST_GOOGLE_URL = 'https://www.google.com/'