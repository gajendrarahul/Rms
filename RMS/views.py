
from django.shortcuts import redirect,render,HttpResponseRedirect
from django.contrib.auth import authenticate,logout,login
from django.contrib import messages
from owner.models import OwnerInfo
from Account.models import Account
from django.contrib.auth.hashers import make_password

def home(request):
    return render(request,'signin.html')

def signin(request):
    if request.method == 'GET':
        return redirect('signin')
    else:
        u = request.POST.get('email')
        p = request.POST['password']
        user = authenticate(email=u, password=p)
        if user is not None:
            login(request, user)
            if request.user.is_admin:
                return redirect('admin')
            elif request.user.is_owner:
                return redirect('ownerview')
            elif request.user.is_client:
                return redirect('clientview')
            else:
                pass

        else:
            messages.error(request, 'Enter the valid username and password')
            return render(request,'owner_dashboard.html')
def admin(request):
    return render(request, 'admin_dashboard.html')


def signout(request):
    logout(request)
    return redirect('home')