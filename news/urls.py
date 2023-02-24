from django.urls import path
from .views import ProductsList, ProductDetail, ProductUpdate, ProductCreate, ProductDelete

urlpatterns = [
  path('', ProductsList.as_view(), name='post_list'),
  path('<int:pk>', ProductDetail.as_view(), name='postdetail'),
  path('create/', ProductCreate.as_view(), name='post_create'),
  path('<int:pk>/update/', ProductUpdate.as_view(), name='post_update'),
  path('<int:pk>/delete/', ProductDelete.as_view(), name='post_delete')
]