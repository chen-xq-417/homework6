from homework2.page.app import App


class TestDelect:
    def test_delect(self):
        name = 'aaa16'
        App().start().goto_contacts().goto_search1().goto_search2(name).goto_click1().goto_edit().goto_delect()
