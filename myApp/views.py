import json
from datetime import datetime

from django.shortcuts import render,redirect
from django.template.defaulttags import comment
from django.views.decorators.csrf import csrf_exempt
from matplotlib.table import table
# from requests.packages import target
from statsmodels.genmod.families.links import identity
from django.db.models import Count, Sum
# Create your views here.
from django.core.paginator import Paginator
from statsmodels.sandbox.distributions.extras import informcode

from myApp.models import User,Admin,Posttext,Question,Answer_question
from django.http import JsonResponse
from .utils.get_information import *
# import sklearn
from django.utils import timezone

@csrf_exempt
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        username = data.get('username')
        password = data.get('password')
        last_login = timezone.now()
        # 将last_login转换为json格式
        last_login = last_login.strftime('%Y-%m-%d %H:%M:%S')
        if User.objects.filter(username=username, password=password).exists():
            request.session['username'] = username
            request.session['password'] = password
            request.session['last_login'] = last_login
            # 将登录时间存入数据库
            User.objects.filter(username=username).update(last_login=last_login)
            return JsonResponse({'success': 1, 'message': '登录成功'})
        else:
            return JsonResponse({'success': 0, 'message': '用户名或密码错误'})

@csrf_exempt
def login_admin(request):
    if request.method == 'POST':
        data= json.loads(request.body.decode('utf-8'))
        username= data.get('username')
        password= data.get('password')
        identify= data.get('identify')
        if Admin.objects.filter(username=username, password=password, identify=identify).exists():
            return JsonResponse({'success': 1, 'message': '登录成功'})
        else:
            return JsonResponse({'success': 0, 'message': '用户名或密码错误'})


@csrf_exempt
def admin_homepage(request):
    if request.method == 'GET':
        return render(request, 'get_all_text.html')


@csrf_exempt
def register(request):
    if request.method == 'POST':
        data=json.loads(request.body.decode('utf-8'))
        username= data.get('username')
        password= data.get('password')
        email= data.get('email')
        # 检查User中是否已经存在username了
        if User.objects.filter(username=username).exists():
            return JsonResponse({'success': 0, 'message': '用户名已存在'})
        if User.objects.filter(email=email).exists():
            return JsonResponse({'success': 0, 'message': '邮箱已被使用'})
        User.objects.create(username=username, password=password, email=email)
        return JsonResponse({'success': 1, 'message': '注册成功'})

@csrf_exempt
def user(request):
    if request.method == 'GET':
        return render(request, 'user.html')

@csrf_exempt
def homepage(request):
    if request.method == 'GET':
        return render(request, 'homepage.html')

@csrf_exempt
def calculator(request):
    if request.method == 'GET':
        return render(request, 'calculator.html')

@csrf_exempt
def plot(request):
    if request.method == 'GET':
        return render(request, 'plot.html')

@csrf_exempt
def matrix_compute(request):
    if request.method == 'GET':
        return render(request, 'matrix_compute.html')


@csrf_exempt
def function_progress(request):
    if request.method == 'GET':
        return render(request, 'function_progress.html')

@csrf_exempt
def get_all_text(request):
    if request.method == 'GET':
        tabelData=get_history_post()
        post_text=Posttext.objects.all()
        paginator=Paginator(tabelData,10)
        cur_page=1
        if request.GET.get('page'):
            cur_page=int(request.GET.get('page'))
        c_page=paginator.page(cur_page)

        page_range=[]
        visibleNumber=10
        min=int(cur_page-visibleNumber/10)
        if min<1:
            min=1
        max=min+visibleNumber
        if max>paginator.page_range[-1]:
            max=paginator.page_range[-1]
        for i in range(min,max):
            page_range.append(i)

        return render(request, 'get_all_text.html',
                      {'post_text':post_text,
                       'page_range':page_range,
                       'c_page':c_page,
                       'paginator':paginator})

