#'django.contrib.auth.views.logout', {'next_page': '/'}, name='auth_logout'
from django.contrib.auth import views as auth_views

from . import views


from django.conf.urls import url
#from accounts.views import(login_view,register_view)



urlpatterns = [


    url(r'^logout/$',auth_views.logout, {'next_page': '/accounts/home'}, name='logout'),
    url(r'^home/$',views.login_view, name='login'),
    url(r'^show/$',views.show, name='show'),
    url(r'^(?P<idd>[0-9]+)/edit/$',views.edit, name='edit'),
]
