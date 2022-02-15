# i have created this file
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

# <----------------------------------- lecture-10-12 for backend code -------------------->
def analyze(request):
    djtext=request.GET.get('text','defalt')
    removepunc=request.GET.get('removepunc','off')
    capfrist=request.GET.get('capfrist','off')
    newlineremover=request.GET.get('newlineremover','off')
    spaceremover=request.GET.get('spaceremover','off')
    charcount=request.GET.get('charcount','off')
    # print(removepunc)
    # print(djtext)
    
    if removepunc=='on':
        # analyzed=djtext
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=" "
        for char in djtext:
            if char not in punctuations:
                analyzed+=char
        params={'purpose':'Remove Puntuation','Analized_text':analyzed}
        djtext=analyzed
        # return render(request, 'analyze.html',params)

#  uppercase cahrecter 
    if( capfrist=='on'):
        analyzed=" "
        for char in djtext:
            analyzed= analyzed+char.upper()
        params={'purpose':'Captalized charecter','Analized_text':analyzed}
        djtext=analyzed
        # return render(request, 'analyze.html',params)
# new line remover 
    if(newlineremover=='on'):
        analyzed=" "
        for char in djtext:
            if char != '\n' and char != '\r':
                analyzed= analyzed+char
        params={'purpose':'Newline Remover','Analized_text':analyzed}
        djtext=analyzed
        # return render(request, 'analyze.html',params)

# Space remover in sentance
    if(spaceremover=='on'):
        analyzed=" "
        for index,char in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index+1] ==" "):
               
                analyzed= analyzed+char
        params={'purpose':'Space Remover ','Analized_text':analyzed}
        djtext=analyzed
        # return render(request, 'analyze.html',params)

#char count in programe
    if(charcount=="on"):
        analyzed=0
        for char in djtext:
            analyzed+=1
        params={'purpose':'char count','Analized_text':analyzed}
        djtext=analyzed
        # return render(request, 'analyze.html',params)

# when you are nothing selected any chek box then this line code will be execute 
    if ( removepunc!='on' and capfrist!='on' and newlineremover!='on' and spaceremover!='on' and charcount!="on"):
        return HttpResponse("<h1> Eror:404 </h1> plese! Select any opration " )
    return render(request, 'analyze.html',params)   


# <-----------------------------for templates lecture-8 ------------------------>

# def index(request):
#     info={ 'name':'Vaseem','place':'Nepal'}
#     return render(request, 'index.html',info)



# def capfrist(request):
#     return HttpResponse("Captalize frist")

# def newlineremove(request):
#     return HttpResponse("remove new line")

# def spaceremove(request):
#     return HttpResponse("Space remove <a href='capfrist'>back</a>")

# def charcount(request):
#     return HttpResponse("Charecter count <a href='/'>back</a>")


# def about(request):
#     #  how to html work 
#     return HttpResponse(""" <h4> about my self <h4> """)  

# <----------------- Video lecture-7   "pip line" --------------------------------->

# def home(request):
#     return HttpResponse("Home")


# <------------------------- lecture number-9  ------------------->
# def removepunc(request):
#     print(request.GET.get('text','defalt'))
#     return HttpResponse("remove punc")
# < ------------- end lect-9 -------------------------->