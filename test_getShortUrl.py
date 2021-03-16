import webbrowser

from unittest import TestCase
from GetShortUrl import GetShortUrl

    ## open the short URL by browser.

class TestGetShortUrl(TestCase):

    def test_get_short_url_post(self):
        r = GetShortUrl.get_short_url_post(self)

        if (r.status_code == 200):
            shortUrl = r.json().get("short_url")
            webbrowser.open(shortUrl, 1)
