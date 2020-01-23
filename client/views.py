from django.shortcuts import render

# Create your views here.
def clientview(request):
    return render(request,'client_dashboard.html')
