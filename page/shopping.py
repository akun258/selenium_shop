import time
from operator import contains

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from auto_test_01.selenium_hub.page.base import base
from auto_test_01.selenium_hub.page.shopping_cart import ShoppingCart


class Shopping(base):
    # 添加商品用例
    def add_shop(self,shop_add_num):
        # 判断用户想添加多少个商品，如果超过6个，最大值就是6
        if shop_add_num > 6:
            shop_add_num = 6
        # 获取当前加入购物车元素的所有数量
        # ele_lens = self.finds(By.CLASS_NAME,"inventory_item").__len__()
        # print(ele_lens,"len")
        # 循环遍历添加至购物车
        for i in range(shop_add_num):
            ele = self.find(By.CSS_SELECTOR,f'.inventory_list > .inventory_item:nth-child({i+1})')
            add_btn = self.WebDriverWait(By.XPATH,"//*[contains(@id,'add')]")
            add_btn.click()
        time.sleep(1)
        # 获取购物车中的数量
        num = self.find(By.XPATH, "//*[@id='shopping_cart_container']/a/span").text
        # 断言判断购物车的数量是否与我添加的数量一致
        assert int(shop_add_num) == int(num)
        return self

    # 移除添加商品用例
    def remove_shop(self,shop_del_num):
        # 判断用户想添加多少个商品，如果超过6个，最大值就是6
        if shop_del_num > 6:
            shop_del_num = 6
        # 循环遍历添加至购物车
        for i in range(shop_del_num):
            ele = self.find(By.CSS_SELECTOR, f'.inventory_list > .inventory_item:nth-child({i + 1})')
            del_btn = self.WebDriverWait(By.XPATH,"//*[contains(@id,'remove')]")
            del_btn.click()
        time.sleep(1)
        shopCar_num = self.finds(By.XPATH, "//*[@id='shopping_cart_container']/a/span")
        # 验证当前获取元素的数组是否为空
        # print(shopCar_num.__len__(),"1213")
        assert shopCar_num.__len__() == 0
        return self

    # 查看商品详情用例
    def view_details(self):
        # 获取商品详情定位
        title_link = self.find(By.ID,'item_4_title_link')
        title_link.click()
        time.sleep(2)
        assert contains(self._driver.current_url,"https://www.saucedemo.com/inventory-item.html")
        # 找到回退按钮
        back_btn = self.find(By.ID,'back-to-products')
        back_btn.click()
        time.sleep(2)
        assert self._driver.current_url == "https://www.saucedemo.com/inventory.html"
        return self

    # 商品排序
    def shop_sort(self):
       try:
           old_list = []
           new_list = []
           # 获取商品总数
           shop_total = self.finds(By.CLASS_NAME, "inventory_item_name ").__len__()
           # 将原始列表的标题全部存储
           for i in range(shop_total):
               old_list_title = self.find(By.ID, f'item_{i}_title_link').text
               old_list.append(old_list_title)
           # print(old_list, "oldlist")
           # 点击筛选框
           select_sort = Select(self.find(By.CLASS_NAME, "product_sort_container"))
           select_sort.select_by_value("lohi")
           # 重新获取商品名称，验证排序是否更改
           for i in range(shop_total):
               new_list_title = self.find(By.ID, f'item_{i}_title_link').text
               new_list.append(new_list_title)
           select_sort_text = self.find(By.CLASS_NAME, "active_option").text
           assert select_sort_text == "Price (low to high)"
           return ShoppingCart(self._driver)
       except Exception as e:
           print(e,"e")




