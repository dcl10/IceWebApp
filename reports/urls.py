from django.conf.urls import url
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from reports.models import Report

urlpatterns = [
    url(r'^$', login_required(ListView.as_view(queryset=Report.objects.all(), template_name="reports/report_list.html"),
                              login_url="/")),
    url(r'^(?P<pk>\w+)$', login_required(DetailView.as_view(model=Report, template_name="reports/report.html"),
                                         login_url="/"))
]