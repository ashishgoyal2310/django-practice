from django.shortcuts import render
from django.http import HttpResponse
from teerresults.models import Result

# Create your views here.

def teerhome(request): 
    teer_dct = dict(Result.TITLE_LIST)
    print('--------', teer_dct)

    teer_all = Result.objects.all()
    for teer in teer_all:
        teer_dct[teer.title] = teer
    print('--------===========', teer_dct)

    return render(request, 'teerhome.html', {
                                                'name': 'RITESH', 
                                                'last': 'GOYAL', 
                                                'teer_all': teer_all,
                                                'teer_dct': teer_dct,
                                            }   
                                        )