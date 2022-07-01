from django.contrib import admin
from django.urls import path

from todo.views import todos, add_todo

urlpatterns = [
    path('', todos, name='todos'),
    path('add-todo/', add_todo, name='add_todo'),
    path('admin/', admin.site.urls),
]
