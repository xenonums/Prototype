from django.shortcuts import render,redirect,reverse
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.clickjacking import xframe_options_exempt
from .models import Fodder, FodderInfo,Vaccine,VaccineInfo , CultivationInfo, QuarantineInfo, TurnInfo
from ..greatadmin.models import Animal
from ..users.models import User
from django.db.models import Q
class CultivationInfoBoard(View):
    @method_decorator(login_required(login_url='/users/login/'), name='dispatch')
    def get(self, request):
        ci = CultivationInfo.objects.filter()
        return render(request, "pages_doc_cultivation.html", {"ci":ci})

class FodderBoard(View):
    @method_decorator(login_required(login_url='/users/login/'), name='dispatch')
    def get(self, request):
        mes = CultivationInfo.objects.filter(fiid__isnull=False)
        mess = Fodder.objects.filter()
        messi = FodderInfo.objects.filter()
        return render(request, "pages_doc_fodder.html", locals())

class AddFodder(View):
    @method_decorator(login_required(login_url='/users/login/'), name='dispatch')
    @xframe_options_exempt
    def get(self, request):
        return render(request, "pages_doc_addfodder.html")
    def post(self, request):
        user = request.POST.get('user')
        u = User.objects.get(id=user)
        name = request.POST.get('name')
        factory = request.POST.get('factory')
        license = request.POST.get('license')
        if (len(name) == 0) or (len(factory) == 0) or (len(license) == 0) or (len(user) == 0):
            msg = "数据不全，饲料录入失败"
            return render(request, "pages_doc_addfodder.html", {"msg": msg})
        else:
            Fodder.objects.create(
                name=name,
                factory=factory,
                license=license,
                user=u,
            )
            msg = "饲料信息录入成功"

            return render(request, "pages_doc_addfodder.html",{"msg": msg})

class AddFodderInfo(View):
    @method_decorator(login_required(login_url='/users/login/'), name='dispatch')
    @xframe_options_exempt
    def get(self, request):
        fo = Fodder.objects.filter()
        # a = CultivationInfo.objects.filter(qiid__isnull=True).values_list("aid_id") # 多表联合查询
        ani = Animal.objects.filter(is_turn=False).order_by("create_time")

        # ani = Animal.objects.filter().values_list('id').union(CultivationInfo.objects.filter(qiid__isnull=True).values_list('aid'))

        return render(request, "pages_doc_addfodderinfo.html", locals())
    def post(self, request):
        user = request.POST.get('user')
        u = User.objects.get(id=user)
        fo = Fodder.objects.filter()
        a = request.POST.get('aid')
        n = request.POST.get('brand')
        num = request.POST.get('num')
        if (len(n) == 0) or (len(num) == 0) or (len(a) == 0) or (len(user) == 0):
            msg = "数据不全，饲料使用信息录入失败"
            return render(request, "pages_doc_addfodderinfo.html", {"msg": msg,"fo":fo})
        else:
            ani = Animal.objects.get(id=a)
            order = Fodder.objects.get(id=n)
            FodderInfo.objects.create(
                fid=order,
                use_num=num,
                user=u,
            )

            fiid = FodderInfo.objects.last()
            CultivationInfo.objects.create(
                aid=ani,
                fiid=fiid,
            )

            msg = "饲料使用信息信息录入成功"
            return render(request, "pages_doc_addfodderinfo.html", {"msg": msg,"fo":fo})

class VaccineBoard(View):
    @method_decorator(login_required(login_url='/users/login/'), name='dispatch')
    def get(self, request):
        viid = VaccineInfo.objects.last()
        mes = CultivationInfo.objects.filter(viid__isnull=False)
        mess = Vaccine.objects.filter()
        messi = VaccineInfo.objects.filter()
        return render(request, "pages_doc_vaccine.html",{"mes":mes,"mess":mess,"messi":messi})
class AddVaccine(View):
    @method_decorator(login_required(login_url='/users/login/'), name='dispatch')
    @xframe_options_exempt
    def get(self, request):
        return render(request, "pages_doc_addvaccine.html")
    def post(self, request):
        user = request.POST.get('user')
        u = User.objects.get(id=user)
        name = request.POST.get('name')
        factory = request.POST.get('factory')
        license = request.POST.get('license')
        if (len(name) == 0) or (len(factory) == 0) or (len(license) == 0) or (len(user) == 0):
            msg = "数据不全，疫苗信息录入失败"
            return render(request, "pages_doc_addvaccine.html", {"msg": msg})
        else:
            Vaccine.objects.create(
                name=name,
                factory=factory,
                license=license,
                user=u,
            )
            msg = "疫苗信息录入成功"

            return render(request, "pages_doc_addvaccine.html",{"msg": msg})

