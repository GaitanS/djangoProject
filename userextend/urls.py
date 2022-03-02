from django.urls import path

from userextend import views

urlpatterns = [
    path('user/', views.UserExtendCreatView.as_view(), name='create_user'),

]
