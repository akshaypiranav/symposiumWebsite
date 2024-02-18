"""SymphosiumWebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from APP import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.index,name="index"),
    path("events",views.events,name="events"),
    path("conference",views.conference,name="conference"),
    path("hackathon",views.hackathon,name="hackathon"),
    path("symphosium",views.symphosium,name="symphosium"),
    path("add",views.add,name="add"),
    path("login",views.login,name="login"),
    path("register/",views.register,name="register"),
    path("details/<int:id>",views.details,name="details"),
    path("profile/<int:id>",views.profile,name="profile"),
    path('clearSession', views.clearSession, name='clearSession'),
    path("update/<int:id>",views.update,name="update"),
    path("delete/<int:id>",views.delete,name="delete"),
    path("notify",views.notify,name="notify"),
    path("faq",views.faq,name="faq"),
    path("verify",views.verify,name="verify"),
    path("deleteMyEmail",views.deleteMyEmail,name="deleteMyEmail")
    

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

LOGIN_REDIRECT_URL="add"
LOGIN_URL="login"

