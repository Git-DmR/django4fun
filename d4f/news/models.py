from django.db import models
from django.urls import reverse_lazy


class News(models.Model):
    title = models.CharField(max_length=150, verbose_name="Наименование")
    content = models.TextField(verbose_name="Содержание", blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата содания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата публикации")
    photo = models.ImageField(upload_to='photos/%y/%m/%d', verbose_name="Изображение", blank=True)
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")
    category = models.ForeignKey('Category', verbose_name="Категория", on_delete=models.PROTECT)

    def get_absolute_url(self):
        return reverse_lazy('view_news',kwargs={"news_id": self.pk})

    def __str__(self):
        return f'{self.title} model'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = "Новости"
        ordering = ['-created_at', "title"]


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name="Название категории")

    def get_absolute_url(self):
        return reverse_lazy('category',kwargs={"category_id": self.pk})


    def __str__(self):
        return f'{self.title}'.upper()

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = "Категории"
        ordering = ["title"]
