class Login():
    def __init__(self,driver):
        self.driver = driver

    def zoomin_login(self,un,pwd):
        # Login to the application
        self.driver.find_element_by_xpath("//a[text()='Sign In']").click()
        self.driver.find_element_by_xpath("//input[@placeholder='Email or Username']").send_keys(un)
        self.driver.find_element_by_id("password").send_keys(pwd)
        self.driver.find_element_by_id("btnSignin").click()


