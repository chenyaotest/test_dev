from django import forms
from .models import Project

#class ProjectForm(forms.Form):
#    name = forms.CharField(label='项目名称', max_length=100)
#    describe = forms.Field(label='项目描述', widget=forms.Textarea)
#    status = forms.BooleanField(label='项目状态', required=False)


class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        exclude = ['create_time']
