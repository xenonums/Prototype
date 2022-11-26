from __future__ import unicode_literals
from django.shortcuts import render
# Create your views here.
from django.shortcuts import render, redirect, reverse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from .models import HNews, TBCode
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage
from datetime import datetime
from django.contrib import messages
from ..greatadmin.models import Animal
from ..cultivation.models import CultivationInfo
from ..slaughter.models import SlaughterInfo
from ..shop.models import SaleInfo, ListInfo
from django.db.models import Q
from django.http import HttpResponse, JsonResponse

import qrcode
from django.shortcuts import render
from django.http import HttpResponse
from io import BytesIO

import jieba
import jieba.analyse
# 生成二维码
class BecomeQrcode(View):
    def get(self, request, aid, sid):
        u = request.get_host()
        url = "http://" + u + "/homeindex/traceabilityinfo" + str(aid) + "+" + str(sid)
        img = qrcode.make(url)

        buf = BytesIO()
        img.save(buf)
        image_stream = buf.getvalue()

        return HttpResponse(image_stream, content_type="image/png")


# 搜索
class SearchNews(View):
    def get(self, request):  # 超级链接是get请求，则只写get函数就可以了
        search_word = request.GET.get("wd","")
        # 标题匹配
        search_news = HNews.objects.filter(title__icontains=search_word)
        count = HNews.objects.filter(title__icontains=search_word).count()
        reco = HNews.objects.filter().order_by("-views")[:10]
        return render(request, "home_search.html", locals())


# 溯源查询
class SearchTraceability(View):
    def post(self, request):
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            pc = request.POST.get("productCode")
            try:
                ab = TBCode.objects.get(code=pc).code
            except TBCode.DoesNotExist:
                datas = {'msg': "溯源码不存在"}
                return JsonResponse(datas)

            aid = pc[:22]
            sid = pc[22:]
            datas = {'msg': "溯源码存在", 'aid': aid, 'sid': sid}
            return JsonResponse(datas)
            # return redirect(reverse("homeindex:traceabilityinfo", args=(aid, sid)), locals())
# 溯源
class TraceabilityInfo(View):
    def get(self, request, aid, sid):  # 超级链接是get请求，则只写get函数就可以了
        newest = HNews.objects.filter().order_by("-create_time")[:10]
        reco = HNews.objects.filter().order_by("-views")[:10]

        # 重要溯源流程
        name = aid[:1]
        id = aid
        animal = Animal.objects.get(id=aid)  # 要么0要么1条 (第一个id是：数据库表格里字段的名字，第二个id是：参数传递过来的具体的值）
        # 养殖企业
        fc = CultivationInfo.objects.filter(Q(aid=aid) & Q(fiid__isnull=False))
        vc = CultivationInfo.objects.filter(Q(aid=aid) & Q(viid__isnull=False))
        qc = CultivationInfo.objects.filter(Q(aid=aid) & Q(qiid__isnull=False))
        tc = CultivationInfo.objects.filter(Q(aid=aid) & Q(tiid__isnull=False))
        # 屠宰企业
        slsf = SlaughterInfo.objects.filter(aid=aid).first()
        sls = SlaughterInfo.objects.filter(aid=aid)
        # 销售企业

        shsa = SlaughterInfo.objects.filter(Q(aid=aid) & Q(is_in__isnull=False))
        shs = ListInfo.objects.filter(id=sid)

        return render(request, "home_endinfo.html", locals())

# 打开新闻+相关性
class OpenNews(View):
    def get(self, request, nid):  # 超级链接是get请求，则只写get函数就可以了
        pages = HNews.objects.get(id=nid)  # 要么0要么1条 (第一个id是：数据库表格里字段的名字，第二个id是：参数传递过来的具体的值）
        reco = HNews.objects.filter().order_by("-views")[:10]
        if not request.COOKIES.get("news_%s_read" % nid):
            pages.views += 1
            pages.save()
        # 相关性(废弃！！！！)
        # cpages = strip_tags(HNews.objects.get(id=nid).gcontent)  # 获取本网页文章
        # count = jieba.lcut(cpages) # 分词
        # word_count = {}
        # for word in count:
        #     word_count[word] = word_count.get(word, 0) + 1  # 统计
        # word_count = {}
        #
        # module_dir = os.path.dirname(__file__)
        # file_path = os.path.join(module_dir, 'HIT_ST.txt')  # 读取ST.
        # stopwords = [line.strip() for line in open(file_path, encoding="utf-8").readlines()]
        # for word in count:
        #     if word not in stopwords:
        #         # 不统计字数为一的词
        #         if len(word) == 1:
        #             continue
        #         else:
        #             word_count[word] = word_count.get(word, 0) + 1   # 去停用词
        #
        # items = list(word_count.items())
        # items.sort(key=lambda x: x[1], reverse=True)  # 高低排序

        # module_dir = os.path.dirname(__file__)
        # file_path = os.path.join(module_dir, 'HIT_ST.txt')  # 读取ST.
        # stopwords = [line.strip() for line in open(file_path, encoding="utf-8").readlines()]
        # for word in count:
        #     if word not in stopwords:
        #         # 不统计字数为一的词
        #         if len(word) == 1:
        #             continue
        #         else:
        #             word_list.append(word)
        #
        # 转化矩阵
        # vectorizer = CountVectorizer()
        # word_frequence = vectorizer.fit_transform(word_list)
        # words = vectorizer.get_feature_names()
        # #TF -IDF
        # transformer = TfidfTransformer()
        # tfidf = transformer.fit_transform(word_frequence)
        # weight = tfidf.toarray()
        #
        # data = {'word': vectorizer.get_feature_names(),
        #         'tfidf': tfidf.toarray().sum(axis=0).tolist()}
        # df = pd.DataFrame(data)
        # df.sort_values(by="tfidf", ascending=False)

        bpages = HNews.objects.get(id=nid).gcontent  # 获取本网页文章
        cpages = HNews.objects.filter(~Q(id=nid))  # 获取本网页文章
        base = jieba.analyse.extract_tags(bpages, topK=10)  # 基础关键词

        id = []
        title = []
        timel = []
        retlist = []
        for c in cpages:
            retlist = list(set(jieba.analyse.extract_tags(c.gcontent, topK=10)) & set(base))
            if len(retlist) >= 3:
                id.append(c.id)
                title.append(c.title)
                timel.append(c.create_time)
            else:
                continue
        itzip = list(zip(id, title, timel))[:5]

        response = render(request, "home_page.html", locals())
        response.set_cookie("news_%s_read" % nid, "true")
        return response
        
