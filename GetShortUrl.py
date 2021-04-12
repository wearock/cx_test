import requests

from configuration.constans import ShortUrlConstants

class GetShortUrl():

    ## Get the shortUrl

    @staticmethod
    def get_short_url_post(self):
        """ Returns short_url
        """
        response = requests.post(url=ShortUrlConstants.POST_SHORT_URL,
                                 data=ShortUrlConstants.POST_SHORT_URL_BODY,
                                 headers=ShortUrlConstants.POST_SHORT_URL_HEADERS, verify=False)

        assert response.status_code == 200, 'r.status_code is not 200'

        short_url = response.json().get("short_url")

        return short_url




