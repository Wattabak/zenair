from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from api import views

urlpatterns = [
    path('airplanes/', views.AirplanesView.as_view()),
    path('airplanes/<int:pk>/', views.AirplaneView.as_view()),
    path('airplanes/spec/<int:pk>', views.AirplaneSpec.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