# class OpenNews(View):
#     def get(self, request, nid):  # 超级链接是get请求，则只写get函数就可以了
#         pages = HNews.objects.get(id=nid)  # 要么0要么1条 (第一个id是：数据库表格里字段的名字，第二个id是：参数传递过来的具体的值）
#         reco = HNews.objects.filter().order_by("-views")[:10]
#         if not request.COOKIES.get("news_%s_read" % nid):
#             pages.views += 1
#             pages.save()

#         response = render(request, "home_page.html", locals())
#         response.set_cookie("news_%s_read" % nid, "true")
#         return response

class HomeIndex(View):
    def get(self, request):
        newest = HNews.objects.filter().order_by("-create_time")[:10]
        head = HNews.objects.filter(category='8').order_by("-create_time")[:6]
        headnews = HNews.objects.filter(category='1').order_by("-create_time")[:1]
        headnewsl = HNews.objects.filter(category='1').order_by("-create_time")[1:6]
        notice = HNews.objects.filter(category='3').order_by("-create_time")[:7]
        exposure = HNews.objects.filter(category='4').order_by("-create_time")[:7]
        group = HNews.objects.filter(category='5').order_by("-create_time")[:8]
        legal = HNews.objects.filter(category='2').order_by("-create_time")[:7]
        know = HNews.objects.filter(category='6').order_by("-create_time")[:7]
        mnews = HNews.objects.filter(category='1').order_by("-create_time")[:4]
        return render(request, "home_index.html", locals())

class HomeNews(View):
    def get(self, request):
        newest = HNews.objects.filter().order_by("-create_time")[:10]
        new = HNews.objects.filter(category='1').order_by("-create_time")
        reco = HNews.objects.filter().order_by("views")[:10]
        ######################################

        paginator = Paginator(new, 20)

        # 获取 url 后面的 page 参数的值, 首页不显示 page 参数, 默认值是 1
        page = request.GET.get('page', 1)
        currentPage = int(page)
        try:
            Page = paginator.page(page)
        # todo: 注意捕获异常
        except PageNotAnInteger:
            # 如果请求的页数不是整数, 返回第一页。
            Page = paginator.page(1)
        except InvalidPage:
            # 如果请求的页数不存在, 重定向页面
            return HttpResponse('找不到页面的内容')
        except EmptyPage:
            # 如果请求的页数不在合法的页数范围内，返回结果的最后一页。
            Page = paginator.page(paginator.num_pages)

        ######################################
        return render(request, "home_news.html", locals())  # locals () 函数会以字典类型返回当前位置的全部局部变量。

class HomeTraceability(View):
    def get(self, request):
        newest = HNews.objects.filter().order_by("-create_time")[:10]
        reco = HNews.objects.filter().order_by("-views")[:10]
        return render(request, "home_traceability.html", locals())

class HomeLegal(View):
    def get(self, request):
        newest = HNews.objects.filter().order_by("-create_time")[:10]
        legal = HNews.objects.filter(category='2').order_by("-create_time")
        reco = HNews.objects.filter().order_by("-views")[:10]
        ######################################

        paginator = Paginator(legal, 20)

        # 获取 url 后面的 page 参数的值, 首页不显示 page 参数, 默认值是 1
        page = request.GET.get('page', 1)
        currentPage = int(page)
        try:
            Page = paginator.page(page)
        # todo: 注意捕获异常
        except PageNotAnInteger:
            # 如果请求的页数不是整数, 返回第一页。
            Page = paginator.page(1)
        except InvalidPage:
            # 如果请求的页数不存在, 重定向页面
            return HttpResponse('找不到页面的内容')
        except EmptyPage:
            # 如果请求的页数不在合法的页数范围内，返回结果的最后一页。
            Page = paginator.page(paginator.num_pages)

        ######################################
        return render(request, "home_legal.html", locals())  # locals () 函数会以字典类型返回当前位置的全部局部变量。

