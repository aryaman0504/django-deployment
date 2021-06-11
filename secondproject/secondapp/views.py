from django.shortcuts import render
from django.http import HttpResponse
from secondapp.models import User
# Create your views here.
def index(request):
    return HttpResponse("Hi we are here")

def user(request):
    users_list = User.objects.order_by('first_name')
    user_dict = {'records':users_list}
    return render(request,"secondapp/index.html",context = user_dict)
