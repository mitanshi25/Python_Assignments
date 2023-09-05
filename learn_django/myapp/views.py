from django.shortcuts import render, HttpResponse


# Create your views here.
def index (requests):
    context = {
        'variable': 'this is sent'
    }
    
    return render(requests, 'index.html', context )
    # return HttpResponse("this is the home page")

def about (requests):
        return render(requests, 'about.html' )

    # return HttpResponse("this is the about page")

def services (requests):
          return render(requests, 'sevices.html' )

    # return HttpResponse('i am the service page')

def contact(requests):
       return render (requests, 'contact.html')
