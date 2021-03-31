from appium import webdriver

from homework2.page.base_page import BasePage
from homework2.page.contacts_page import ContactsPage


class App(BasePage):
    package = 'com.tencent.wework'
    activity = 'com.tencent.wework.launch.WwMainActivity'

    def start(self):

        if self.driver is None:
            desired_caps = {}
            desired_caps['platformName'] = 'Android'
            desired_caps['platformVersion'] = '6.0'
            desired_caps['deviceName'] = 'emulator-5554'
            desired_caps['appPackage'] = self.package
            desired_caps['appActivity'] = self.activity
            desired_caps['noReset'] = True
            self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
            self.driver.implicitly_wait(3)
        else:
            self.driver.start_activity(self.package, self.activity)

        return self

    def goto_contacts(self):
        self.steps("../page/app.yaml", "goto_contacts")
        return ContactsPage(self.driver)
