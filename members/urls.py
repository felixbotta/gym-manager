from django.urls import *
from .views import *

app_name = 'members'
urlpatterns = [
    path('', list_members, name='list'),
    path('detalhes/<int:id>', details_members, name='details'),
    path('adicionar/', create_members, name='create'),
    path('atualizar/<int:id>', update_members, name="update"),
    path('deletar/<int:id>', delete_members, name='delete'),

]
