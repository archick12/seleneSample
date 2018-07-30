from selene import config
from selene.browser import open_url
from selene.browsers import BrowserName
from selene.support.conditions import be, have
from selene.support.jquery_style_selectors import s, ss
config.browser_name = BrowserName.CHROME

class GooglePage(object):

    def open(self):
        open_url("http://google.com/ncr")
        return self

    def search(self, text):
        s("[name='q']").set(text).press_enter()
        return SearchResultsPage()

class SearchResultsPage(object):

    def __init__(self):
        self.results = ss(".srg .g")

def test_google_search():
    google = GooglePage().open()
    search = google.search("selene")
    search.results[0].should(have.text("In Greek mythology, Selene is the goddess of the moon"))  # :D
