from django.http import HttpResponse

def index(request):
    return HttpResponse("Hey there partner! <br/> <a href='/myapp/about/'>About</a>.")
    
def about(request):
    return HttpResponse("Hello, world. Here is the about page.<a href='/myapp/'>Index</a>")
