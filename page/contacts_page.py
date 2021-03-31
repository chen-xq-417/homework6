from homework2.page.base_page import BasePage
from homework2.page.search_page import SearchPage


class ContactsPage(BasePage):
    def goto_search1(self):
        self.steps('../page/contacats_page.yaml', 'goto_search')
        return SearchPage(self.driver)
