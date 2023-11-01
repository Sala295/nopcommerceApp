from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    else:
        raise ValueError("Invalid browser name provided")

    driver.maximize_window()
    yield driver  # The test will run at this point
    driver.quit()  # Close the browser after the test

# Define the custom command-line option --browser
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Specify the browser to use (e.g., chrome)")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")
