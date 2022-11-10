from django.urls import path
from .views import index, get_category

urlpatterns = [
    path('', index, name='home'),
    path('newscat/<int:category_id>/', get_category, name='category'),
]
