from django.urls import path

from . import views

app_name = 'notes'

urlpatterns = [
    path('', views.note_list, name='note_list'),
    path('note/<int:note_id>/', views.note_detail, name='detail'),
    path("users/<int:user_id>/", views.user_detail, name="user_detail"),
    path("notes/create/", views.note_create, name="note_create"),
    path("<int:note_id>/edit/", views.note_edit, name="note_edit"),
    path("<int:note_id>/delete/", views.note_delete, name="note_delete"),
]
