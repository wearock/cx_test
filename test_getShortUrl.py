import pytest

from GetShortUrl import GetShortUrl
from selenium import webdriver
from configuration.constans import ShortUrlConstants

    ## open the short URL by browser.

class TestGetShortUrl:


    def test_get_short_url_post(self):
        """https://testrail.internetbrands.com/testrail//index.php?/cases/view/19317545"""

        short_url = GetShortUrl.get_short_url_post(self)

        driver = webdriver.Chrome()
        driver.get(short_url)
        assert driver.current_url == ShortUrlConstants.POST_GOOGLE_URL, 'www.google.com has not openned!'



