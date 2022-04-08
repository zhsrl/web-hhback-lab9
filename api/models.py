from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    city = models.CharField(max_length=255)
    address = models.TextField()

    def __str__(self):
        return self.name

    def to_json(self):

        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'city': self.city,
            'address': self.address
        }


class Vacancy(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    salary = models.FloatField()
    company = models.ForeignKey(Company,
                                on_delete=models.CASCADE,
                                null=True,
                                related_name='company')

    def __str__(self):
        return self.name

    def to_json(self):

        return {
            'id': self.id,
            'name': self.name,
            'salary': self.salary,
            'company': self.company
        }
