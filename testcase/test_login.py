from ..page.login_in import ShopIndex

class TestLogin():
    def setup(self):
        self.main = ShopIndex()
    def test_login(self):
        # secret_sauce
        self.main.login_in("standard_user","secret_sauce").add_shop(2).view_details().shop_sort().shopping_cart_list().check_out().create_Information()
