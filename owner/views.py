from django.shortcuts import render
from owner.models import OwnerInfo

# Create your views here.
def ownerview(request):
    context ={
        'detail':OwnerInfo.objects.filter(user_id=request.user.id),
    }
    return render(request, 'owner_dashboard.html',context)