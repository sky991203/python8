from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Address
from django.utils import timezone
from django.urls import reverse
from .models import Board 
from django.db.models import Q

def index(request):
    #return HttpResponse("<center><h3>형수의 안녕 장고^^</h3></center>")
    template = loader.get_template('index.html')
    #return HttpResponse(template.render()) # 나중에 session 변수값을 가져오지 못함
    return HttpResponse(template.render({},request)) #request 받으므로 확장성이 좋음.

def list (request):
    template = loader.get_template('list.html')
    addresses = Address.objects.all().values()
    #addresses = Address.objects.filter(name='홍길동').values()
    #views.py 수정
    #addresses = Address.objects.all().values()
    #addresses = Address.objects.filter(name='홍길동').values()
    #addresses = Address.objects.filter(name='홍길동', addr='한양시').values()
    #addresses = Address.objects.filter(name='홍길동').values() | Address.objects.filter(addr='부산시').values()
    #addresses = Address.objects.filter(Q(name='홍길동')|Q(addr='부산시')).values()
    #addresses = Address.objects.filter(name__startwith='이').values()
    #addresses = Address.object.all().order_by('-name').values() = desc
    #addresses = Address.object.all().order_by('-name','addr', '-id').values()
    
    # 효과) select * from address where name='홍길동';
    # 효과) select * from address where name='홍길동' and addr='한양시';
    # 효과) select * from address where name='홍길동' or addr='부산시';
    # 효과) select * from address where NAME like '이%'
    context = {
        'addresses' : addresses,
    }
    return HttpResponse(template.render(context,request)) 

def write(request):
    template = loader.get_template('write.html')
    return HttpResponse(template.render({},request)) 

def write_ok(request):
    x = request.POST['name']
    y = request.POST['addr']
    nowDatetime = timezone.now().strftime('%Y-%m-%d %H:%M:%S')
    address = Address(name=x, addr=y, rdate=nowDatetime)
    address.save()
    return HttpResponseRedirect(reverse('list'))

def delete(request, id):
    address = Address.objects.get(id=id)
    address.delete()
    return HttpResponseRedirect(reverse('list'))

def update(request, id):
    template = loader.get_template('update.html')
    address = Address.objects.get(id=id)
    context = {
            'address' : address,
        }
    return HttpResponse(template.render(context,request)) 

def update_ok(request, id):
    x = request.POST['name']
    y = request.POST['addr']  
    address = Address.objects.get(id=id)
    address.name = x 
    address.addr = y
    nowDatetime = timezone.now().strftime('%Y-%m-%d %H:%M:%S') #최근 수정 날짜 옵션
    address.rdate = nowDatetime #최근 수정 날짜 옵션
    address.save()
    return HttpResponseRedirect(reverse('list'))

# def board_list(request):
#     boards = Board.objects.all()
#     return render(request, 'board/list.html', {'boards': boards})

def board_list(request):
    template = loader.get_template('board/list.html')
    #boards = Board.objects.all().values()
    context = {
        #'boards': boards,
    }
    return HttpResponse(template.render(context, request))

def board_write(request):
    template = loader.get_template('board/write.html')
    return HttpResponse(template.render({}, request))

