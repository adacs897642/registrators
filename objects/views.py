from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Lpu, Object, Error, Documents

from .forms import ErrorsForm, DocumentForm, LpuForm, ObjectForm


def home(request):
    objects_lpu = Lpu.objects.all()
    form = LpuForm()

    if request.method == 'POST':
        if 'btn_add' in request.POST:
            form = LpuForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(request.path)

    return render(request, 'objects/home.html', {'objects_lpu': objects_lpu, 'form':form})


def detail(request, lpu_id):
    lpu = get_object_or_404(Lpu, pk=lpu_id)
    objects = Object.objects.filter(lpu_id=lpu_id).order_by('project')
    error = Error.objects.order_by('obj_id').distinct('obj_id')

    form  = ObjectForm(initial={
        'lpu' : lpu_id,
    })

    if request.method == 'POST':
        if 'btn_add' in request.POST:
            form = ObjectForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(request.path)

    return render(request,'objects/lpu.html',{'objects':objects,
                                              'lpu_id':lpu_id,
                                              'error':error,
                                              'lpu':lpu,
                                              'form':form
                                              })


def content(request, lpu_id, objects_id):
    error = Error.objects.filter(obj_id=objects_id)
    objects=get_object_or_404(Object, pk=objects_id)
    lpu = get_object_or_404(Lpu, pk=lpu_id)
    documents = Documents.objects.filter(obj_id=objects_id)



    if request.method == 'GET':
        form_document = DocumentForm(initial={
            'obj': objects_id
        })
        form_error = ErrorsForm(initial={
            'obj': objects_id,
        })

    if request.method == 'POST':

        if 'btn_add_error' in request.POST:
            form_error = ErrorsForm(request.POST)

            if form_error.is_valid():
                form_error.save()
                return HttpResponseRedirect(request.path)
        else:
            form_error = ErrorsForm(initial={
                'obj': objects_id,
            })
        if 'btn_upload_file' in request.POST:

            form_document = DocumentForm(request.POST, request.FILES)

            if form_document.is_valid():
                form_document.save()
                return HttpResponseRedirect(request.path)

        else:
            form_document = DocumentForm(initial={
                'obj': objects_id
            })

    return render(request,'objects/content.html',
                  {'error':error,
                   'objects':objects,
                   'documents': documents,
                   'lpu':lpu,
                   'form_error':form_error,
                   'form_document': form_document,
                   })
