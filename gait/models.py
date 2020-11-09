from django.db import models
from accounts.models import CustomUser

# Create your models here.
class Gaitdata(models.Model):
    data_json = models.TextField()
    created_date = models.DateTimeField('date created')
    owner = models.ForeignKey(CustomUser, default=1,
        on_delete=models.CASCADE,
        related_name='gaitdata')

    def __str__(self):
        return str(self.created_date)

