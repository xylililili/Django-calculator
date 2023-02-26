from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

def test_mycal(request):
    if request.method == "GET":
        return render(request, "mycal.html")
    elif request.method == "POST":
        x = int(request.POST.get('x', 0))
        y = int(request.POST.get('y', 0))
        op = request.POST['op']

        result = 0
        if op == 'add':
            result = x+y
        elif op == 'sub':
            result = x-y
        elif op == 'mul':
            result = x*y
        elif op == 'div':
            result = x/y

        #dic =  {'x':x, 'y':y, 'op':op}
        return render(request, 'mycal.html', locals())