from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from backweb.Artform import AddArtForm
from backweb.models import User, Article


def login(request):
        if request.method == 'GET':
                # GET 访问http://127.0.0.1:8000/register/
                return render(request, 'backweb/login.html')

        if request.method == 'POST':
            # 1. 获取登录提交的用户名和密码
                username = request.POST.get('username')
                password = request.POST.get('password')
            # 2. 查询数据库中用户名和密码对应的用户对象
                user = User.objects.filter(username=username,
                                           password=password).first()
        if not user:
                err = '用户名或者密码错误'
                return render(request, 'backweb/login.html', {'err': err})
        # 3. 登录操作
        # 给与登录成功的标识符（令牌），存在于cookie中
        # res = HttpResponseRedirect('/my_index/')
        # token = get_cookie_token()
        # res.set_cookie('token', token, 6000)
        # # 向TokeUser表中插入或更新数据
        # token_user = TokenUser.objects.filter(user=user).first()
        # # token_user = TokenUser.objects.filter(user_id=user.id).first()
        # if token_user:
        #     token_user.token = token
        #     token_user.save()
        # else:
        #     TokenUser.objects.create(token=token, user=user)

        # 3. 使用session实现登录操作
        # 3.1 向cookie中设置sessionid值，value为随机字符串
        # 3.2 向django_session表中存入sessionid值，并保持键值对
        request.session['user_id'] = user.id
        # 4. 跳转到首页
        res = HttpResponseRedirect('/backweb/index/')
        return res


def index(request):
    return render(request, 'backweb/index.html')


def article(request):
    return render(request, 'backweb/article.html')


def add_article(request):
    if request.method == 'GET':
        return render(request, 'backweb/add_article.html')

    if request.method == 'POST':
            form = AddArtForm(request.POST, request.FILES)
            if form.is_valid():
                title = form.cleaned_data['title']
                desc = form.cleaned_data['desc']
                content = form.cleaned_data['content']
                icon = form.cleaned_data['icon']
                Article.objects.create(title=title, desc=desc, content=content, icon=icon)
                # Article.objects.create(title=request.POST.get('title'),
                #                        content=request.POST.get('content'),
                #                        desc=request.POST.get('desc'))
                return HttpResponseRedirect(reverse('back_web:article_list'))

            else:
                return render(request, 'backweb/add_article.html', {'form': form})
