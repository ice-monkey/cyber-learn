from django.shortcuts import render

# Create your views here.
def cybersite(request):
    return render(request, 'index.html', {})
