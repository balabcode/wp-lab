from django.contrib import admin
from django.urls import path
from webapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('update_human/', views.update_human, name='update_human'),
    path('delete_human/', views.delete_human, name='delete_human'),
    path('get_human_data/', views.get_human_data, name='get_human_data')
]