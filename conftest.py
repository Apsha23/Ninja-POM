import pytest
from selenium import webdriver
from utilities import PullConfigurations


@pytest.fixture()
def setup_teardown(request):
    # driver = None
    browserobject = PullConfigurations.read_configurations("basic", "browser")

    if browserobject == "chrome":
        driver = webdriver.Chrome()
    elif browserobject == "edge":
        driver = webdriver.Edge()
    elif browserobject == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError("Provide a valid browser name")

    driver.maximize_window()

    url = PullConfigurations.read_configurations("basic", "website")
    driver.get(url)

    request.cls.driver = driver
    yield

    driver.quit()
