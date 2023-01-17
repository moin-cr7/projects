#this is my django file
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'index.html')
def analyse(request):

    djtext=request.GET.get("text","default")
    removepunc=request.GET.get('removepunc','off')
    uppercase=request.GET.get("upercase","off")
    newline=request.GET.get("newlineremover","off")
    Spaceremover=request.GET.get("spaceremover","off")
    charcounter=request.GET.get("charcounter","off")

    if removepunc=="on":
        analysed = ""
        punctuation = '''<>,./?:;"'[]{}()""!@#$%^&*|\-_*'''
        for char in djtext:
            if char not in punctuation:
                analysed=analysed+char
        p={'purpose':'remove puctuations','analyser_text':analysed}
        djtext=analysed

    if (uppercase == "on"):
        analysed = ""
        for char in djtext:
            analysed = analysed + char.upper()
        p = {'purpose': 'UPPERCASE', 'analyser_text': analysed}
        djtext=analysed

    if (newline == "on"):
        analysed = ""
        for char in djtext:
            if (char != "\n" and char!="\r"):
                analysed = analysed + char
        p = {'purpose': 'Remove newline', 'analyser_text': analysed}
        djtext=analysed

    if (Spaceremover == "on"):
        analysed = ""
        for index,char in enumerate(djtext):
            if not(djtext[index]==" "  and djtext[index+1]==" "):
                analysed = analysed + char
        p = {'purpose': 'SPACEREMOVER', 'analyser_text': analysed}
        djtext=analysed

    if (charcounter == "on"):
        count=0
        for char in djtext:
            if char!=0:
                count=count+1
        return HttpResponse(count)
        p = {'purpose': 'Character counting', 'analyser_text': analysed}

    if(charcounter != "on" and Spaceremover != "on" and newline != "on" and uppercase != "on" and removepunc!="on" ):
        return HttpResponse("ERROR")
    return render(request, 'analyse.html', p)