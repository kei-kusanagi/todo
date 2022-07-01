from django.contrib import admin
from django.urls import path

from todo.views import todos

urlpatterns = [
    path('', todos, name='todos'),
    path('admin/', admin.site.urls),
]
