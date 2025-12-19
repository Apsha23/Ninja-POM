import pytest
from pages.LoginPage import HomePage

@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.FullFunctional
class TestLogin:
    @pytest.mark.smoke
    def test_valid_credentials(self):
       home_page = HomePage(self.driver)
       home_page.login_page_valid_credentials("apshashaik050@gmail.com","12345")

    @pytest.mark.smoke
    def test_invalid_credentials(self):
        home_page = HomePage(self.driver)
        home_page.login_page_invalid_credentials("apshashaik050@gmail.com", "1234567890")

    def test_valid_email(self):
        home_page = HomePage(self.driver)
        home_page.login_page_valid_email_invalid_password("apshashaik050@gmail.com","1234567890")

    def test_valid_password(self):
        home_page = HomePage(self.driver)
        home_page.login_page_invalid_email_valid_password("apshashaik@gmail.com","12345")

    @pytest.mark.skip(reason = 'not implemented yet')
    def test_login_international(self):
        home_page = HomePage(self.driver)
        home_page.login_page_international_email_password("","")

    @pytest.mark.skip(reason='not implemented yet')
    def test_login_special_characters(self):
        home_page = HomePage(self.driver)
        home_page.login_page_with_special_characters("", "")
