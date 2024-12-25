from django.urls import path
from myApp import views

urlpatterns=[
    path("login/",views.login,name="login"),
    path("register/",views.register,name="register"),
    # path("check/",views.check,name="check"),
    path('user/',views.user,name="user"),
    path('login_admin/',views.login_admin,name="login_admin"),
    path('admin_homepage/',views.admin_homepage,name="admin_homepage"),
    path('homepage/',views.homepage,name="homepage"),
    path("calculator/",views.calculator,name="calculator"),
    path('plot/',views.plot,name="plot"),
    path('matrix_compute/',views.matrix_compute,name="matrix_compute"),
    path('function_progress/',views.function_progress,name="function_progress"),
    path("get_all_text/",views.get_all_text,name="get_all_text"),
    path("customer_analysis/",views.customer_analysis,name="customer_analysis"),
    path("problem_analysis/",views.problem_analysis,name="problem_analysis"),
    path("topic_analysis/",views.topic_analysis,name="topic_analysis"),
    # path("plot_text/",views.plot_text,name="plot_text"),
    # path("Createcount/",views.Createcount,name="Createcount"),
    path("trending/",views.trending,name="trending"),
    path("challenges/",views.challenges,name="challenges"),
    path("self-challenges/",views.self_challenges,name="self-challenges"),
    path("profile/",views.profile,name="profile"),
    path("forum/",views.forum,name="forum"),
    path("check/",views.check,name="check"),
    path("check_text/",views.check_text,name="check_text"),
    path("resources/",views.resources,name="resources"),
    path("question1/",views.question1,name="question1"),
    path("question2/",views.question2,name="question2"),
    path("question3/",views.question3,name="question3"),
    path("question4/",views.question4,name="question4"),
    path("数学/",views.math,name="数学"),
    path("数学三大核心领域/",views.math1,name="数学三大核心领域"),
    path("抽象代数/",views.math2,name="抽象代数"),
]