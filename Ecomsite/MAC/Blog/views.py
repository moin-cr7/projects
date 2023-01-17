from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # return HttpResponse("index blog ")
    return render(request,'Blog/index.html')

