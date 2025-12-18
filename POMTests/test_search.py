import pytest
from pages.SearchPage import SearchPage

@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.FullFunctional
class TestSearch:
    @pytest.mark.smoke
    def test_search_valid_input(self):
        search_page = SearchPage(self.driver)
        product = search_page.search_valid_input("HP")  # method returns WebElement
        assert product.is_displayed()
    @pytest.mark.smoke
    def test_invalid_input(self):
        search_page = SearchPage(self.driver)
        no_result_text = search_page.search_invalid_input("Honda")  # returns text
        assert "There is no product" in no_result_text

    def test_search_none(self):
        search_page = SearchPage(self.driver)
        no_result_text = search_page.search_none()  # returns text
        assert "There is no product" in no_result_text
    @pytest.mark.smoke
    def test_search_product(self):
        search_page = SearchPage(self.driver)
        search_page.search_phone("Phone")


