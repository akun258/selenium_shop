import time

from selenium.webdriver.common.by import By

from auto_test_01.selenium_hub.page.base import base


class Shopping(base):
    def add_shop(self,shop_num):
        # 判断用户想添加多少个商品，如果超过6个，最大值就是6
        if shop_num > 6:
            shop_num = 6
        # 获取当前加入购物车元素的所有数量
        # ele_lens = self.finds(By.CLASS_NAME,"inventory_item").__len__()
        # print(ele_lens,"len")
        # 循环遍历添加至购物车
        for i in range(shop_num):
            ele = self.find(By.CSS_SELECTOR,f'.inventory_list > .inventory_item:nth-child({i+1})')
            add_btn = self.WebDriverWait(By.XPATH,"//*[@class='btn btn_primary btn_small btn_inventory ']")
            add_btn.click()
        time.sleep(1)
        # 获取购物车中的数量
        num = self.find(By.XPATH, "//*[@id='shopping_cart_container']/a/span").text
        # 断言判断购物车的数量是否与我添加的数量一致
        assert int(shop_num) == int(num)




    # def remove_shop(self):
