from django.http import HttpResponse
def about(request):
    #  how to html work 
    return HttpResponse(""" <a href="https://www.w3schools.com/tags/tag_a.asp"> Click Here </a> <br> <a href="https://www.youtube.com"> Youtube Here </a>""")  
    