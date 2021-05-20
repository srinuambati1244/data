from django.urls import path
from cook import views
urlpatterns = [
    path('',views.simple_upload,name='simple_upload'),
    path(' export/',views.export,name='export'),
]