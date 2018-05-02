from django.shortcuts import render
from myweb.models import Users
from myweb.models import music
# Create your views here.
def myweb_index(request):
    myweb_list=Users.objects.all()  #获=获取所有数据
    return render(request,'index.html',{'myweb_list':myweb_list})# 返回index.html的页面


def show_data(request):
    show_list=music.objects.all()
    #for f in show_list:
       # f.title_name=f.title_name.encode("utf-8")
    return render(request,'music.html',{'show_list':show_list})