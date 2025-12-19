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

    @pytest.mark.xfail
    def test_gibberish1(self):
        search_page = SearchPage(self.driver)
        search_page.search_gibberish_text_xfail("qwertyuiop")
        # assert self.gibberish_assertion == "https://tutorialsninja.com/demo/index.php?route=product/search&search=qwerty"
        current_url = self.driver.current_url
        assert "ASDFGHJKL" in current_url

    @pytest.mark.xfail
    def test_gibberish2(self):
        search_page = SearchPage(self.driver)
        search_page.search_gibberish_text_xpass("qwertyuiop")
        # assert self.gibberish_assertion == "https://tutorialsninja.com/demo/index.php?route=product/search&search=qwertyuiop"
        current_url = self.driver.current_url
        assert "qwertyuiop" in current_url
