from django.contrib import admin
from teerresults.models import Result
from teerresults.models import DreamNumber, ResultList, CommonNumber
# Register your models here.
admin.site.register(Result)
admin.site.register(DreamNumber)
admin.site.register(ResultList)
admin.site.register(CommonNumber)