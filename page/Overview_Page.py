import time

import allure
from selenium.webdriver.common.by import By

from auto_test_01.selenium_hub.page.Finshed_page import FinshPage
from auto_test_01.selenium_hub.page.base import base

@allure.feature("最终确认模块")
class OverView(base):
    @allure.story("去结算")
    def go_to_finshed(self):
        time.sleep(1)
        finsh_btn = self.find(By.ID, "finish")
        finsh_btn.click()
        time.sleep(1)
        title_text = self.find(By.XPATH, "//*[@id='header_container']/div[2]/span").text
        assert "Complete" in title_text
        return FinshPage(self._driver)
