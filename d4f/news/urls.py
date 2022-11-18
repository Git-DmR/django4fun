from django.urls import path
from .views import HomeNews, NewsByCategory, ViewSingleNews, add_news


urlpatterns = [
    path('', HomeNews.as_view(), name='home'),
    path('category/<int:category_id>/', NewsByCategory.as_view(), name='category'),
    path('news/<int:pk>', ViewSingleNews.as_view(), name='view_news'),
    path('news/add_news', add_news, name='add_news'),
]
