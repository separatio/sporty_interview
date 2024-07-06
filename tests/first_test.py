from seleniumbase import BaseCase
BaseCase.main(__name__, __file__)

class TestSimpleLogin(BaseCase):
    def test_simple_login(self):
        self.open("https://twitch.tv")
        # self.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        # Accept cookies
        self.wait_for_element("button[data-a-target='consent-banner-accept']")
        self.click("button[data-a-target='consent-banner-accept']")

        self.click("[aria-label='Search']")

        search_input_locator = "[placeholder='Search...']"
        self.wait_for_element(search_input_locator)
        self.type(search_input_locator, "Starcraft II")

        self.click("[title='StarCraft II']")
        self.wait_for_element("//h1[text()='StarCraft II']")

        self.scroll_to_bottom()

        # self.wait_for_element_clickable("//*[@role='list']/div[2]")
        self.js_click("//*[@role='list']/div[0]")
        # self.click("h1")
