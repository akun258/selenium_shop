import time

from selenium.webdriver.common.by import By

from auto_test_01.selenium_hub.page.base import base
from auto_test_01.selenium_hub.page.shopping import Shopping


class ShopIndex(base):
    _base_url = "https://www.saucedemo.com/"
    def login_in(self,usn,pwd):
        username = self.find(By.ID,"user-name")
        password = self.find(By.ID,"password")
        # 找到用户名
        username.click()
        # 输入用户名
        username.send_keys(usn)
        time.sleep(1)
        # 找到密码
        password.click()
        # 输入密码
        password.send_keys(pwd)
        # 点击登录
        time.sleep(1)
        self.find(By.ID,"login-button").click()
        time.sleep(2)
        login_result = self._driver.current_url
        # 判断当前是否正常登录
        if login_result != "https://www.saucedemo.com/inventory.html":
            # 提取错误信息
            error_text = self.find(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]").text
            # print(error_text,"223")
            assert "Epic sadface" in error_text
        else:
            # print(login_result,"shopping_cart_container")
            assert login_result == "https://www.saucedemo.com/inventory.html"
            return Shopping(self._driver)

