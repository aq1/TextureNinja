from django.http import HttpResponse


def texture_list(request):
    return HttpResponse('texture_list')


def texture_detail(request, pk):
    return HttpResponse('texture_detailt')
