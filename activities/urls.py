from django.urls import path

from . import views

app_name = 'activities'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:schedule_id>/', views.detail, name='detail'),
    path('<int:action_id>/action-edit/', views.edit_action, name='edit-action'),
]