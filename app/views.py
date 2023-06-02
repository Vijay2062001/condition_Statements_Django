from django.shortcuts import render

# Create your views here.

def jinja(request):
    d={'a':20,'b':30}
    return render(request,'jinja.html',context=d)


def jinja2(request):
    d={'a':30}
    return render(request,'jinja1.html',context=d)


def jinja3(request):
    d={'a':20,'b':30}
    return render(request,'jinja4.html',context=d)

def elifcon(request):
    d={'a':20,'b':80,'c':40}
    return render(request,'elif.html',context=d)

def nestedif(request):
    d={'a':10,'b':20,'c':30,'d':40}
    return render(request,'nested.html',context=d)