from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    def __init__(self, driver):
        self.driver = driver

    cart_icon = "//div[@class='button-group']/button[1]"

    def add_phone(self,phone_data):
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,self.cart_icon))).click()
        
