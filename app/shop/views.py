from django.shortcuts import render,redirect,reverse
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from ..slaughter.models import Slaughter, SlaughterInfo
from ..users.models import User
from . models import SaleInfo, ListInfo, Passage
from ..greatadmin.models import Animal
from ..homeindex.models import TBCode
import qrcode, os
from django.conf import settings


class SaleInfoBoard(View):
    @method_decorator(login_required(login_url='/users/login/'), name='dispatch')
    def get(self, request):
        sli = SlaughterInfo.objects.filter(is_in=False)
        sa = SaleInfo.objects.filter()
        return render(request, "pages_doc_shop.html", {"sli": sli,"sa":sa})

class AddSaleInfo(View):
    @method_decorator(login_required(login_url='/users/login/'), name='dispatch')
    def get(self, request):
        sli = SlaughterInfo.objects.filter(is_in=False)
        sa = SlaughterInfo.objects.values_list("id")
        return render(request, "forms_addlsaleinfo.html",{"sli": sli,"sa":sa})
    def post(self, request):

        sli = SlaughterInfo.objects.filter(is_in=False)
        sa = SaleInfo.objects.filter()

        n = request.POST.get('name')
        name = User.objects.get(id=n)

        s = request.POST.get('sid')
        price = request.POST.get('price')
        license = request.POST.get('license')

        ##
        aid = SlaughterInfo.objects.get(id=s).aid_id
        shgroup = Animal.objects.get(id=aid)
        shgroup.shgroup = name
        shgroup.save()
        ##

        if (len(n) == 0) or (len(s) == 0) or (len(price) == 0) or (len(license) == 0):
            msg = "数据不全，销售信息录入失败"
            return render(request, "forms_addlsaleinfo.html", {"msg":msg,"sli": sli,"sa":sa})
        else:
            a = SlaughterInfo.objects.get(id=s)
            a.is_in = True
            a.save()

            name = User.objects.get(username=name)  # !!!!!!!!!!!!
            si = SlaughterInfo.objects.get(id=s)  # !!!!!!!!!!!
            SaleInfo.objects.create(
                siid=si,
                lisence=license,
                name=name,
                price=price,
            )

            msg = "销售信息录入成功"
        return render(request, "forms_addlsaleinfo.html",{"msg":msg,"sli": sli,"sa":sa})

class ListInfoBorad(View):####
    @method_decorator(login_required(login_url='/users/login/'), name='dispatch')
    def get(self, request):
        # mes = ListInfo.objects.filter()
        tb = TBCode.objects.filter()
        return render(request, "pages_doc_listinfo.html", locals())

class AddListInfo(View):
    @method_decorator(login_required(login_url='/users/login/'), name='dispatch')
    def get(self, request):
        sa = SaleInfo.objects.filter()
        pa = Passage.objects.filter().order_by("-create_time")[:5]
        return render(request, "forms_addlistinfo.html",{"sa":sa,"pa":pa})
    def post(self, request):
        sa = SaleInfo.objects.filter()
        pa = Passage.objects.filter().order_by("-create_time")[:5]

        if 'info' in request.POST:
            u = request.POST.get('user')
            user= User.objects.get(id=u)
            si = request.POST.get('si')
            heavy = request.POST.get('heavy')
            price = request.POST.get('price')
            day = request.POST.get('day')
            if (len(si) == 0) or (len(heavy) == 0) or (len(price) == 0) or (len(day) == 0) or (len(u) == 0):
                msg = "数据不全，销售清单信息录入失败"
                return render(request, "forms_addlistinfo.html", {"msg": msg,"sa":sa,"pa":pa})
            else:
                saiid = SaleInfo.objects.get(id=si)  # !!!!!!!!!!!
                ListInfo.objects.create(
                    saiid=saiid,
                    heavy=heavy,
                    price=price,
                    day=day,
                    user=user,
                )
                msg = "销售清单信息录入成功"

                list = ListInfo.objects.filter().order_by("-create_time").first()
                animal = ListInfo.objects.filter().order_by("-create_time").first().saiid.siid.aid
                nlist = ListInfo.objects.filter().order_by("-create_time").first().id
                nanimal = ListInfo.objects.filter().order_by("-create_time").first().saiid.siid.aid.id
                code = int(str(nanimal)+str(nlist))

                TBCode.objects.create(
                    animal=animal,
                    listinfo=list,
                    code=code,
                    )

                return render(request, "forms_addlistinfo.html", {"msg": msg,"sa":sa,"pa":pa})
        elif 'na' in request.POST:
            passage = request.POST.get('passage')
            u = request.POST.get('u')
            if len(passage) ==0 or len(u) == 0:
                msg = "数据不全，备忘信息录入失败"
                return render(request, "forms_addlistinfo.html", {"msg": msg,"sa":sa,"pa":pa})
            else:
                uid = User.objects.get(username=u)  # !!!!!!!!!!!!

                Passage.objects.create(
                    uid=uid,
                    passage=passage,
                )
                msg = "备忘信息录入成功"
                return render(request, "forms_addlistinfo.html", {"msg": msg,"sa":sa,"pa":pa})