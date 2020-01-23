import string,random
from django.contrib.auth.hashers import make_password
from django.shortcuts import redirect,render,HttpResponseRedirect
from Account.models import Account
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages

def randomPassword():
    password = ''
    letters = string.ascii_letters + string.digits + string.punctuation
    for i in range(10):
        password = password+str(random.choice(letters))
    return password

def changepassword(request):
    if request.method == 'GET':
        return render(request,'forgot_password.html')
    else:
        p1 = request.POST.get('password1')
        p2 = request.POST.get('password2')
        if p1 == p2:
            user = Account.objects.get(id=request.user.id)
            user.password = make_password(p1)
            user.is_firstLogin = False
            user.save()
            logout(request)
            messages.add_message(request, messages.SUCCESS, 'Password Change Successfully')
            return redirect('signin')
        else:
            messages.add_message(request, messages.ERROR, 'password does not match')
            return redirect('changepassword')