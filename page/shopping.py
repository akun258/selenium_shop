from selenium.webdriver.common.by import By

from auto_test_01.selenium_hub.page.base import base


class Shopping(base):
    def add_shop(self):
        # 点击添加购物车的商品
        first_div = self.WebDriverWait(By.ID,"add-to-cart-sauce-labs-backpack")
        first_div.click()
        # print(first_div,"first")
        pass