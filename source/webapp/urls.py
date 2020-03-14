from django.urls import path
from webapp.views import IndexView, FileDetailView, FileCreateView, FileUpdateView, FileDeleteView

app_name = 'webapp'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('file/<int:pk>/', FileDetailView.as_view(), name='file_detail'),
    path('file/add/', FileCreateView.as_view(), name='file_create'),
    path('file/edit/<int:pk>/', FileUpdateView.as_view(), name='file_edit'),
    path('file/delete/<int:pk>/', FileDeleteView.as_view(), name='file_delete'),
    # path('ad/<int:pk>/image/add/', AdImageAdd.as_view(), name='ad_image_add'),
    # path('photo/delete/<int:pk>/', ImageDeleteView.as_view(), name='photo_delete'),
    # path('product/add-to-favorites/', AddToFavorites.as_view(), name='add_to_favorites'),
    # path('product/delete-from-favorites/', DeleteFromFavorites.as_view(), name='delete_from_favorites'),
]
