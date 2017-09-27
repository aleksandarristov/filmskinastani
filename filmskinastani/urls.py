from django.conf.urls import url
from .import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register',  views.register_view, name='register'),
    url(r'^login$',    views.login_view,    name='login'),
    url(r'^logout$',   views.logout_view,   name='logout'),
    url(r'^about$',    views.about_view,    name='about'),
    url(r'^forum$',    views.forum_view,    name='forum'),
]