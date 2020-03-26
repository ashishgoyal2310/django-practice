from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import redirect


# Create your views here.

def register(request):

    print('Post result',request.POST)
    print('Get result' , request.GET)

    if request.method == 'POST':
        data = request.POST
        first_name = data['first_name']
        last_name = data['last_name']
        email = data['email']
        username = data['username']
        password1 = data['password1']
        password2 = data['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                print('***** USername taken **** ')
                return render(request, 'register.html', {'usererror':" Username already taken !!", 'message':"Please regsiter yourself !!"})
            elif User.objects.filter(email=email).exists():
                print('***** email taken **** ')
                return render(request, 'register.html', {'emailerror':" Email already taken !!", 'message':"Please regsiter yourself !!"})
            else:                
                user = User.objects.create_user(first_name=first_name,last_name=last_name,email=email,password=password1,username=username)
                user.save()
            
        else:
            print("*******  Password Does not matches *********** ")
            return render(request, 'register.html', {'passerror':" Password incorrect !!", 'message':"Please regsiter yourself !!"})
        return redirect('/')
    else:
        return render(request, 'register.html', {'message':"Please regsiter yourself !!"})