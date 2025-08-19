from django.conf import settings
from django.shortcuts import render
def home_view(request):
    name=getattr(settings,"RESTAURANT_NAME","Spice Garden")

    return render(request,'home.html',{restauant_name":restaurant_name})
    

# Create your views here.
