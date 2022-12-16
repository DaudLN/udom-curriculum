from django.urls import path
from .views import ProgramListAPIView, ProgramRetrieveAPIView
urlpatterns = [
    path('?format=json', ProgramListAPIView.as_view()),
    path('?format=json/<int:pk>', ProgramRetrieveAPIView.as_view())
]
