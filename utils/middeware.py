from django.http import HttpResponse, HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin
from backweb.models import User


class LoginStatusMiddleware(MiddlewareMixin):
    def process_request(self, request):
        print('test1 request')
        # 在访问登录和注册的时候，不需要做以下的登录校验功能
        if request.path in ['/login/']:
            return None

        # 登录校验
        # token = request.COOKIES.get('token')
        # if token:
        #     token_user = TokenUser.objects.filter(token=token).first()
        #     if token_user:
        #         # process_request中可以不写return，或者写return None
        #         return None
        #     else:
        #         return HttpResponseRedirect('/login/')
        # else:
        #     return HttpResponseRedirect('/login/')

        # session校验
        # 1. 获取cookie中的session值
        # 2. 查询django_session表中的session_key字段，
        # 查询的到数据，则获取sesson_data中存入的键值对
        user_id = request.session.get('user_id')
        if user_id:
            # 向request.user中赋值，赋值为当前的登录系统的用户对象
            user = User.objects.get(pk=user_id)
            request.user = user
            return None
        else:
            return HttpResponseRedirect('/login/')

    def process_response(self, request, response):
        return response
