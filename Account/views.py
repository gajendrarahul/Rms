from django.shortcuts import render,redirect
from RMS.password import randomPassword
from django.contrib.auth.hashers import make_password
from Account.models import Account
from owner.models import OwnerInfo
from django.contrib import messages
from RMS.mail import Mail
from client.models import Client


# Create your views here.
def OwnerAccountCreate(request):
    if request.method == 'GET':
        return render(request,'owner_register.html')
    else:
        email = request.POST.get('email')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        contact = request.POST['contact']
        address = request.POST['address']
        password = randomPassword()
        user = Account(email=email, first_name=fname,last_name=lname,password=make_password(password),is_owner=True,is_client=False)
        user.save()
        msg = f'{fname + lname}, your account is created successfully \n use the following credential to login \n email:{email} \n password:{password}'
        Mail(subject='Account created', message=msg, recipient_list=[email])
        owner = OwnerInfo(email=request.user.email,address=address,name=fname + lname, contact=contact, user_id=user.id)
        owner.save()
        messages.add_message(request,messages.SUCCESS,'owner Account is created successfully')
        return render(request,'signin.html')


def ClientAccountCreate(request):
    if request.method == 'GET':
        return render(request,'client_register.html')
    else:
        fname = request.POST['fname']
        lname = request.POST['lname']
        contact = request.POST['contact']
        address = request.POST.get('address')
        email = request.POST['email']
        no_of_person = request.POST['no_of_person']
        password = randomPassword()
        user = Account(email=email, first_name=fname, last_name=lname, password=make_password(password), is_owner=False,
                       is_client=True)
        user.save()
        msg = f'{fname + lname}, your account is created successfully \n use the following credential to login \n email:{email} \n password:{password}'
        Mail(subject='Account created', message=msg, recipient_list=[email])
        client = Client(name=fname+lname, contact=contact, address=address, email=email, no_of_person=no_of_person, user_id=user.id)
        client.save()
        messages.add_message(request,messages.SUCCESS,'client Account created successfully')
        return render(request, 'signin.html')