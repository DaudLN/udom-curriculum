from django.urls import path
from .views import *

urlpatterns = [
    path("programs", ProgramListView.as_view(), name="program_list"),
    path("programs/<slug:program>", program_detail, name="program_detail"),
    path("searh_program", search_program, name="search_program"),
    path("program/generate_pdf/<slug:program>", generate_pdf, name="program_pdf"),
    # path("colleges/", list_of_college, name="list_of_college")
]
