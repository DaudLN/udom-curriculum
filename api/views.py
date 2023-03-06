from rest_framework import generics
from .serializers import ProgramSerializer
from programs.models import Program

# Create your views here.

from .renderers import CustomJSONRenderer

# Your viewset methods...


class ProgramListAPIView(generics.ListAPIView):
    renderer_classes = [CustomJSONRenderer]
    serializer_class = ProgramSerializer
    queryset = Program.objects.all()


class ProgramRetrieveAPIView(generics.RetrieveAPIView):
    renderer_classes = [CustomJSONRenderer]
    serializer_class = ProgramSerializer
    queryset = Program.objects.all()
