import requests

class GetShortUrl():

    ## Get the shortUrl

    @staticmethod
    def get_short_url_post(self):

        url = "https://stg.ib4.me"

        bearer_token = "Bearer 8900D215-88A9-DBC9-8C50-290A89UU53C6"
        headers = {
            "Authorization": bearer_token,
            "Content-Type": "application/json"
        }

        data = "{ \"original_url\":\"https://www.google.com\" }"

        r = requests.post(url=url, data=data, headers=headers, verify=False)

        return r




