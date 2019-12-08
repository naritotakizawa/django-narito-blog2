from django.urls import path
from . import views

app_name = 'nblog2'

urlpatterns = [
    path('', views.NoteList.as_view(), name='note_list'),
    path('detail/<int:pk>/', views.NoteDetail.as_view(), name='note_detail'),
    path('upload/', views.upload, name='upload'),
]
