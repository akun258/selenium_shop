import time

import allure
from selenium.webdriver.common.by import By

from auto_test_01.selenium_hub.page.base import base

@allure.feature("消费成功模块")
class FinshPage(base):
    @allure.story("返回选购界面")
    def finsh_click(self):
        time.sleep(1)
        back_home_btn = self.find(By.ID,"back-to-products")
        back_home_btn.click()
        time.sleep(1)
        title_text = self.find(By.XPATH, "//*[@id='header_container']/div[2]/span").text
        assert "Products" in title_text
