import pytest
from pages.AddToCart import CartPage


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.FullFunctional
class TestCart:
    def test_cart_phone(self):
        cart_page = CartPage(self.driver)
        cart_page.add_phone("Phone")

    @pytest.mark.smoke
    def test_click_cart_icon_in_login_page(self):
        cart_page = CartPage(self.driver)
        cart_page.click_cart_icon()


