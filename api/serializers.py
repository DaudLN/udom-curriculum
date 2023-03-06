from rest_framework import serializers
from programs.models import Program


class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = [
            "name",
            "college",
            "description",
            "years_of_study",
            "fee",
            "knowledge",
            "skills",
            "competences",
            "special_requirements",
            "fields_of_work",
        ]
