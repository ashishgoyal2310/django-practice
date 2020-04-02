from django.db import models

# Create your models here.

class Result(models.Model):
    TITLE_LIST = (
        ('JTR', 'JUWAI TEER RESULT'),
        ('KTR', 'KHANAPARA TEER RESULT'),
        ('STR', 'SHILLONG TEER RESULT'),
        ('JLTR', 'JOWAI-LADRYMBAI TEER RESULT'),
        ('NTR', 'NIGHT TEER RESULT'),
    )

    title = models.CharField(max_length=20, choices=TITLE_LIST)
    param1_title = models.CharField(max_length=30)
    param2_title = models.CharField(max_length=30)
    param1_time = models.TimeField()
    param2_time = models.TimeField()
    param1_data = models.IntegerField()
    param2_data = models.IntegerField()


class DreamNumber(models.Model):
    dream = models.CharField(max_length=32)
    num = models.CharField(max_length=16,blank=True)
    house = models.CharField(max_length=16,blank=True)
    ending = models.CharField(max_length=16,blank=True)


class ResultList(models.Model):
    date = models.DateField()
    FR = models.IntegerField()
    SR = models.IntegerField()


class CommonNumber(models.Model):
    TITLE_LIST = (
        ('KTR', 'KHANAPARA TEER RESULT'),
        ('STR', 'SHILLONG TEER RESULT'),
    )
    title = models.CharField(max_length=32, choices=TITLE_LIST)
    direct = models.CharField(max_length=10)
    house = models.IntegerField()
    ending = models.IntegerField()