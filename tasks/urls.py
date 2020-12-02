from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='list'),
    path('update/<int:pk>', views.update_task, name='update'),
    path('delete/<int:pk>', views.delete_task, name='delete'),
]
