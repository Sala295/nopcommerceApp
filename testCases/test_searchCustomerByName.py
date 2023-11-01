import time
import pytest
from pageObjects.LoginPage import LoginPage
from pageObjects.AddcustomerPage import AddCustomer
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_SearchCustomerByName_005:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_searchCustomerByName(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("********Login Successful********")

        self.logger.info("********Starting search customer by name********")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomerMenu()
        self.addcust.clickOnCustomerMenuItem()

        self.logger.info("******** searching customer by name********")
        self.searchcust = SearchCustomer(self.driver)
        self.searchcust.setFirstName("Victoria")
        self.searchcust.setLastName("Terces")  # Fixed the typo here
        self.searchcust.clickSearch()
        time.sleep(3)
        status = self.searchcust.searchCustomerByName("Victoria Terces")
        assert True == status
        self.logger.info("**************TC_SearchCustomerByName_005 Finished **********")
        self.driver.close()
