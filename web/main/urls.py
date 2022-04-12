from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.ZipAirlinesView.as_view(), name='zip_airlines')
]
