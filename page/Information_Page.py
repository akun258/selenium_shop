import time

from selenium.webdriver.common.by import By

from auto_test_01.selenium_hub.page.Finshed_page import FinshedPage
from auto_test_01.selenium_hub.page.base import base


class InformationPage(base):
    def create_Information(self):
        try:
            first_name = self.find(By.ID, "first-name")
            last_name = self.find(By.ID, "last-name")
            postal_code = self.find(By.ID, "postal-code")
            first_name.send_keys("邢")
            last_name.send_keys("杰坤")
            postal_code.send_keys("050000")
            con_btn = self.find(By.ID, "continue").click()
            time.sleep(2)
            title_text = self.find(By.XPATH, "//*[@id='header_container']/div[2]/span").text
            if title_text == "Overview":
                assert "Overview" in title_text
                return FinshedPage(self._driver)
            elif "Information" in title_text:
                assert "Error" in self.find(By.XPATH,"//*[@id='checkout_info_container']/div/form/div[1]/div[4]/h3").text
        except Exception as e:
            print(f"发生了一个错误：{e}")
