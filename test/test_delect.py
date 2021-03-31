from homework2.page.app import App


class TestDelect:
    def test_delect(self):
        name = 'aaa16'
        App().start().goto_contacts().goto_search1(name).goto_search2().goto_click1().goto_edit().goto_delect()
