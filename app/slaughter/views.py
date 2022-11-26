from django.shortcuts import render, HttpResponse, reverse, redirect
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from ..greatadmin.models import Animal
from ..users.models import User
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage
from .models import Slaughter, SlaughterInfo
from django.db.models import Q
# Create your views here.
class AddSlaughter(View):
    @method_decorator(login_required(login_url='/users/login/'), name='dispatch')
    def get(self, request, anid):
        # return redirect(reverse("slaughter:addslaughter"))
         return render(request, "forms_addslaughter.html",{"anid":anid})
    def post(self, request, anid):
        n = request.POST.get('name')
        name = User.objects.get(id=n)

        a = request.POST.get('aid')
        patch = request.POST.get('patch')
        safe = request.POST.get('safe')
        license = request.POST.get('license')
        if (len(n) == 0) or (len(a) == 0) or (len(patch) == 0) or (len(safe) == 0) or (len(license) == 0):
            msg = "数据不全，屠宰信息录入失败"
            return render(request, "forms_addslaughter.html", {"anid":anid,"msg":msg})
        else:
            is_sl = Animal.objects.get(id=a)
            is_sl.is_sl = True
            is_sl.save()

            slgroup = Animal.objects.get(id=a)
            slgroup.slgroup = name
            slgroup.save()

            ani = Animal.objects.get(id=a)  # !!!!!!!!!!!
            patchs = patch.split("/")
            for p in patchs:
                Slaughter.objects.create(
                    patch=p,
                    aeid=name,
                )

                si = Slaughter.objects.last()
                SlaughterInfo.objects.create(
                    safe=safe,
                    license=license,
                    aid=ani,
                    sid=si,
                    user=name,
                )
            msg = "屠宰信息录入成功"
            return render(request, "forms_addslaughter.html", {"anid":anid,"msg":msg})

class SlaughterBoard(View):
    @method_decorator(login_required(login_url='/users/login/'), name='dispatch')
    def get(self, request):

        sl = SlaughterInfo.objects.filter().order_by('-create_time')
        paginator = Paginator(sl, 9)

        # 获取 url 后面的 page 参数的值, 首页不显示 page 参数, 默认值是 1
        page = request.GET.get('page', 1)
        currentPage = int(page)
        try:
            sli = paginator.page(page)
        # todo: 注意捕获异常
        except PageNotAnInteger:
            # 如果请求的页数不是整数, 返回第一页。
            sli = paginator.page(1)
        except InvalidPage:
            # 如果请求的页数不存在, 重定向页面
            return HttpResponse('找不到页面的内容')
        except EmptyPage:
            # 如果请求的页数不在合法的页数范围内，返回结果的最后一页。
            sli = paginator.page(paginator.num_pages)

        return render(request, "pages_doc_slaughter.html", locals())

class AnimalToKill(View):
    @method_decorator(login_required(login_url='/users/login/'), name='dispatch')
    def get(self, request):

        mes = Animal.objects.filter(Q(is_turn=True) & Q(is_sl=False)).order_by('-create_time')

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

        return render(request, "pages_doc_animail2kill.html", locals())