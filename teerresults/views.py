from django.shortcuts import render
from django.http import HttpResponse
from teerresults.models import Result,DreamNumber, ResultList, CommonNumber 
import datetime

# Create your views here.

def teerhome(request): 

    teer_all = Result.objects.all()
    return render(request, 'teerhome.html', {
                                                'name': 'RITESH', 
                                                'last': 'GOYAL', 
                                                'teer_all': teer_all,
                                            }   
                                        )

def dreamnumber(request): 
    
    dream_all = DreamNumber.objects.all()
    return render(request, 'dreamnumber.html', {'dream_all': dream_all})

def commonnumber(request):
    common_str = CommonNumber.objects.filter(title='STR')
    common_ktr = CommonNumber.objects.filter(title='KTR')
    return render(
        request, 'commonnumber.html',
        {'common_str': common_str, 'common_ktr': common_ktr}
        )

def resultlist(request):

    # result_all = ResultList.objects.all()
    return render(request, 'resultlist.html')
