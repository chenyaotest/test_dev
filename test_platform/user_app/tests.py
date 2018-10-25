from django.test import TestCase
from django.contrib.auth.models import User

# Create your tests here.
# 单元测试


class UserModuleTest(TestCase):
    """ 模型测试 """

    def setUp(self):
        User.objects.create_user("test01", "test01@gmail.com", "test123456")

    def test_user_create(self):
        """测试添加用户"""
        user = User.objects.get(username="test01")
        self.assertEqual(user.username, 'test01')
        self.assertEqual(user.email, 'test01@gmail.com')

    def test_user_update(self):
        """测试更新用户"""
        user = User.objects.get(username="test01")
        user.username = "test02"
        user.email = "test02@gmail.com"
        user.save()
        user2 = User.objects.get(username="test02")
        self.assertEqual(user2.username, 'test02')
        self.assertEqual(user2.email, 'test02@gmail.com')

    def test_delete_user(self):
        """测试删除用户"""
        User.objects.get(username="test01").delete()
        user = User.objects.filter(username="test01")
        self.assertEqual(len(user), 0)


class IndexPageTest(TestCase):
    """测试index页面"""

    def test_index_page_renders_index_template(self):
        """断言是否用给定的index.html模版响应"""

        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')


class LoginActionTest(TestCase):
    """测试登录动作"""

    def setUp(self):
        User.objects.create_user('user01', 'user01@gmail.com', 'user123456')

    def test_username_password_null(self):
        """户名密码为空"""
        response = self.client.post(
            '/login_action/', {'username': '', 'password': ''})
        login_html = response.content.decode('utf-8')
        self.assertEqual(response.status_code, 200)
        self.assertIn("用户名或密码为空", login_html)

    def test_username_password_error(self):
        """用户名或密码错误"""
        response = self.client.post(
            '/login_action/', {'username': 'test', 'password': 'test'})
        login_html = response.content.decode('utf-8')
        self.assertEqual(response.status_code, 200)
        self.assertIn("用户名或密码错误", login_html)

    def test_success(self):
        """登录成功"""
        response = self.client.post(
            '/login_action/', data={'username': 'user01', 'password': 'user123456'})
        self.assertEqual(response.status_code, 302)
