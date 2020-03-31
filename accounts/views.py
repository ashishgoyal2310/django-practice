from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout

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
            return render(request, 'register.html', {'passerror':" Password incorrect !!", 'message':"Please Register yourself !!"})
        return redirect('/accounts/login/')
    else:
        return render(request, 'register.html', {'message':"Please Register yourself !!"})


def login_view(request):
    if request.method == 'POST':
        username= request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'login.html', {'muser':"Invalid credentials  !!"})
    else:
        return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('/')