@csrf_exempt
def customer_analysis(request):

    user_information=get_users_information()
    gender={"男":0,"女":0}
    address = {'北京': 0, '天津': 0, '上海': 0, '重庆': 0, '河北': 0, '河南': 0, '云南': 0, '辽宁': 0, '黑龙江': 0, '湖南': 0,
               '安徽': 0, '山东': 0, '新疆': 0, '江苏': 0, '浙江': 0, '江西': 0, '湖北': 0, '广西': 0, '甘肃': 0, '山西': 0,
               '内蒙古': 0, '陕西': 0, '吉林': 0, '福建': 0, '贵州': 0, '广东': 0, '青海': 0, '西藏': 0, '四川': 0, '宁夏': 0,
                '海南': 0, '台湾': 0, '香港': 0, '澳门': 0}
    age={"15岁以下":0,"15-20岁":2,"20-25岁":3,"25-30岁":1,"30-40岁":1,"40-50岁":1,"50岁以上":1}
    # 数据来自leetcode（2024-10-7）
    score={"<1250":498,"1250-1300":831,"1300-1350":2638,"1350-1400":7762,"1400-1450":27970,"1450-1500":28540,"1500-1550":19747,"1550-1600":13092,"1600-1650":8756,"1650-1700":6169,"1700-1750":4494,"1750-1800":3407,"1800-1850":2690,"1850-1900":2031,"1900-1950":1746,"1950-2000":1297,
       "2000-2050":1105,"2050-2100":832,"2100-2150":698,"2150-2200":547,"2200-2250":426,"2250-2300":403,"2300-2350":327,"2350-2400":230,"2400+":1067}
    range=["<1250","1250-1300","1300-1350","1350-1400","1400-1450","1450-1500","1500-1550","1550-1600","1600-1650","1650-1700","1700-1750","1750-1800","1800-1850","1850-1900","1900-1950","1950-2000",
       "2000-2050","2050-2100","2100-2150","2150-2200","2200-2250","2250-2300","2300-2350","2350-2400","2400+"]

    for information in user_information:
        gender[information['gender']] += 1
        address[information['address']] += 1
        this_year = datetime.now().year
        ages = int(this_year) - int(information['birthday'].year)
        if ages < 15:
            age["15岁以下"] += 1
        elif ages < 20:
            age["15-20岁"] += 1
        elif ages < 25:
            age["20-25岁"] += 1
        elif ages < 30:
            age["25-30岁"] += 1
        elif ages < 40:
            age["30-40岁"] += 1
        elif ages < 50:
            age["40-50岁"] += 1
        else:
            age["50岁以上"] += 1
    print(gender)
    print(age)
    print(address)
    gender = [{'value': value, 'name': key} for key, value in gender.items()]
    address=[{'value': value, 'name': key} for key, value in address.items()]
    age=[value for key, value in age.items()]
    score=[value for key, value in score.items()]
    # 计算百分比
    scores2=[round(value/sum(score)*100,2) for value in score]
    print(gender)
    print(age)
    if request.method == 'GET':
        return render(request, 'customer_analysis.html',
                      {'gender':gender,
                       'age':age,
                       'address':address,
                       "score":score,
                       "scores2":scores2,})


@csrf_exempt
def problem_analysis(request):
    if request.method == 'GET':
        return render(request, 'problem_analysis.html')

@csrf_exempt
def topic_analysis(request):
    if request.method == 'GET':
        return render(request, 'topic_analysis.html')

