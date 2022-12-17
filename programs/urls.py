from django.urls import path
from .views import *

urlpatterns = [
    path('pdf', ProgramDetailView.generate_pdf, name='generate_pdf'),
    path('programs/', ProgramListView.as_view(), name='program_list'),
    path('programs/<int:pk>',
         ProgramDetailView.as_view(),
         name='program_detail'),
    path('searh_program/', search_program, name="search_program"),
    path('generate_pdf/<int:pk>', generate_pdf, name="program_pdf"),
]
