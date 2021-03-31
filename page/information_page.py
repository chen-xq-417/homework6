from homework2.page.base_page import BasePage
from homework2.page.infor_page import InforPage


class InformationPage(BasePage):
    def goto_click1(self):
        self.steps("../page/information_page.yaml", "goto_click1")
        return InforPage(self.driver)