@csrf_exempt
def challenges(request):
    if request.method == 'GET':
        username=request.session.get('username')
        post_text=Posttext.objects.filter(username=username)
        tabelData=get_text_information(username)
        paginator = Paginator(tabelData, 10)
        cur_page = 1
        if request.GET.get('page'):
            cur_page = int(request.GET.get('page'))
        c_page = paginator.page(cur_page)

        page_range = []
        visibleNumber = 10
        min = int(cur_page - visibleNumber / 10)
        if min < 1:
            min = 1
        max = min + visibleNumber
        if max > paginator.page_range[-1]:
            max = paginator.page_range[-1]
        for i in range(min, max):
            page_range.append(i)
        print(post_text,c_page)
        return render(request, 'challenges.html',
                      {'post_text': post_text,
                       'page_range': page_range,
                       'c_page': c_page,
                       'paginator': paginator})



        # return render(request, 'challenges.html')
    if request.method=='POST':
        data = json.loads(request.body.decode('utf-8'))
        question=data.get('question')
        title=data.get('title')
        username=request.session.get('username')
        # 将数据存入数据库
        Answer_question.objects.create(username=username,question_title=question,answer=title)
        return JsonResponse({'success': 1, 'message': '成功'})

@csrf_exempt
def trending(request):
    if request.method == 'GET':
        # 筛选出浏览量（viewers）前三的帖子
        post=Posttext.objects.order_by('-viewers')
        post_text_first=post[0]
        post_text_second=post[1]
        post_text_third=post[2]
        return render(request, 'trending.html',
                      {'post_text_first': post_text_first,
                       'post_text_second': post_text_second,
                       'post_text_third': post_text_third})
    if request.method == 'POST':
        data=json.loads(request.body.decode('utf-8'))
        title=data.get('title')
        # 点赞数实现自增
        t=Posttext.objects.filter(title=title)[0]
        if  data.get("target")=="like":
            # likes=Posttext.objects.filter(title=title).values('likes')[0]['likes']
            likes=t.likes
            Posttext.objects.filter(title=title).update(likes=likes+1)
        elif data.get("target")=="dislike":
            # 获取当前的踩数
            dislikes=t.dislikes
            Posttext.objects.filter(title=title).update(dislikes=dislikes+1)
        else:
            views=t.viewers
            Posttext.objects.filter(title=title).update(viewers=views+1)

        return JsonResponse({'success': 1, 'message': '成功'})

@csrf_exempt
def self_challenges(request):
    if request.method == 'GET':
        username=request.session.get('username')
        post_text=Answer_question.objects.filter(username=username,Judge=True)
        index=post_text.values('question_title').distinct()
        # 将{question_title:xxx}转化为{xxx:1}
        index=[value['question_title'] for value in index]
        return render(request,'self-challenges.html',
                      {'index':index})

@csrf_exempt
def profile(request):
    if request.method == 'GET':
        targetname=request.session.get('username')
        targetpassword=request.session.get('password')
        target=User.objects.filter(username=targetname,password=targetpassword)[0]
        # 转化为 /2021/10/07/ 这种格式
        # birthday=target.birthday.strftime('%Y-%m-%d')
        # 统计用户的发帖数
        post=Posttext.objects.filter(username=targetname)
        post_num=post.count()
        # 统计用户的帖子总点赞数
        post_like=post.aggregate(sum=Sum('likes'))
        answer=Answer_question.objects.filter(username=targetname)
        answer_num=answer.count()
        return render(request,
                      'profile.html',
                      {'username':target.username,
                       'gender':target.gender,
                       'birthday':target.birthday.strftime('%Y-%m-%d') ,
                       'address':target.address,
                       'email':target.email,
                       'post_num':post_num,
                       'post_like':post_like if post_like['sum'] else 0,
                       'answer_num':answer_num,})
    if request.method == 'POST':
        # const
        # body = {nickname, gender, birthday, address, email};
        data = json.loads(request.body.decode('utf-8'))
        username = data.get('nickname')
        gender= data.get('gender')
        email = data.get('email')
        birthday = data.get('birthday')
        address = data.get('address')
        request.session['username'] = username
        targetname=request.session.get('username')
        targetpassword=request.session.get('password')
        User.objects.filter(username=targetname,password=targetpassword).update(username=username,gender=gender,birthday=birthday,address=address,email=email)
        Posttext.objects.filter(username=targetname).update(username=username)
        return JsonResponse({'success': 1, 'message': targetpassword})

