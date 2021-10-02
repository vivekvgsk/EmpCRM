
from django.shortcuts import render,redirect
from django.views.generic import TemplateView,CreateView,ListView,UpdateView,DeleteView,DetailView
from .models import MyEmp
from .forms import EmployeeRegistrationForm,LoginForm
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.db.models import Q

from django.core.mail import send_mail
# Create your views here.

class Home(TemplateView):
    template_name="index2.html"
    context={}

    def get(self, request, *args, **kwargs):
        employees=MyEmp.objects.all()
        totemp = MyEmp.objects.all().count()
        femp = MyEmp.objects.filter(gender="Female").count()
        memp = MyEmp.objects.filter(gender="Male").count()
        oemp = MyEmp.objects.filter(gender="Others").count()
        self.context = {
            "totemp": totemp,
            "femp": femp,
            "memp":memp,
            "oemp":oemp,
            "employees":employees
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
                return redirect("home")


            else:
                messages.error(request,"Invalid User")
                return render(request, self.template_name, self.context)

        return render(request, self.template_name, self.context)

class LogOutView(TemplateView):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("login")

class EmpCreationView(CreateView):
    model=MyEmp
    form_class = EmployeeRegistrationForm
    template_name = "register.html"
    success_url = reverse_lazy("list")

class EmpListView(TemplateView):
    model=MyEmp
    template_name="listemp.html"
    context={}

    def get(self,request,*args,**kwargs):
        employees=self.model.objects.all()
        self.context["employees"]=employees
        return render(request, self.template_name, self.context)

class EmpProfileView(DetailView):
    model=MyEmp
    template_name="empdetails.html"
    context_object_name ="emp"

class EmpEditView(UpdateView):
    model=MyEmp
    form_class = EmployeeRegistrationForm
    template_name = "empedit.html"
    success_url = reverse_lazy("list")

class EmployeeFilterView(TemplateView):
    def post(self,request,*args,**kwargs):
        search=request.POST.get('search',None)
        if search:
            employees=MyEmp.objects.filter((Q(first_name=search) | Q(department=search) | Q(id=search)))

            return render(request, "filter.html",{'employees':employees})
        return render(request, "filter.html")
