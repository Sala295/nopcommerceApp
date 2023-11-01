from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

class SearchCustomer:
    #Add customer page
    txtEmail_id="//input[@name='SearchEmail']"
    txtFirstName_id="//input[@name='SearchFirstName']"
    txtLastName_id="//input[@name='SearchLastName']"
    btnSearch_id="//button[@id='search-customers']"

    table_xpath="//div[@id='customers-grid_wrapper']"
    tableRows_xpath="//table[@id='customers-grid']//tr"
    tableColumns_xpath="//table[@id='customers-grid']//tr/td"

    def __init__(self,driver):
        self.driver=driver

    def setEmail(self,email):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.txtEmail_id))).clear()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.txtEmail_id))).send_keys(email)

    def setFirstName(self,fname):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.txtFirstName_id))).clear()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.txtFirstName_id))).send_keys(fname)

    def setLastName(self,lname):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.txtLastName_id))).clear()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.txtLastName_id))).send_keys(lname)

    def clickSearch(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.btnSearch_id))).click()

    def getNoOfRows(self):
        return len(WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, self.tableRows_xpath))))

    def getNoOfColumns(self):
        return len(WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, self.tableColumns_xpath))))

    def searchCustomerByEmail(self,email):
        flag=False
        for r in range(1,self.getNoOfRows()+1):
            table= WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.table_xpath)))
            emailid=table.find_element(By.XPATH,"//table[@id='customers-grid']//tr["+str(r)+"]/td[2]").text
            if emailid == email:
                flag = True
                break
        return flag

    def searchCustomerByName(self, Name):
        flag = False
        for r in range(1, self.getNoOfRows() + 1):
            table = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.table_xpath)))
            name = table.find_element(By.XPATH, "//table[@id='customers-grid']//tr[" + str(r) + "]/td[3]").text
            if name == Name:
                flag = True
                break
        return flag
