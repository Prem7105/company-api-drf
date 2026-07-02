from django.http import HttpResponse

def home_page(request):
    print("home page requeste")
    return HttpResponse("This is home page")
