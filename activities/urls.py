from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # ex: /activities/
    path('', views.index, name='index'),
    # ex: /activities/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /activities/5/listactions/
    path('<int:question_id>/listactions/', views.listactions, name='listactions'),
    # ex: /activities/5/priority/
    path('<int:question_id>/priority/', views.priority, name='priority'),
]