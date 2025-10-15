import time

from selenium.webdriver.common.by import By

from auto_test_01.selenium_hub.page.Information_Page import InformationPage
from auto_test_01.selenium_hub.page.base import base


class ShoppingCart(base):
    # 进入购物车列表
    def shopping_cart_list(self):
        self.find(By.ID,"shopping_cart_container").click()
        time.sleep(2)
        assert self._driver.current_url == "https://www.saucedemo.com/cart.html"
        return self
    # 回到选购商品页面
    def back_shopping(self):
        self.find(By.ID,"continue-shopping").click()
        time.sleep(2)
        assert self._driver.current_url == "https://www.saucedemo.com/inventory.html"
        return self

    #去结算
    def check_out(self):
        try:
            self.find(By.ID, "checkout").click()
            info_text = self.find(By.XPATH, "//*[@id='header_container']/div[2]/span").text
            time.sleep(2)
            assert "Information" in info_text
            return InformationPage(self._driver)
        except Exception as e:
            print(f"发生了一个错误：{e}")





