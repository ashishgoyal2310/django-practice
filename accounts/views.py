from django.shortcuts import render

# Create your views here.

def register(request):
    print('Post result',request.POST)
    print('Get result' , request.GET)
    return render(request, 'register.html')