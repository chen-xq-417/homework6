import json

import allure
import yaml
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.remote.webdriver import WebDriver

from homework2.conftest import root_log


class BasePage:
    params = {}
    blacklist = []
    max_num = 3
    error_num = 0

    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find_click(self, by, locator):
        self.find(by, locator).click()

    def send(self, by, locator):
        self.find(by, locator).send_keys()

    def setup_implicitly_wait(self, timeout):
        self.driver.implicitly_wait(timeout)

    def find(self, by, locator=None):
        root_log.info(f'find: by={by}, locator = {locator}')
        # 捕获异常
        try:
            element = self.driver.find_element(by, locator)
            self.error_num = 0
            return element
        # 处理异常
        except Exception as e:
            root_log.error("未找到元素")
            # 处理黑名单逻辑
            self.driver.implicitly_wait(2)
            self.driver.get_screenshot_as_file("tmp.png")
            allure.attach.file("tmp.png", attachment_type=allure.attachment_type.PNG)
            # 设置最大查找次数,如果错误次数大于最大错误次数，则首先把错误次数置0，然后抛出异常
            if self.error_num > self.max_num:
                self.error_num = 0
                raise e
            # 每进入except一次，都执行+1操作
            self.error_num += 1
            # 处理黑名单,遍历黑名单，
            for ele in self.blacklist:
                # find_elements 会返回元素都列表[ele1，ele2。。。]，如果没有元素会返回一个空列表
                eles = self.driver.find_elements(*ele)
                # 如果eles列表都长度>0，说明有弹窗，则对弹窗进行点击，然后返回self.find，继续对要查找对元素进行查找
                if len(eles) > 0:
                    eles[0].click()
                    return self.find(by, locator)
            # 如果黑名单都处理完，仍然没有找到想要都元素，则抛出异常
            raise e

    def swip_click(self, text):
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().'
                                 'scrollable(true).instance(0)).'
                                 'scrollIntoView(new UiSelector().'
                                 f'text("{text}").instance(0));').click()

    def steps(self, path, fun_name):
        with open(path, encoding='utf-8') as f:
            function = yaml.safe_load(f)
            # 将yaml文件中的内容，读取到steps中
            steps: list[dict] = function[fun_name]

            # json 序列化与反序列化
            # json.dumps（）序列化  python对象转化成字符串
            # json.loads（）反序列化 python字符串转化为python对象
            raw = json.dumps(steps)
            for key, value in self.params.items():
                raw = raw.replace("${" + key + "}", value)
            steps = json.loads(raw)

            # step是steps中的字典
            for step in steps:
                if step['action'] == 'find_click':
                    self.find_click(step['by'], step['locator'])
                if step['action'] == 'find':
                    self.find(step['by'], step['locator'])
                elif step['action'] == 'swip_click':
                    self.swip_click(step['text'])
                elif step['action'] == 'find_sendkeys':
                    self.find(step['by'], step['locator']).send_keys(step['text'])
