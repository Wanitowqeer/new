from django.urls import path
from .views import MusicianListView,MusicianDetailView,AlbumListView,AlbumdetailView
urlpatterns = [
    path('musicians/',MusicianListView.as_view(), name='musicians'),
    path('musicians/<int:pk>/', MusicianDetailView.as_view(), name='musician'),
    path('album/',AlbumListView.as_view(), name='albums'),
    path('album/<int:pk>/', AlbumdetailView.as_view(), name='album'),
   
]