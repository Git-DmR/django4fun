from django.db import models


class News(models.Model):
    title = models.CharField(max_length=150, verbose_name="Наименование")
    content = models.TextField(verbose_name="Содержание", blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата содания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата публикации")
    photo = models.ImageField(upload_to='photos/%y/%m/%d', verbose_name="Изображение", blank=True)
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано" )

    def __str__(self):
        return f'{self.title} model'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = "Новости"
        ordering = ['-created_at', "title"]
