from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SearchPage:
    def __init__(self, driver):
        self.driver = driver

    # Locators
    search_box_name = "search"
    # search_button_xpath = "//button[@id='button-search']"
    search_button_xpath = "//i[@class='fa fa-search']"
    valid_product_link_text = "HP LP3065"
    no_product_found_xpath = '//input[@id="button-search"]/following-sibling::p'


    # Search with valid input
    def search_valid_input(self, text_data):
        # Wait for search box to be visible
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.NAME, self.search_box_name))
        ).clear()

        self.driver.find_element(By.NAME, self.search_box_name).send_keys(text_data)

        # Wait for search button to be clickable
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.search_button_xpath))
        ).click()

        # Wait for valid product link to appear
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.LINK_TEXT, self.valid_product_link_text))
        )

    # Search with invalid input
    def search_invalid_input(self, text_data):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.NAME, self.search_box_name))
        ).clear()
        self.driver.find_element(By.NAME, self.search_box_name).send_keys(text_data)

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.search_button_xpath))
        ).click()

        # Wait for no-result message to appear and return text
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.no_product_found_xpath))
        ).text

    # Search with empty input
    def search_none(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.NAME, self.search_box_name))
        ).clear()
        self.driver.find_element(By.NAME, self.search_box_name).send_keys("")

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.search_button_xpath))
        ).click()

        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.no_product_found_xpath))
        ).text

    def search_phone(self,text_data):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.NAME, self.search_box_name))
        ).clear()
        self.driver.find_element(By.NAME, self.search_box_name).send_keys(text_data)

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.search_button_xpath))
        ).click()

    def search_gibberish_text_xfail(self,text_data):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.NAME, self.search_box_name))
        ).clear()
        self.driver.find_element(By.NAME, self.search_box_name).send_keys(text_data)

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.search_button_xpath))
        ).click()

    def search_gibberish_text_xpass(self,text_data):

         WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.NAME, self.search_box_name))
         ).clear()
         self.driver.find_element(By.NAME, self.search_box_name).send_keys(text_data)

         WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.search_button_xpath))
         ).click()