@csrf_exempt
def forum(request):
    if request.method == 'GET':
        username = request.session.get('username')
        post_text = Posttext.objects.filter(username=username)
        tabelData = get_text_information(username)
        paginator = Paginator(tabelData, 10)
        cur_page = 1
        if request.GET.get('page'):
            cur_page = int(request.GET.get('page'))
        c_page = paginator.page(cur_page)

        page_range = []
        visibleNumber = 10
        min = int(cur_page - visibleNumber / 10)
        if min < 1:
            min = 1
        max = min + visibleNumber
        if max > paginator.page_range[-1]:
            max = paginator.page_range[-1]
        for i in range(min, max):
            page_range.append(i)
        print(post_text, c_page)
        return render(request, 'forum.html',
                      {'post_text': post_text,
                       'page_range': page_range,
                       'c_page': c_page,
                       'paginator': paginator})

        # return render(request, 'forum.html')
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        comment=data.get('comment')
        username=request.session.get('username')
        # 读取第一个回车键之前的内容
        title=comment.split('\n')[0]
        content=comment[len(title)+1:]
        # 将数据存入数据库
        Posttext.objects.create(username=username, title=title, text=content)
        return JsonResponse({'success': 1, 'message': '成功'})

@csrf_exempt
def check(request):
    if request.method == 'GET':
        tabelData = get_history_post2()
        post_text = Posttext.objects.all()
        paginator = Paginator(tabelData, 10)
        cur_page = 1
        if request.GET.get('page'):
            cur_page = int(request.GET.get('page'))
        c_page = paginator.page(cur_page)

        page_range = []
        visibleNumber = 10
        min = int(cur_page - visibleNumber / 10)
        if min < 1:
            min = 1
        max = min + visibleNumber
        if max > paginator.page_range[-1]:
            max = paginator.page_range[-1]
        for i in range(min, max):
            page_range.append(i)

        return render(request, 'check.html',
                      {'post_text': post_text,
                       'page_range': page_range,
                       'c_page': c_page,
                       'paginator': paginator})

    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        title = data.get('title')
        username=data.get('username')

        Posttext.objects.filter(title=title,username=username).update(Judge=True)
        return JsonResponse({'success': 1, 'message': '成功'})


@csrf_exempt
def check_text(request):
    if request.method == 'GET':
        tabelData = get_check_post()
        post_text = Answer_question.objects.filter(Judge=False)
        paginator = Paginator(tabelData, 10)
        cur_page = 1
        if request.GET.get('page'):
            cur_page = int(request.GET.get('page'))
        c_page = paginator.page(cur_page)

        page_range = []
        visibleNumber = 10
        min = int(cur_page - visibleNumber / 10)
        if min < 1:
            min = 1
        max = min + visibleNumber
        if max > paginator.page_range[-1]:
            max = paginator.page_range[-1]
        for i in range(min, max):
            page_range.append(i)

        return render(request, 'check_text.html',
                      {'post_text': post_text,
                       'page_range': page_range,
                       'c_page': c_page,
                       'paginator': paginator})
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        answer=data.get('answer')
        Answer_question.objects.filter(answer=answer).update(Judge=True)
        return JsonResponse({'success': 1, 'message': '成功'})


@csrf_exempt
def resources(request):
    if request.method == 'GET':
        return render(request, 'resources.html')


@csrf_exempt
def question1(request):
    if request.method == 'GET':
        return render(request, 'question1.html')

@csrf_exempt
def question2(request):
    if request.method == 'GET':
        return render(request, 'question2.html')

@csrf_exempt
def question3(request):
    if request.method == 'GET':
        return render(request, 'question3.html')

@csrf_exempt
def question4(request):
    if request.method == 'GET':
        return render(request, 'question4.html')

@csrf_exempt
def math(request):
    if request.method == 'GET':
        return render(request, '数学.html')


def math1(request):
    if request.method == 'GET':
        return render(request, '数学三大核心领域.html')

def math2(request):
    if request.method == 'GET':
        return render(request, '抽象代数.html')
