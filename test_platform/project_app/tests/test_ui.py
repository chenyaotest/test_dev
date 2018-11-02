from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver import Chrome
from time import sleep
from django.contrib.auth.models import User
from project_app.models import Project, Module


class ProjectTests(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.driver = Chrome()
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        super().tearDownClass()

    def setUp(self):
        """初始化数据"""
        User.objects.create_user("test01", "test01@mail.com", "test123456")
        Project.objects.create(name="测试平台项目", describe="描述")
        self.driver.get('%s%s' % (self.live_server_url, '/'))
        username_input = self.driver.find_element_by_name("username")
        username_input.send_keys("test01")
        password_input = self.driver.find_element_by_name("password")
        password_input.send_keys("test123456")
        sleep(1)
        self.driver.find_element_by_id('LoginButton').click()

    def test_add_project(self):
        self.driver.get('%s%s' % (self.live_server_url, '/manage/add_project/'))
        username_input = self.driver.find_element_by_name("name")
        username_input.send_keys("项目A")
        password_input = self.driver.find_element_by_name("describe")
        password_input.send_keys("项目A的描述")
        self.driver.find_element_by_id('id_status').click()
        sleep(1)
        self.driver.find_element_by_id('SaveButton').click()
        sleep(1)
        success_hint = self.driver.find_element_by_xpath("//table[@class='table table-striped']/tbody/tr[2]/td[2]").text
        # print(error_hint)
        self.assertEqual("项目A", success_hint)

    def test_edit_project(self):
        self.driver.get('%s%s' % (self.live_server_url, '/manage/edit_project/1'))
        username_input = self.driver.find_element_by_name("name")
        username_input.clear()
        username_input.send_keys("项目B")
        password_input = self.driver.find_element_by_name("describe")
        password_input.clear()
        password_input.send_keys("项目B的描述")
        self.driver.find_element_by_id('id_status').click()
        sleep(1)
        self.driver.find_element_by_id('SaveButton').click()
        sleep(5)
        success_hint = self.driver.find_element_by_xpath("//table[@class='table table-striped']/tbody/tr[1]/td[2]").text
        # print(error_hint)
        self.assertEqual("项目B", success_hint)

    def test_delete_project(self):
        self.driver.get('%s%s' % (self.live_server_url, '/manage/delete_project/1'))
        sleep(1)
        pro = self.driver.find_element_by_id('plist').find_elements_by_xpath('tbody/tr')
        self.assertEqual(len(pro), 0)


class ModuleTests(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.driver = Chrome()
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        super().tearDownClass()

    def setUp(self):
        """初始化数据"""
        User.objects.create_user("test01", "test01@mail.com", "test123456")
        Project.objects.create(name="测试平台项目", describe="描述")
        project_obj = Project.objects.get(name='测试平台项目')
        Module.objects.create(name='模块A', describe='模块AAA', project=project_obj)
        Project.objects.create(name="测试平台项目2", describe="描述2")
        self.driver.get('%s%s' % (self.live_server_url, '/'))
        username_input = self.driver.find_element_by_name("username")
        username_input.send_keys("test01")
        password_input = self.driver.find_element_by_name("password")
        password_input.send_keys("test123456")
        sleep(1)
        self.driver.find_element_by_id('LoginButton').click()
        self.driver.find_element_by_link_text('模块管理').click()

    def test_add_module(self):
        self.driver.get('%s%s' % (self.live_server_url, '/manage/add_module/'))
        self.driver.find_element_by_id("id_project").send_keys("测试平台项目")
        username_input = self.driver.find_element_by_name("name")
        username_input.send_keys("模块B")
        password_input = self.driver.find_element_by_name("describe")
        password_input.send_keys("模块B的描述")
        sleep(1)
        self.driver.find_element_by_id('SaveButton').click()
        sleep(5)
        success_hint = self.driver.find_element_by_xpath("//table[@class='table table-striped']/tbody/tr[2]/td[2]").text
        # print(error_hint)
        self.assertEqual("模块B", success_hint)

    def test_edit_module(self):
        self.driver.get('%s%s' % (self.live_server_url, '/manage/edit_module/1'))
        self.driver.find_element_by_id("id_project").send_keys("测试平台项目2")
        username_input = self.driver.find_element_by_name("name")
        username_input.clear()
        username_input.send_keys("模块C")
        password_input = self.driver.find_element_by_name("describe")
        password_input.clear()
        password_input.send_keys("模块C的描述")
        sleep(1)
        self.driver.find_element_by_id('SaveButton').click()
        sleep(5)
        success_hint = self.driver.find_element_by_xpath("//table[@class='table table-striped']/tbody/tr[1]/td[2]").text
        self.assertEqual("模块C", success_hint)

    def test_delete_module(self):

        self.driver.get('%s%s' % (self.live_server_url, '/manage/delete_module/1'))
        sleep(5)
        pro = self.driver.find_element_by_id('mlist').find_elements_by_xpath('tbody/tr')
        self.assertEqual(len(pro), 0)
