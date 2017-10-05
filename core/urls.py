from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.enter),
    url(r'^login/', views.login_error),
    url(r'^home/', views.home),
    url(r'^logout/', views.logout_view)
]