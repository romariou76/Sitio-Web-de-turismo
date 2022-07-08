from django.shortcuts import render

from django.contrib import messages



def base(request):
    return render(request, 'WebPayments/base.html')

def index(request):
    return render(request, 'WebPayments/index.html')





        

