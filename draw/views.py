from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
# Create your views here.
from draw.models import Users

import random


def index(request):
    return render(request,'index.html')

#获取用户
def person(request):
    list = Users.objects.all()
    return render(request,'person.html',{'list':list})


#添加名单
def add(request):
    if request.method=='POST':
        name = request.POST.get('name')
        # print(name)
        # 判断姓名不能为空
        if not name:
            return JsonResponse({'code':400,'msg':'请填写姓名'})
        is_name = Users.objects.filter(name=name).count()
        if is_name:
            return JsonResponse({'code':400,'msg':'该人已存在'})

        userModel = Users()
        userModel.name = name
        userModel.type = 0
        userModel.save()

        userna = Users.objects.filter(name=name).count()
        # print(userna)
        # exit()
        return JsonResponse({'code':0,'msg':'成功'})
    else:
        return render(request,'add.html')




# 获取中奖名单
def get_prize(request):
    Users.objects.all().update(type=0)
    if request.method=='POST':
        # 获取参数
        type = request.POST.get('type')
        type = int(type)
        list = Users.objects.values('name').filter(type=0)
        # print(list)
        if list:
            list_len = len(list)
            list_a=[]
            for v in list:
                # print(v['name'])
                list_a.append(v['name'])

            # print(list_a)
            if type==1:
                num = 1
            elif type==2:
                num = 2
            elif type==3:
                num = 3

            i=0
            res = []
            while i<num:
                key=random.randint(0,list_len-1)
                if list_len>key:
                    res.append(list_a[key])
                    list_a.pop(key)
                i = i+1
                list_len = len(list_a)
            Users.objects.filter(name__in=res).update(type=type)
            return JsonResponse({'code': 0, 'msg': '成功', 'result': res})
        else:
            return JsonResponse({'code': 100, 'msg': '奖品送完'})




# 一等奖
def get_first_prize(request):
    if request.method == 'POST':
        return JsonResponse({'code':0,'msg':'成功','result':'result'})


# 二等奖
def get_second_prize(request):
    return JsonResponse({'code':0,'msg':'成功','result':'result'})

# 三等奖
def get_third_prize(request):
    return JsonResponse({'code':0,'msg':'成功','result':'result'})