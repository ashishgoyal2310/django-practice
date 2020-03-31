from django.http import HttpResponse 
from django.shortcuts import render
# import datetime

# def current_datetime(request):
#     now = datetime.datetime.now()
#     html = "<html><body>It is now %s.</body></html>" % now
#     return HttpResponse(html)

def home(request):
	return render(request, 'home.html', {'name': 'Ashish', 'add': 'hn 46 b block'})

def add(request):
	print(request.POST)
	v1 = int(request.POST.get('num1'))
	v2 = int(request.POST['num2'])
	result = v1 + v2
	#result = 0
	return render(request, 'result.html', {'resu': result})

def practice(request):
	return render(request, 'practice.html')
