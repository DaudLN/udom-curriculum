from django.urls import path
from .views import ProgramListAPIView, ProgramRetrieveAPIView
urlpatterns = [
    path('?format=json', ProgramListAPIView.as_view()),
    path('/<int:pk>', ProgramRetrieveAPIView.as_view())
]