class AddVaccineInfo(View):
    @method_decorator(login_required(login_url='/users/login/'), name='dispatch')
    @xframe_options_exempt
    def get(self, request):
        vo = Vaccine.objects.filter()
        ani = Animal.objects.filter(is_turn=False).order_by("-create_time")
        return render(request, "pages_doc_addvaccineinfo.html", locals())
    def post(self, request):
        user = request.POST.get('user')
        u = User.objects.get(id=user)
        vo = Vaccine.objects.filter()
        a = request.POST.get('aid')
        n = request.POST.get('brand')
        num = request.POST.get('num')
        if (len(n) == 0) or (len(num) == 0) or (len(a) == 0) or (len(user) == 0):
            msg = "数据不全，疫苗使用信息录入失败"
            return render(request, "pages_doc_addvaccineinfo.html", {"msg": msg,"vo":vo})
        else:
            ani = Animal.objects.get(id=a)
            order = Vaccine.objects.get(id=n)
            VaccineInfo.objects.create(
                vid=order,
                use_num=num,
                user=u
            )

            viid = VaccineInfo.objects.last()
            CultivationInfo.objects.create(
                aid=ani,
                viid=viid,
            )

            msg = "疫苗使用信息信息录入成功"
            return render(request, "pages_doc_addvaccineinfo.html", {"msg": msg,"vo":vo})

class Turn(View):
    @method_decorator(login_required(login_url='/users/login/'), name='dispatch')
    def get(self, request):
        ms = CultivationInfo.objects.filter(tiid__isnull=False)  # 取此列不为空的的行
        return render(request, "pages_doc_turn.html", {"ms":ms})

class AddTurn(View):
    @method_decorator(login_required(login_url='/users/login/'), name='dispatch')
    def get(self, request):
        ani = Animal.objects.filter(is_turn=False).order_by("create_time")
        return render(request, "forms_addturninfo.html", locals())
    def post(self, request):
        user = request.POST.get('user')
        u = User.objects.get(id=user)
        si = request.POST.get('si')
        name = request.POST.get('name')
        band = request.POST.get('band')
        if (len(si) == 0) or (len(name) == 0) or (len(band) == 0) or (len(user) == 0):
            msg = "数据不全，转出信息录入失败"
            return render(request, "forms_addturninfo.html", {"msg": msg})
        else:
            ani = Animal.objects.get(id=si)
            ani.is_turn = True
            ani.save()

            TurnInfo.objects.create(
                sla_name=name,
                car_name=band,
                user=u,
            )

            tiid = TurnInfo.objects.last()
            CultivationInfo.objects.create(
                aid=ani,
                tiid=tiid,
            )

            msg = "转出信息信息录入成功"
            return render(request, "forms_addturninfo.html", {"msg": msg})

class Quarantine(View):
    @method_decorator(login_required(login_url='/users/login/'), name='dispatch')
    def get(self, request):
        ms = CultivationInfo.objects.filter(qiid__isnull=False).order_by("-create_time")  #取此列不为空的的行
        return render(request, "pages_doc_quarantine.html",{"ms":ms})

class AddQuarantine(View):
    @method_decorator(login_required(login_url='/users/login/'), name='dispatch')
    def get(self, request):
        ani = Animal.objects.filter(is_turn=False).order_by("-create_time")
        return render(request, "forms_addquarantine.html", locals())
    def post(self, request):
        user = request.POST.get('user')
        u = User.objects.get(id=user)
        si = request.POST.get('si')
        qua_end = request.POST.get('qua_end')
        qua_team = request.POST.get('qua_team')
        if (len(si) == 0) or (len(qua_end) == 0) or (len(qua_team) == 0):
            msg = "数据不全，检疫信息录入失败"
            return render(request, "forms_addquarantine.html", {"msg": msg})
        else:
            ani = Animal.objects.get(id=si)

            QuarantineInfo.objects.create(
                qua_end=qua_end,
                qua_team=qua_team,
                user=u
            )

            qiid = QuarantineInfo.objects.last()
            CultivationInfo.objects.create(
                aid=ani,
                qiid=qiid,
            )

            msg = "检疫信息信息录入成功"
            return render(request, "forms_addquarantine.html", {"msg": msg})