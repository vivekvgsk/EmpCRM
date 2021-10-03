
from django.shortcuts import render,redirect
from django.views.generic import TemplateView,CreateView,ListView,UpdateView,DeleteView,DetailView
from .models import MyEmp
from .forms import EmployeeRegistrationForm,LoginForm
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.db.models import Q
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
import datetime
from datetime import timedelta
from django.utils import timezone
from celery.schedules import crontab
from celery.task import periodic_task


from django.core.mail import send_mail
# Create your views here.

def get_bday_count():
    datetime_now = timezone.now()
    now_day, now_month = datetime_now.day, datetime_now.month
    cnt = MyEmp.objects.filter(dob__day=now_day, dob__month=now_month).count()
    return cnt


@method_decorator(login_required,name="dispatch")
class Home(TemplateView):
    template_name="index2.html"
    context={}

    def get(self, request, *args, **kwargs):
        employees=MyEmp.objects.all()
        totemp = MyEmp.objects.all().count()
        femp = MyEmp.objects.filter(gender="Female").count()
        memp = MyEmp.objects.filter(gender="Male").count()
        oemp = MyEmp.objects.filter(gender="Others").count()
        cnt=get_bday_count()
        self.context = {
            "totemp": totemp,
            "femp": femp,
            "memp":memp,
            "oemp":oemp,
            "employees":employees,
            "cnt":cnt
        }
        return render(request, self.template_name, self.context)




class SignInView(TemplateView):
    model=MyEmp
    form_class=LoginForm
    template_name="signin.html"
    # template_name="index.html"
    context={}
    def get(self,request,*args,**kwargs):
        form=self.form_class()
        self.context["form"]=form
        return render(request,self.template_name,self.context)
    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            user=authenticate(request,username=username,password=password)
            if user:

                login(request,user)
                print("loginsucess")
                return redirect("bday")


            else:
                messages.error(request,"Invalid User")
                return render(request, self.template_name, self.context)

        return render(request, self.template_name, self.context)

# class LogOutView(TemplateView):
#     def get(self,request,*args,**kwargs):
#         logout(request)
#         return redirect("login")

def sign_out(request,*args,**kwargs):
    logout(request)
    return redirect("login")

@method_decorator(login_required,name="dispatch")
class EmpCreationView(CreateView):
    model=MyEmp
    form_class = EmployeeRegistrationForm
    template_name = "register.html"
    success_url = reverse_lazy("list")
    cnt = get_bday_count()
    context={"cnt":cnt}

@method_decorator(login_required, name="dispatch")
class EmpListView(TemplateView):
    model=MyEmp
    template_name="listemp.html"
    context={}


    def get(self,request,*args,**kwargs):
        employees=self.model.objects.all()
        cnt = get_bday_count()
        self.context={"employees":employees,"cnt":cnt}
        # self.context["employees"]=employees
        return render(request, self.template_name, self.context)

@method_decorator(login_required, name="dispatch")
class EmpProfileView(DetailView):
    model=MyEmp
    template_name="empdetails.html"
    context_object_name ="emp"

@method_decorator(login_required, name="dispatch")
class EmpEditView(UpdateView):
    model=MyEmp
    form_class = EmployeeRegistrationForm
    template_name = "empedit.html"
    success_url = reverse_lazy("list")

@method_decorator(login_required, name="dispatch")
class EmployeeFilterView(TemplateView):
    def post(self,request,*args,**kwargs):
        cnt = get_bday_count()

        search=request.POST.get('search',None)
        if search:
            employees=MyEmp.objects.filter((Q(first_name=search) | Q(department=search) | Q(id=search)))

            return render(request, "filter.html",{'employees':employees,'cnt':cnt})
        return render(request, "filter.html")

# class BdayNotification(TemplateView):
#     def get(self,request,*args,**kwargs):
#         emp=MyEmp.objects.all()
#         date = datetime.date.today()
#         print(date)
#         for em in emp:
#
#             # print(str(em.dob))
#             bday=str(em.dob)
#             bmd=bday[5:]
#             print(bmd)
#             tday=str((date))
#             today=tday[5:]
#             print(today)
#
#
#         return render(request,"index2.html")
# @periodic_task(run_every=crontab(hour=3, minute=57, day_of_week=6))
# def bday_alert(request):
#
#     datetime_now = timezone.now()
#     now_day, now_month = datetime_now.day, datetime_now.month
#     print(now_day)
#     print(now_month)
#     emps = MyEmp.objects.filter(dob__day=now_day, dob__month=now_month)
#     print("hi")
#     print(emps)
#     context={"emps":emps}
#     return render(request,"index2.html",context)


def bday_alert(request,*args,**kwargs):
    if request.method=="GET":
        datetime_now = timezone.now()
        now_day, now_month = datetime_now.day, datetime_now.month
        print(now_day)
        print(now_month)
        emps = MyEmp.objects.filter(dob__day=now_day, dob__month=now_month)
        cnt = MyEmp.objects.filter(dob__day=now_day, dob__month=now_month).count()
        print("hi")
        print(emps)
        context={"emps":emps,
                 "cnt":cnt}
        return render(request, "index2.html",context)