class HomeNotice(View):
    def get(self, request):
        newest = HNews.objects.filter().order_by("-create_time")[:10]
        notice = HNews.objects.filter(category='3').order_by("-create_time")
        reco = HNews.objects.filter().order_by("-views")[:10]
        ######################################

        paginator = Paginator(notice, 20)

        # 获取 url 后面的 page 参数的值, 首页不显示 page 参数, 默认值是 1
        page = request.GET.get('page', 1)
        currentPage = int(page)
        try:
            Page = paginator.page(page)
        # todo: 注意捕获异常
        except PageNotAnInteger:
            # 如果请求的页数不是整数, 返回第一页。
            Page = paginator.page(1)
        except InvalidPage:
            # 如果请求的页数不存在, 重定向页面
            return HttpResponse('找不到页面的内容')
        except EmptyPage:
            # 如果请求的页数不在合法的页数范围内，返回结果的最后一页。
            Page = paginator.page(paginator.num_pages)

        ######################################
        return render(request, "home_notice.html", locals())  # locals () 函数会以字典类型返回当前位置的全部局部变量。

class HomeExposure(View):
    def get(self, request):
        newest = HNews.objects.filter().order_by("-create_time")[:10]
        exposure = HNews.objects.filter(category='4').order_by("-create_time")
        reco = HNews.objects.filter().order_by("-views")[:10]
        ######################################

        paginator = Paginator(exposure, 20)

        # 获取 url 后面的 page 参数的值, 首页不显示 page 参数, 默认值是 1
        page = request.GET.get('page', 1)
        currentPage = int(page)
        try:
            Page = paginator.page(page)
        # todo: 注意捕获异常
        except PageNotAnInteger:
            # 如果请求的页数不是整数, 返回第一页。
            Page = paginator.page(1)
        except InvalidPage:
            # 如果请求的页数不存在, 重定向页面
            return HttpResponse('找不到页面的内容')
        except EmptyPage:
            # 如果请求的页数不在合法的页数范围内，返回结果的最后一页。
            Page = paginator.page(paginator.num_pages)

        ######################################
        return render(request, "home_exposure.html", locals())  # locals () 函数会以字典类型返回当前位置的全部局部变量。

class HomeGroup(View):
    def get(self, request):
        newest = HNews.objects.filter().order_by("-create_time")[:10]
        group = HNews.objects.filter(category='5').order_by("-create_time")
        reco = HNews.objects.filter().order_by("-views")[:10]
        ######################################

        paginator = Paginator(group, 20)

        # 获取 url 后面的 page 参数的值, 首页不显示 page 参数, 默认值是 1
        page = request.GET.get('page', 1)
        currentPage = int(page)
        try:
            Page = paginator.page(page)
        # todo: 注意捕获异常
        except PageNotAnInteger:
            # 如果请求的页数不是整数, 返回第一页。
            Page = paginator.page(1)
        except InvalidPage:
            # 如果请求的页数不存在, 重定向页面
            return HttpResponse('找不到页面的内容')
        except EmptyPage:
            # 如果请求的页数不在合法的页数范围内，返回结果的最后一页。
            Page = paginator.page(paginator.num_pages)

        ######################################
        return render(request, "home_group.html", locals())  # locals () 函数会以字典类型返回当前位置的全部局部变量。

class HomeKnow(View):
    def get(self, request):
        newest = HNews.objects.filter().order_by("-create_time")[:10]
        know = HNews.objects.filter(category='6').order_by("-create_time")
        reco = HNews.objects.filter().order_by("-views")[:10]
        ######################################

        paginator = Paginator(know, 20)

        # 获取 url 后面的 page 参数的值, 首页不显示 page 参数, 默认值是 1
        page = request.GET.get('page', 1)
        currentPage = int(page)
        try:
            Page = paginator.page(page)
        # todo: 注意捕获异常
        except PageNotAnInteger:
            # 如果请求的页数不是整数, 返回第一页。
            Page = paginator.page(1)
        except InvalidPage:
            # 如果请求的页数不存在, 重定向页面
            return HttpResponse('找不到页面的内容')
        except EmptyPage:
            # 如果请求的页数不在合法的页数范围内，返回结果的最后一页。
            Page = paginator.page(paginator.num_pages)

        ######################################
        return render(request, "home_know.html", locals())  # locals () 函数会以字典类型返回当前位置的全部局部变量。

class HomeIntroduction(View):
    def get(self, request):
        newest = HNews.objects.filter().order_by("-create_time")[:10]
        reco = HNews.objects.filter().order_by("-views")[:10]
        return render(request, "home_introduction.html", locals())

class HomeComm(View):
    def get(self, request):
        newest = HNews.objects.filter().order_by("-create_time")[:10]
        reco = HNews.objects.filter().order_by("-views")[:10]
        return render(request, "home_comm.html", locals())

class HomeJvbao(View):
    def get(self, request):
        return render(request, "jvbao.html", locals())