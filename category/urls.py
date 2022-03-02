from django.urls import path

from category import views

urlpatterns = [
    path('create-category/', views.CategoryCreateView.as_view(), name='create_category'),
    path('list-of-categories/', views.CategoryListView.as_view(), name='list_of_categories'),
    path('update-categories/<int:pk>/', views.CategoryUpdateView.as_view(), name='update_categories'),
    path('delete-categories/<int:pk>/', views.CategoryDeleteView.as_view(), name='delete_categories'),
    path('delete-category-popup/<int:pk>/', views.delete_category_with_popup, name='delete_with_popup'),
    path('detail-category/<int:pk>/', views.CategoryDetailsView.as_view(), name='details_category'),
]
