from django.db import models


class My_Model(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    age = models.SmallIntegerField()
    date_of_born = models.DateField()

    def __str__(self):
        return self.name
