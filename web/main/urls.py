from django.urls import path

from . import views

app_name = 'main'

urlpatterns = [path('consumption-check/', views.ZipAirlinesView.as_view(), name='zip_airlines')]
