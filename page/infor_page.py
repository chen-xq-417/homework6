from homework2.page.base_page import BasePage
from homework2.page.edit_page import EditPage


class InforPage(BasePage):
    def goto_edit(self):
        self.steps("../page/infor_page.yaml", "goto_edit")
        return EditPage(self.driver)
