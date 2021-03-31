from homework2.page.base_page import BasePage
from homework2.page.information_page import InformationPage


class SearchPage(BasePage):
    def goto_search2(self):
        self.steps("../page/search_page.yaml", "goto_search")
        self.steps("../page/search_page.yaml", "goto_click")
        return InformationPage(self.driver)
