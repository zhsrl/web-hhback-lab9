
import operator
import logging
from django.shortcuts import render

from django.views import View
from django.http import HttpResponse, JsonResponse

from django.core.serializers import serialize


from .serializers import VacancySerializer

from .models import Company, Vacancy

LOGGER = logging.getLogger("mylogger")


class CompanyView(View):

    def get(self, request):
        all_companies = Company.objects.all()
        companies_count = Company.objects.count()

        companies_serialized = serialize('python', all_companies)

        companies = {
            'companies': companies_serialized,
            'count': companies_count
        }

        return JsonResponse(companies)

    def get_single(request, id):
        single_company = Company.objects.get(id=id)

        LOGGER.info("COMPID")
        LOGGER.info(single_company.pk)

        return JsonResponse(single_company.to_json())


class VacancyView(View):

    def get(self, request):
        all_vacancy = Vacancy.objects.all()
        vacany_count = Vacancy.objects.count()

        serialized_data = VacancySerializer(
            all_vacancy, many=True).data

        vacancies = {
            'vacancies': serialized_data,
            'count': vacany_count
        }

        return JsonResponse(vacancies)

    def get_single(request, id):
        single_vacancy = Vacancy.objects.get(id=id)

        return JsonResponse(single_vacancy.to_json())

    def top_ten(request):
        sorted_vacancy = Vacancy.objects.order_by('-salary')[:10]

        serialized = VacancySerializer(sorted_vacancy, many=True).data

        vacancies = {
            'vacancies': serialized,
        }

        LOGGER.info(vacancies)

        return JsonResponse(vacancies)

    def get_vacs_by_company(request, id):
        company = Company.objects.get(id=id)

        comp_id = company.pk
        vacancies = Vacancy.objects.filter(company=comp_id)

        serialized_vacs = VacancySerializer(vacancies, many=True).data

        total_vacs = {
            'vacancies': serialized_vacs
        }

        LOGGER.info("GGTX")
        LOGGER.info(vacancies)

        return JsonResponse(total_vacs)
