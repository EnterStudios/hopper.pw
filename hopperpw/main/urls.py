# coding=utf-8
from api.views import (
    MyIpView, DetectIpView, NicUpdateView, AuthorizedNicUpdateView)
from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from main.views import (
    HomeView, OverviewView, HostView, DeleteHostView, AboutView, HelpView,
    GenerateSecretView, DomainOverwievView, DeleteDomainView, ThankYouView,
    RegistrationSuccessView
)
from stats.views import StatsView


urlpatterns = patterns(
    '',
    url(r'^$', HomeView.as_view(), name="home"),
    url(r'^about/$', AboutView.as_view(), name="about"),
    url(r'^thank_you/$', ThankYouView.as_view(), name="thank_you"),
    url(r'^welcome/$', RegistrationSuccessView.as_view(), name="welcome"),
    url(r'^legal/$',
        TemplateView.as_view(template_name='main/legal.html'), name="legal"),
    url(r'^help/$', HelpView.as_view(), name="help"),
    url(r'^stats/$', StatsView.as_view(), name="stats"),
    url(r'^overview/$', OverviewView.as_view(), name='overview'),
    url(r'^host/(?P<pk>\d+)/$', HostView.as_view(), name='host_view'),
    url(r'^generate_secret/(?P<pk>\d+)/$',
        GenerateSecretView.as_view(), name='generate_secret_view'),
    url(r'^host/(?P<pk>\d+)/delete/$',
        DeleteHostView.as_view(), name='delete_host'),
    url(r'^domain_overview/$',
        DomainOverwievView.as_view(), name='domain_overview'),
    url(r'^domain/(?P<pk>\d+)/delete/$',
        DeleteDomainView.as_view(), name='delete_domain'),
    url(r'^myip$', MyIpView),
    url(r'^detectip/$', DetectIpView),
    url(r'^detectip/(?P<secret>\w+)/$', DetectIpView),
    url(r'^nic/update$', NicUpdateView),
    url(r'^nic/update_authorized$',
        AuthorizedNicUpdateView, name='nic_update_authorized'),
)
