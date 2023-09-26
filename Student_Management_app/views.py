from django.shortcuts import render

# Create your views here.
def showDemoPage(request):
    return render(request, 'demo_page.html')