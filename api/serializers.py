from rest_framework import serializers
from .models import Vacancy


class VacancySerializer(serializers.ModelSerializer):
    company = serializers.PrimaryKeyRelatedField(
        read_only=True,
    )

    class Meta:
        model = Vacancy
        fields = ('id', 'name', 'description', 'salary', 'company')
