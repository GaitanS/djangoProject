from django.urls import path

from home import views

urlpatterns = [
    path('index/', views.index, name='index1'),
    path('all-students/', views.student, name='all_students'),
    path('cars/', views.cars, name='cars1'),
    path('', views.HomeTemplateView.as_view(), name='homepage'),
]
