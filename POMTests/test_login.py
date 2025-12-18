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


