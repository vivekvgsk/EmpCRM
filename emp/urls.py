from django.urls import path
from .views import SignInView,EmpCreationView,EmpListView,EmpProfileView,EmpEditView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("login",SignInView.as_view() , name="login"),
    path("register",EmpCreationView.as_view() , name="register"),
    path("list",EmpListView.as_view() , name="list"),
    path("profile/<int:pk>",EmpProfileView.as_view(),name="profile"),
    path("profileedit/<int:pk>",EmpEditView.as_view(),name="profileedit")


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)