from django.shortcuts import render
from django.http import HttpResponse
from . import try1
# Create your views here.
def home(request):
    #return HttpResponse("Maps 1.1")
    return render(request,"home.html")

def locs(request):
    try:
        l1=request.GET["l01"]
        l2=request.GET["l02"]
        l3=request.GET["l03"]
        l4=request.GET["l04"]
        l5=request.GET["l05"]
        l6=request.GET["l06"]
        l7=request.GET["l07"]
        l8=request.GET["l08"]
        l9=request.GET["l09"]
        l10=request.GET["l10"]
        l=[]
        if len(l1)>1:
            l.append(l1)
        if len(l2)>1:
            l.append(l2)
        if len(l3)>1:
            l.append(l3)
        if len(l4)>1:
            l.append(l4)
        if len(l5)>1:
            l.append(l5)
        if len(l6)>1:
            l.append(l6)
        if len(l7)>1:
            l.append(l7)
        if len(l8)>1:
            l.append(l8)
        if len(l9)>1:
            l.append(l9)
        if len(l10)>1:
            l.append(l10)
        print("="*25,">",l)
        try1.codegen(l)
    except:
        print("="*25,">","GET ERROR")
        
    try:
        return render(request,"index.html")
    except:
        return HttpResponse("Maps 1.1")