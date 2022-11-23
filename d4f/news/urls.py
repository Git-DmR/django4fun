from django.urls import path, include
from .views import HomeNews, NewsByCategory, ViewSingleNews, CreateNews, register, login


urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('__debug__/', include('debug_toolbar.urls')),
    path('', HomeNews.as_view(), name='home'),
    path('category/<int:category_id>/', NewsByCategory.as_view(), name='category'),
    path('news/<int:pk>', ViewSingleNews.as_view(), name='view_news'),
    path('news/add_news', CreateNews.as_view(), name='add_news'),

]
