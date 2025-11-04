from django.shortcuts import render

# Create your views here.
def whoamI(request):
    return render(request, 'index.html')