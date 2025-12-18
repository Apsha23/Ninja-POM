import pytest
from pages.AddToCart import CartPage


@pytest.mark.usefixtures("setup_teardown")
class TestCart:
    def test_cart_phone(self):
        cart_page = CartPage(self.driver)
        cart_page.add_phone("Phone")

