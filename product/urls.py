from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from product import views

urlpatterns = [
    path('create-product/', views.ProductCreatView.as_view(), name='creat_product'),
    path('list-of-products/', views.ProductListView.as_view(), name='list_of_products'),
    path('update-product/<int:pk>/', views.ProductUpdateView.as_view(), name='update_product'),
    path('delete-product/<int:pk>/', views.ProductDeleteView.as_view(), name='delete_product'),
    path('detail-product/<int:pk>/', views.ProductDetailsView.as_view(), name='details_product'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
