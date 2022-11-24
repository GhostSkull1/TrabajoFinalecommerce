from django.shortcuts import render
from .models import categoria

# Create your views here.
def home(request):
    data=categoria.objects
    return render(request,'index.html')

# categoria
def category_list(request):
    return render(request,'category_list.html')