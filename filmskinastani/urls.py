from django.conf.urls import url
from .import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register',  views.register_view, name='register'),
    url(r'^login$',    views.login_view,    name='login'),
    url(r'^logout$',   views.logout_view,   name='logout'),
    url(r'^about$',    views.about_view,    name='about'),
    url(r'^forum$',    views.forum_view,    name='forum'),
    url(r'^add-movie$', views.movie_form_view, name='movie_form'),
    url(r'^add-actor$', views.movie_actor_view, name='actor_form'),
    url(r'^add-award$', views.movie_award_view, name='award_form'),
    url(r'^add-producent$', views.movie_producent_view, name='producent_form'),
    url(r'^profile$', views.profile_view, name='profile'),
]