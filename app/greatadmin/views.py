from django.shortcuts import render, redirect, reverse, HttpResponse
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.clickjacking import xframe_options_exempt
from .models import Animal
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage
import random,string
import time
from ..users.models import User
from ..shop.models import ListInfo, SaleInfo
from ..cultivation.models import CultivationInfo
import datetime


class Index(View):
    @method_decorator(login_required(login_url='/users/login/'), name='dispatch')
    def get(self, request):
        today = datetime.datetime.now().date()
        im = Animal.objects.filter().order_by("-create_time")[:9]
        money = ListInfo.objects.filter()
        m = 0
        for i in money:
            m = m+i.price
        ic = Animal.objects.filter(is_turn__isnull=True).count()
        oc = Animal.objects.filter(is_turn__isnull=False).count()
        lc = CultivationInfo.objects.filter().count()
        ##
        now_time = datetime.datetime.now()

        return render(request, "index.html", locals())

class Editpwd(View):
    @method_decorator(login_required(login_url='/users/login/'), name='dispatch')
    def get(self, request):
        return render(request, "pages_edit_pwd.html")

class Edieprofile(View):
    @method_decorator(login_required(login_url='/users/login/'), name='dispatch')

    def get(self, request):
        return render(request, "pages_profile.html")


class AnimalInfo(View):
    @xframe_options_exempt
    @method_decorator(login_required(login_url='/users/login/'), name='dispatch')
    def get(self, request):

        mes = Animal.objects.filter().order_by("-create_time")
        ######################################

        paginator = Paginator(mes, 9)

        # 获取 url 后面的 page 参数的值, 首页不显示 page 参数, 默认值是 1
        page = request.GET.get('page', 1)
        currentPage = int(page)
        try:
            mess = paginator.page(page)
        # todo: 注意捕获异常
        except PageNotAnInteger:
            # 如果请求的页数不是整数, 返回第一页。
            mess = paginator.page(1)
        except InvalidPage:
            # 如果请求的页数不存在, 重定向页面
            return HttpResponse('找不到页面的内容')
        except EmptyPage:
            # 如果请求的页数不在合法的页数范围内，返回结果的最后一页。
            mess = paginator.page(paginator.num_pages)

        ######################################

        return render(request, "pages_doc_animail.html", locals())  # locals () 函数会以字典类型返回当前位置的全部局部变量。

class AddAnimal(View):
    @method_decorator(login_required(login_url='/users/login/'), name='dispatch')
    def get(self, request):
        return render(request, "pages_guide_addanimal.html")
    def post(self, request):
        user = request.POST.get('user')
        hid = request.POST.get('hid') #
        address = request.POST.get('address')
        aclass = request.POST.get('aclass')
        fa_mo = request.POST.get('fa_mo')
        num = request.POST.get('num')
        license = request.POST.get('license')
        if (len(address) == 0) or (len(aclass) == 0) or (len(fa_mo) == 0) or (len(num) == 0) or (len(license) == 0) or (len(hid) == 0) or (len(user) == 0):
            msg = "数据不全，动物信息录入失败"
            return render(request, "pages_guide_addanimal.html", {"msg": msg})
        else:
            time_array = time.localtime()#
            format_time = time.strftime("%Y%m%d", time_array)[2:8]#
            suiji = "".join(random.sample(string.digits,8))#
            id = int(str(hid) + str(address) + suiji + format_time)#
            Animal.objects.create(
                address=address,
                aclass=aclass,
                fa_mo=fa_mo,
                num=num,
                license=license,
                id=id,
                clgroup=user,
            )
            msg = "动物信息录入成功"
            return render(request, "pages_guide_addanimal.html", {"msg":msg})

class AddAnimalTwo(View):
    @method_decorator(login_required(login_url='/users/login/'), name='dispatch')
    def get(self, request):
        return render(request, "pages_doc_addanimal.html")
    def post(self, request):
        user = request.POST.get('user')
        u = User.objects.get(id=user)

        hid = request.POST.get('hid')
        address = request.POST.get('address')
        aclass = request.POST.get('aclass')
        fa_mo = request.POST.get('fa_mo')
        num = request.POST.get('num')
        license = request.POST.get('license')
        if (len(address) == 0) or (len(aclass) == 0) or (len(fa_mo) == 0) or (len(num) == 0) or (len(license) == 0) or (len(hid) == 0) or (len(user) == 0):
            msg = "数据不全，动物信息录入失败"
            return render(request, "pages_doc_addanimal.html", {"msg": msg})
        else:
            time_array = time.localtime()
            format_time = time.strftime("%Y%m%d", time_array)[2:8]
            suiji = "".join(random.sample(string.digits, 8))
            wb = (int(suiji[-1]) + int(format_time[-1])) % 3
            id = int(str(hid) + str(address) + suiji + format_time + str(wb))
            Animal.objects.create(
                address=address,
                aclass=aclass,
                fa_mo=fa_mo,
                num=num,
                license=license,
                id=id,
                clgroup=u,
            )
            msg = "动物信息录入成功"
            return render(request, "pages_doc_addanimal.html", {"msg":msg})


class CultivationVision(View):
    @method_decorator(login_required(login_url='/users/login/'), name='dispatch')
    def get(self, request):
        money = ListInfo.objects.filter()
        m = 0
        for i in money:
            m = m + i.price
        if Animal.objects.filter(dead=True).count() == 0:
            i = 0
        else:
            i = Animal.objects.filter(dead=True).count() / Animal.objects.filter(dead=True).count()
        return render(request, "js_chartjs_cultivation.html", locals())

class SlaughterVision(View):
    @method_decorator(login_required(login_url='/users/login/'), name='dispatch')
    def get(self, request):
        return render(request, "js_chartjs_slaughter.html")

class MarketVision(View):
    @method_decorator(login_required(login_url='/users/login/'), name='dispatch')
    def get(self, request):
        return render(request, "js_chartjs_market.html")

class ShopVision(View):
    @method_decorator(login_required(login_url='/users/login/'), name='dispatch')
    def get(self, request):
        money = ListInfo.objects.filter()
        m = 0
        for i in money:
            m = m + i.price
        money2 = SaleInfo.objects.filter()
        n = 0
        for i in money:
            n = n + i.price

        x = ListInfo.objects.filter().count()
        g = SaleInfo.objects.filter().count()
        return render(request, "js_chartjs_shop.html", locals())



class DelAnimal(View):
    def get(self, request, aid):  # 超级链接是get请求，则只写get函数就可以了
        a = Animal.objects.get(id=aid)  # 要么0要么1条 (第一个id是：数据库表格里字段的名字，第二个id是：参数传递过来的具体的值）
        a.delete()
        return redirect(reverse("greatadmin:animalinfo"))

def info_multi_del(request):
    variables = request.GET['id']
    for item in variables.split(','):
        info = get_object_or_404(Animal, pk=int(item))
        info.delete()
    return redirect(reverse("greatadmin:animalinfo"))