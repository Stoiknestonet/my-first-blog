from django.urls import path
from . import views

urlpatterns = [
    path('', view.post_vist, name='post_list'),
]