from django.db import models

class todo(models.Model):
    task=models.CharField(max_length=500)
    start_time=models.TimeField(blank=True,null=True)
    end_time=models.TimeField(blank=True,null=True)
    date=models.DateField(auto_now_add=True)
    status=models.CharField(max_length=100)

    def __str__(self):
        return self.task + str(self.date)+ str(self.status)