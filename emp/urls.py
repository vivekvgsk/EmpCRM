from django.urls import path
from .views import SignInView,EmpCreationView,EmpListView,EmpProfileView,EmpEditView,Home,LogOutView,EmployeeFilterView
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path("login",SignInView.as_view() , name="login"),
        path("logout",LogOutView.as_view() , name="logout"),

    path("register",EmpCreationView.as_view() , name="register"),
    path("list",EmpListView.as_view() , name="list"),
    path("profile/<int:pk>",EmpProfileView.as_view(),name="profile"),
    path("profileedit/<int:pk>",EmpEditView.as_view(),name="profileedit"),
    path("home",Home.as_view() , name="home"),
    path("search",EmployeeFilterView.as_view() , name="search")

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)