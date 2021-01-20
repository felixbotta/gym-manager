from django.urls import path
from .views import home
from instructors.views import list_instructor
from members.views import list_members


app_name = 'core'
urlpatterns = [
    path('', list_instructor, name='list'),
]