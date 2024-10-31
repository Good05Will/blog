from django.urls import path
from . import views

app_name = 'blog_app'
urlpatterns = [
    # Домашняя страница.
    path('', views.index, name='index'),
    # Страница всех тем
    path('posts/', views.posts, name='posts'),
    # Страница отдельной темы.
    path('post/<int:post_id>/', views.post, name='post'),
    # Новая ТЕМА
    path('new_post/', views.new_post, name='new_post'),
    # Новая ЗАПИСЬ
    path('new_note/<int:post_id>/', views.new_note, name='new_note'),
    # Редактирование ТЕМЫ
    path('edit_post/<int:post_id>/', views.edit_post, name='edit_post'),
    # Редактирование ЗАПИСИ
    path('edit_note/<int:note_id>/', views.edit_note, name='edit_note'),
    # Страница ошибки
    path('error/', views.error, name='error'),
]