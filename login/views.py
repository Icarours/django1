from django.shortcuts import render
from django.shortcuts import HttpResponse
from login import models

# Create your views here.
# 顶部增加一个空列表
user_list = []


# 第一个参数必须是request,名字可以改,但是最好不要改,这是潜规则.request参数封装了用户所有的请求内容
def index(request):
    # 不能直接返回字符串,必须由HttpResponse封装起来
    # return HttpResponse('hello world!!!')
    # render方法使用数据字典和请求元数据,渲染一个指定的HTML模板.其多个参数中,第一个参数必须是request,第二个参数是模板
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # 将数据爆粗难道数据库
        models.UserInfo.objects.create(user=username, pwd=password)
        print(username, password)
        # 将用户名和面保存到一个字典中
        # temp = {'user': username, 'pwd': password}
        # 将字典添加到列表中
        # user_list.append(temp)
        # 将user_list列表作为上下文参数供render渲染到HTML
    # 从数据库读取所有数据
    user_list = models.UserInfo.objects.all()
    return render(request, 'index.html', {'data': user_list})
