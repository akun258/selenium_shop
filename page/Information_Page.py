import time

import allure
from selenium.webdriver.common.by import By

from auto_test_01.selenium_hub.page.Overview_Page import OverView
from auto_test_01.selenium_hub.page.base import base




@allure.feature("填写邮寄地址模块")
class InformationPage(base):
    @allure.story("创建邮寄地址")
    def create_Information(self):
        try:
            first_name = self.find(By.ID, "first-name")
            last_name = self.find(By.ID, "last-name")
            postal_code = self.find(By.ID, "postal-code")
            first_name.send_keys("邢")
            last_name.send_keys("杰坤")
            postal_code.send_keys("050000")
            time.sleep(2)
            con_btn = self.find(By.ID, "continue").click()
            time.sleep(2)
            title_text = self.find(By.XPATH, "//*[@id='header_container']/div[2]/span").text
            # 判断当前是否在支付详情界面
            if "Overview" in title_text:
                print("进入over")
                assert "Overview" in title_text
                return OverView(self._driver)
            elif "Information" in title_text:
                assert "Error" in self.find(By.XPATH,"//*[@id='checkout_info_container']/div/form/div[1]/div[4]/h3").text
                print("没有进入")
        except Exception as e:
            print(f"发生了一个错误：{e}")
