import time
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver

class base():
    _driver = None
    _base_url = ""
    def __init__(self,driver:WebDriver = None):
        if driver is None:
            self._driver = webdriver.Chrome(service=Service(executable_path="D:/tools/chrome/chromedriver.exe"))
            self._driver.maximize_window()
            self._driver.implicitly_wait(5)
        else:
            self._driver = driver

        if self._base_url != "":
            self._driver.get(self._base_url)


    # 封装查询元素方法
    def find(self,by,locator):
        return self._driver.find_element(by,locator)

    def finds(self,by,locator):
        return self._driver.find_elements(by,locator)

    # 显示等待
    def WebDriverWait(self,by,locator):
        return WebDriverWait(self._driver,10).until(EC.presence_of_element_located((by,locator)))

