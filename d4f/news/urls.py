from django.urls import path, include
from .views import HomeNews, NewsByCategory, ViewSingleNews, CreateNews, register, user_login, user_logout


urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('__debug__/', include('debug_toolbar.urls')),
    path('', HomeNews.as_view(), name='home'),
    path('category/<int:category_id>/', NewsByCategory.as_view(), name='category'),
    path('news/<int:pk>', ViewSingleNews.as_view(), name='view_news'),
    path('news/add_news', CreateNews.as_view(), name='add_news'),

]
