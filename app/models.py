from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Timesave(models.Model):
    save_user = models.ForeignKey(User, on_delete = models.CASCADE)
    save_date = models.IntegerField(default=0)
    input_date = models.DateTimeField('date published', default=timezone.now)
    
    # @property
    # def total_save_time(self):
    #     return self.save_date.count()

    def __str__(self):
        return '%s - %s' % (self.save_user, self.save_date) 