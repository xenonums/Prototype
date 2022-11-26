from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render,redirect,reverse
from .models import User
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from app.users.models import Code
# Create your views here.
import uuid
import hashlib

def get_random_str():
    uuid_val = uuid.uuid4()
    uuid_str = str(uuid_val).encode("utf-8")
    md5 = hashlib.md5()
    md5.update(uuid_str)
    return md5.hexdigest()

snum = ''
class log_in(View):
    def get(self, request):
        return render(request, "login.html")
    def post(self, request):
        if 'lg' in request.POST:
            usn = request.POST.get("username")
            pwd = request.POST.get("password")

            url = request.GET.get("next", reverse("greatadmin:index"))
            # 地址栏传递方式为get方式
            user = authenticate(username=usn, password=pwd)
            if user:
                # 系统会将user信息附加到request对象后传递到前端
                # request.user前端可调用
                # user.is_authenticated判断是否登录用此属性，返回真或假两种情况
                login(request, user)
                return redirect(url)
            else:
                msg = "用户名或密码错误！"
                messages.error(request, msg)
                return render(request, "login.html")

        elif 'code' in request.POST:
            email = request.POST.get("e_mail")
            num = get_random_str()
            subject = '欢迎使用智慧养殖管理系统'
            message = '欢迎注册！你的激活码为：' + num
            send_mail(
                subject=subject,
                message=message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[email],
            )
            global snum
            snum = num
            msg = "激活码已发送"
            messages.error(request, msg)
            return redirect(reverse("users:login"))

        else:
            usn = request.POST.get("user_name")
            pwd = request.POST.get("pass_word")
            email = request.POST.get("e_mail")
            code = request.POST.get("co_de")

            n = User.objects.filter(username=usn).count()
            if n == 1:
                msg = "用户名已存在！"
                messages.error(request, msg)
                return render(request, "login.html")
            elif snum != code or snum is None:
                msg = "激活码为空或错误"
                messages.error(request, msg)
                return render(request, "login.html")
            else:
                user = User.objects.create_user(usn, email, pwd)
                if user:
                    return redirect(reverse("users:login"))
                else:
                    msg = "注册失败！"
                    messages.error(request, msg)
                    return render(request, "login.html")

class log_out(View):
    def get(self, request):
        logout(request)
        return redirect(reverse("users:login"))
