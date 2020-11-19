from django.shortcuts import render
import requests
from Interpolation import templates
from Metodos.lagrange import lagrange
# Create your views here.

def lagrangeP(request):
    if 'x' in request.POST:
        x = request.POST.get('x')
        y = request.POST.get('y')
        x = x.split(',')
        y = y.split(',')

        for i in range(len(x)):
            x[i]= float(x[i])
        
        for i in range(len(y)):
            y[i]= float(y[i])
        print(x,y)
        data = lagrange(x,y)
        return render(request, "lagrange.html",{'polinomio':data})
    return render(request, "lagrange.html",{'polinomio':''})