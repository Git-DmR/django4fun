from django import forms
from .models import News


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
