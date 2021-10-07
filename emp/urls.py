from django.urls import path
from .views import SignInView,EmpCreationView,EmpListView,EmpProfileView,EmpEditView,Home,sign_out,EmployeeFilterView,EmpDeleteView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("login",SignInView.as_view() , name="login"),
    path("logout",sign_out , name="logout"),
    path("register",login_required(EmpCreationView.as_view() ,login_url='login'), name="register"),
    path("list", EmpListView.as_view() , name="list"),
    path("profile/<int:id>",login_required( EmpProfileView.as_view(),login_url='login'),name="profile"),
    path("profileedit/<int:id>",login_required( EmpEditView.as_view(),login_url='login'),name="profileedit"),
    path("home",login_required(Home.as_view(),login_url='login') , name="home"),
    path("search",login_required( EmployeeFilterView.as_view() ,login_url='login'), name="search"),
    # path("notification",bday_alert ,name="alerts"),
    path("remove/<int:pk>",EmpDeleteView.as_view(),name="remove")

]