from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from .models import Disposal
from django.utils import timezone
from django.conf import settings
from django.core.files.storage import FileSystemStorage


def disposal(request):
    disposals=Disposal.objects.all().order_by('-id')
    return render(request, 'disposal.html', {'disposals':disposals})

def detail2(request, disposal_id):
    disposal_detail=get_object_or_404(Disposal, pk=disposal_id)
    return render(request, 'detail2.html', {'disposal':disposal_detail})

def new2(request):
    return render(request, 'new2.html')

def create2(request):
    disposal=Disposal()
    disposal.title=request.POST['title']
    disposal.name=request.POST['name']
    disposal.writer=request.POST['writer']
    disposal.item=request.POST['item']
    disposal.address=request.POST['address']
    disposal.phone=request.POST['phone']
    disposal.etc=request.POST['etc']
    disposal.photo=request.FILES['photo']
    disposal.pub_date=timezone.datetime.now()
    disposal.save()  
    return redirect('/disposal/'+str(disposal.id))

def edit2(request, disposal_id):
    disposal=get_object_or_404(Disposal, pk=disposal_id)
    return render(request, 'edit2.html',{'disposal':disposal})

def update2(request, disposal_id):
    disposal=get_object_or_404(Disposal, pk=disposal_id)
    disposal.title=request.POST['title']
    disposal.name=request.POST['name']
    disposal.writer=request.POST['writer']
    disposal.item=request.POST['item']
    disposal.address=request.POST['address']
    disposal.phone=request.POST['phone']
    disposal.etc=request.POST['etc']
    disposal.photo=request.FILES['photo']
    disposal.pub_date=timezone.datetime.now()
    disposal.save()
    return redirect('/disposal/'+str(disposal.id))

def delete2(request, disposal_id):
    disposal=get_object_or_404(Disposal, pk=disposal_id)
    disposal.delete()
    return redirect('disposal')



