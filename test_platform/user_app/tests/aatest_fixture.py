from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver import Chrome
from time import sleep


class LoginTests(StaticLiveServerTestCase):
    # python manage.py dumpdata - -format = json >user_app/fixtures/data.json
    fixtures = ['data.json']

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.driver = Chrome()
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        super().tearDownClass()

    def test_login(self):
        self.driver.get('%s%s' % (self.live_server_url, '/'))
        username_input = self.driver.find_element_by_name("username")
        username_input.send_keys("")

        password_input = self.driver.find_element_by_name("password")
        password_input.send_keys("")
        sleep(1)
        self.driver.find_element_by_id('LoginButton').click()
        error_hint = self.driver.find_element_by_id("error").text
        print(error_hint)
        self.assertEqual("用户名或密码为空", error_hint)

    def test_login_error(self):
        self.driver.get('%s%s' % (self.live_server_url, '/'))
        username_input = self.driver.find_element_by_name("username")
        username_input.send_keys("error")
        password_input = self.driver.find_element_by_name("password")
        password_input.send_keys("error")
        sleep(1)
        self.driver.find_element_by_id('LoginButton').click()
        error_hint = self.driver.find_element_by_id("error").text
        print(error_hint)
        self.assertEqual("用户名或密码错误", error_hint)

    def test_login_success(self):
        self.driver.get('%s%s' % (self.live_server_url, '/'))
        username_input = self.driver.find_element_by_name("username")
        username_input.send_keys("admin")
        password_input = self.driver.find_element_by_name("password")
        password_input.send_keys("Aa956243cy")
        sleep(1)
        self.driver.find_element_by_id('LoginButton').click()
        error_hint = self.driver.find_element_by_class_name("navbar-brand").text
        print(error_hint)
        self.assertEqual("测试平台", error_hint)
