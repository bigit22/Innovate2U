from django.urls import path
from . import views

app_name = 'training'

urlpatterns = [
    path('', views.training, name='training'),
    path('exercise/<int:ex_id>', views.exercise, name='exercise')
]

