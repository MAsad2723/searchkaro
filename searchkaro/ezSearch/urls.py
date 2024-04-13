from django.urls import path
from ezSearch import views
urlpatterns = [
    path('', views.index, name='homepage'),
    path('data/<str:docid>', views.viewpost, name='viewpost'),
]