from django.contrib.auth.models import User
from django.test import TestCase
from project_app.models import Project, Module

# Create your tests here.
# 单元测试


class ProjectModuleTest(TestCase):
    """ 项目模型测试 """

    def setUp(self):
        Project.objects.create(name='自动化测试项目', describe='自动化测试项目AAA', status='1')

    def test_project_create(self):
        """测试添加项目"""
        project = Project.objects.get(name="自动化测试项目")
        self.assertEqual(project.name, '自动化测试项目')
        self.assertEqual(project.describe, '自动化测试项目AAA')

    def test_project_update(self):
        """测试更新项目"""
        project = Project.objects.get(name="自动化测试项目")
        project.name = "自动化测试项目222"
        project.describe = "自动化测试项目BBB"
        project.save()
        project2 = Project.objects.get(name="自动化测试项目222")
        self.assertEqual(project2.name, '自动化测试项目222')
        self.assertEqual(project2.describe, '自动化测试项目BBB')

    def test_delete_project(self):
        """测试删除项目"""
        Project.objects.get(name="自动化测试项目").delete()
        project = Project.objects.filter(name="自动化测试项目")
        self.assertEqual(len(project), 0)


class ModuleModuleTest(TestCase):
    """ 模块模型测试 """

    def setUp(self):
        Project.objects.create(name='自动化测试项目', describe='自动化测试项目AAA', status='1')
        Project.objects.create(name='自动化测试项目2', describe='自动化测试项目AAA222', status='1')
        project_obj = Project.objects.get(name='自动化测试项目')
        Module.objects.create(name='模块A', describe='模块AAA', project=project_obj)

    def test_module_create(self):
        """测试添加模块"""
        module = Module.objects.get(name="模块A")
        self.assertEqual(module.name, '模块A')
        self.assertEqual(module.describe, '模块AAA')
        project_obj = Project.objects.get(name='自动化测试项目')
        self.assertEqual(module.project, project_obj)

    def test_module_update(self):
        """测试更新模块"""
        module = Module.objects.get(name="模块A")
        module.name = "模块B"
        module.describe = "模块BBB"
        project_obj = Project.objects.get(name='自动化测试项目2')
        module.project = project_obj
        module.save()
        module2 = Module.objects.get(name="模块B")
        self.assertEqual(module2.name, '模块B')
        self.assertEqual(module2.describe, '模块BBB')
        project_obj2 = Project.objects.get(name='自动化测试项目2')
        self.assertEqual(module2.project, project_obj2)

    def test_delete_module(self):
        """测试删除模块"""
        Module.objects.get(name="模块A").delete()
        module = Module.objects.filter(name="模块A")
        self.assertEqual(len(module), 0)


class ProjectManagePageTest(TestCase):
    """测试项目管理页面"""

    def setUp(self):
        User.objects.create_user('user01', 'user01@gmail.com', 'user123456')
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.client.post(
            '/login_action/', data={'username': 'user01', 'password': 'user123456'})

    def test_project_manage_page_renders_project_manage_template(self):
        """断言是否用给定的project_manage.html模版响应"""

        response = self.client.get('/manage/project_manage/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'project_manage.html')


class ProjectActionTest(TestCase):
    """测试项目动作"""

    def setUp(self):
        User.objects.create_user('user01', 'user01@gmail.com', 'user123456')
        self.client.get('/')
        response = self.client.post('/login_action/', data={'username': 'user01', 'password': 'user123456'})
        self.assertEqual(response.status_code, 302)
        self.client.post('/manage/add_project/', data={'name': '项目A', 'describe': '项目AAA', 'status': True})
        self.assertEqual(response.status_code, 302)

    def test_create_project(self):
        """创建项目"""

        response = self.client.post('/manage/add_project/', data={'name': '项目B', 'describe': '项目BBB', 'status': True})
        response.content.decode('utf-8')
        self.assertEqual(response.status_code, 302)

    def test_edit_project(self):
        """修改项目"""
        response = self.client.post(
            '/manage/edit_project/1/', data={'pid': '1', 'name': '项目A2', 'describe': '项目AAA2', 'status': '1'})
        response.content.decode('utf-8')
        self.assertEqual(response.status_code, 302)

    def test_delete_project(self):
        """删除项目"""
        response = self.client.post(
            '/manage/delete_project/1/', data={'pid': '1'})
        project_manage_html = response.content.decode('utf-8')
        self.assertEqual(response.status_code, 302)
        self.assertNotIn("项目A2", project_manage_html)


class ModuleActionTest(TestCase):
    """测试模块动作"""

    def setUp(self):
        User.objects.create_user('user01', 'user01@gmail.com', 'user123456')
        self.client.get('/')
        response = self.client.post('/login_action/', data={'username': 'user01', 'password': 'user123456'})
        self.assertEqual(response.status_code, 302)
        Project.objects.create(name='自动化测试项目', describe='自动化测试项目AAA', status='1')
        response2 = self.client.post('/manage/add_project/', data={'name': '项目A', 'describe': '项目AAA', 'status': True})
        self.assertEqual(response2.status_code, 302)
        project_obj = Project.objects.get(name='项目A')
        Module.objects.create(name='模块A', describe='模块AAA', project=project_obj)

    def test_create_module(self):
        """创建模块"""

        data = {'project': 1, 'name': '模块B', 'describe': '模块BBB'}
        response = self.client.post('/manage/add_module/', data=data)
        module_html = response.content.decode('utf-8')
        print(module_html)
        self.assertEqual(response.status_code, 302)

    def test_edit_module(self):
        """修改模块"""

        response = self.client.post(
            '/manage/edit_module/1/', data={'mid': '1', 'name': '模块A2', 'describe': '模块AAA2', 'project': 1})
        module_html = response.content.decode('utf-8')
        print(module_html)
        self.assertEqual(response.status_code, 302)

    def test_delete_module(self):
        """删除模块"""
        response = self.client.post(
            '/manage/delete_module/1/', data={'mid': '1'})
        response.content.decode('utf-8')
        self.assertEqual(response.status_code, 302)

