from support.base_test_case import BaseTestCase
from support.pages.home_page import HomePage
from support.pages.page import Page
import time

BaseTestCase.main(__name__, __file__)


class TestSimpleLogin(BaseTestCase):
    def test_simple_login(self):
        self.open("https://twitch.tv")

        # Accept cookies
        self.click(Page.accept_cookies_button)

        self.click(HomePage.search_button)
        self.type(HomePage.search_input, "Starcraft II")

        self.click(Page.get_locator_by_title(topic="StarCraft II"))
        self.assert_text_visible("Follow")

        # Below this is still not working; need to fix
        self.scroll_to_bottom()
        self.scroll_to_bottom()

        streamer_elements = self.find_visible_elements("article")
        streamer_elements[2].click()
        # In case an alert is shown, dismiss it
        # Does not work for modals
        # self.dismiss_alert()

        # In case a modal pops up, close it
        # The locator is not correct most likely
        # Assuming that the close button has the same kind of locator
        # self.click("button[data-a-target='modal-close-button']")

        streamer_url = str(time.time())
        self.assert_element_visible("[data-a-target='follow-button']")
        self.save_screenshot(name=streamer_url, folder="./screenshots")
