import time
import pytest
from pageObjects.LoginPage import LoginPage
from pageObjects.AddcustomerPage import AddCustomer
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_SearchCustomerByEmail_004:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_searchCustomerByEmail(self,setup):
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("********Login Successfull********")

        self.logger.info("********Starting search customer by email********")

        self.addcust=AddCustomer(self.driver)
        self.addcust.clickOnCustomerMenu()
        self.addcust.clickOnCustomerMenuItem()

        self.logger.info("******** searching customer by email********")
        self.searchcust=SearchCustomer(self.driver)
        self.searchcust.setEmail("victoria_victoria@nopCommerce.com")
        self.searchcust.clickSearch()
        time.sleep(3)
        status=self.searchcust.searchCustomerByEmail("victoria_victoria@nopCommerce.com")
        assert True==status
        self.logger.info("**************TC_SearchCustomerByEmail_004 Finished **********")
        self.driver.close()

