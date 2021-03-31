from homework2.page.base_page import BasePage


class EditPage(BasePage):
    def goto_delect(self):
        self.steps("../page/edit_page.yaml", "goto_delect")
        self.steps("../page/edit_page.yaml", "goto_sure_delect")
        return True
