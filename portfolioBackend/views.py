from django.http import HttpResponse

def saludo(request):
    return HttpResponse("Hola mundo")

def despedida(request):
    return HttpResponse("adios")

def adulto(request, edad):
    if (edad>=18):
        return HttpResponse("mayor")
    else:
        return HttpResponse("menor")