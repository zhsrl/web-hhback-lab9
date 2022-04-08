from django.urls import path

from api import views
from api.views import CompanyView, VacancyView


urlpatterns = [
    path('companies/', CompanyView.as_view()),
    path('companies/<int:id>', CompanyView.get_single),
    path('companies/<int:id>/vacancies', VacancyView.get_vacs_by_company),
    path('vacancies/', VacancyView.as_view()),
    path('vacancies/<int:id>', VacancyView.get_single),
    path('vacancies/top_ten', VacancyView.top_ten),

]
