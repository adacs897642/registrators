from django.shortcuts import render, get_object_or_404

from .models import Lpu, Object, Error, Documents


def home(request):
    objects_lpu = Lpu.objects.all()
    return render(request, 'objects/home.html', {'objects_lpu': objects_lpu})


def detail(request, lpu_id):

    lpu = Lpu.objects.filter(id=lpu_id)[0]

    objects = Object.objects.filter(lpu_id=lpu_id).order_by('project')
    error = Error.objects.order_by('obj_id').distinct('obj_id')
    print(error)
    return render(request,'objects/lpu.html',{'objects':objects, 'lpu_id':lpu_id,'error':error, 'lpu':lpu})


def content(request, lpu_id, objects_id):
    error = Error.objects.filter(obj_id=objects_id)
    objects = Object.objects.filter(lpu_id=lpu_id).order_by('project')[0]
    documents = Documents.objects.filter(obj_id=objects_id)
    return render(request,'objects/content.html',{'error':error, 'objects':objects, 'documents': documents})
