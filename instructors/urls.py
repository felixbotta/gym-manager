from django.urls import path
from .views import *
from members.views import list_members

app_name = 'instructors'
urlpatterns = [
    path('', list_instructor, name='list'),
    path('detalhes/<int:id>', details, name='details'),
    path('adicionar/', create_instructor, name='create'),
    path('atualizar/<int:id>', update_instructor, name='update'),
    path('deletar/<int:id>', delete_instructor, name='delete'),
]
