from django.contrib import admin
from django.urls import path

from uploader import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.UploadView.as_view(), name='upload'),
    path('signed-url/', views.SignedURLView.as_view(), name='signed-url')
]
