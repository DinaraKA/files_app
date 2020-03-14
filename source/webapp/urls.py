from django.urls import path
from webapp.views import IndexView, FileDetailView, FileCreateView, FileUpdateView, FileDeleteView, AddToPrivate, UserPrivateDelete

app_name = 'webapp'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('file/<int:pk>/', FileDetailView.as_view(), name='file_detail'),
    path('file/add/', FileCreateView.as_view(), name='file_create'),
    path('file/edit/<int:pk>/', FileUpdateView.as_view(), name='file_edit'),
    path('file/delete/<int:pk>/', FileDeleteView.as_view(), name='file_delete'),
    path('user/add-to-private/', AddToPrivate.as_view(), name='add_to_private'),
    path('user/delete-from-favorites/', UserPrivateDelete.as_view(), name='delete_from_privates'),
]
