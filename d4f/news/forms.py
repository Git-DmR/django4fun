from django import forms
from .models import News
import re
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label="Имя пользователя", widget=forms.TextInput(attrs={"class":"form-control"}))
    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={"class":"form-control"}))
    password2 = forms.CharField(label="Подтверждение пароля", widget=forms.PasswordInput(attrs={"class": "form-control"}))
    email = forms.EmailField(label="E-mail", widget=forms.EmailInput(attrs={"class": "form-control"}))

    class Meta(UserCreationForm):
        model = User
        fields = ("username","email", "password1", "password2",)


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label="Имя пользователя", widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={"class": "form-control"}))


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ["title", "content", "is_published", "category"]
        widgets = {
            "title" : forms.TextInput(attrs={"class":"form-control"}),
            "content" : forms.Textarea(attrs={"class":"form-control","rows":5}),
            "is_published" : forms.CheckboxInput(),
            "category" : forms.Select(attrs={"class":"form-control"}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError("Название не должно начинаться с цифры.")
        return title

    def clean_content(self):
        content = self.cleaned_data['content']
        if content == "":
            raise ValidationError("Содержание новости не может быть пустым.")
        return content

    def clean_category(self):
        category = self.cleaned_data['category']
        if category == None:
            raise ValidationError("Поле обязательно для заполнения.")
        else:
            return category





# from django import forms
# from .models import Category
#
# class NewsForm(forms.Form):
#     title = forms.CharField(
#         max_length=150,
#         label="Наименование",
#         widget=forms.TextInput(attrs={"class":"form-control"})
#     )
#
#     content = forms.CharField(
#         required=False,
#         label="Основной текст",
#         widget=forms.Textarea(attrs={"class":"form-control","rows":5})
#     )
#
#     is_published = forms.BooleanField(
#         label="Опубликовано",
#         initial=True,
#         widget=forms.CheckboxInput()
#     )
#
#     category = forms.ModelChoiceField(
#         queryset=Category.objects.all(),
#         empty_label="Выберите категорию",
#         label="Категория",
#         widget=forms.Select(attrs={"class":"form-control"})
#     )
