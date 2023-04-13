from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('portfolio', views.projects, name='projects'),
    path('resume/<str:card_filter>', views.resume, name='resume')
]
