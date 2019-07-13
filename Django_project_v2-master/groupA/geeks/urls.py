from django.conf.urls import url
import views

urlpatterns = [
#post
    url(r'^allcategorys' , views.show_all_categorys),
    url(r'^mainpage',views.show_all_body),
    url(r'^posts/(?P<id>[0-9]+)/show_posts$'  , views.show_posts ),
    url(r'posts/(?P<id>[0-9]+)/details$'  , views.details ),
    url(r'posts/(?P<id>[0-9]+)/newcomment$',views.new_comment),
    url(r'posts/(?P<postid>[0-9]+)/(?P<commentid>[0-9]+)/newreply$',views.new_reply),

    url(r'^subscribe/(?P<cat_id>[0-9]+)/$' , views.subscribe),
	url(r'^unsubscribe/(?P<cat_id>[0-9]+)/$' , views.unsubscribe) ,

#admin
	url(r'^adminuser/user/$', views.show_all_user),
url(r'^contact/$', views.contact),
    url(r'^adminuser/category$' , views.show_allcategorys),
    url(r'^adminuser/(?P<id>[0-9]+)/show_posts/$'  , views.show_posts ),
    #url(r'posts/(?P<id>[0-9]+)/details$'  , views.details ),
    url(r'^adminuser/pnew/$',views.Post_new),
    url(r'^adminuser/(?P<id>[0-9]+)/pdel/$',views.Posts_delete),
    url(r'^adminuser/(?P<id>[0-9]+)/pupdate/$',views.Post_update),
    url(r'(?P<id>[0-9]+)/show/$',views.show_one_user),
    url(r'^adminuser/user/login/$', views.create_user),
    url(r'^adminuser/user/(?P<id>[0-9]+)/delus/$', views.del_user),
    url(r'^adminuser/user/(?P<id>[0-9]+)/upduser/$', views.update),
    url(r'^accounts/chuser/$', views.change),
    #url(r'^$', views.showall_post),
    url(r'^adminuser/(?P<id>[0-9]+)/cat$',views.details_category),
    url(r'^adminuser/(?P<id>[0-9]+)/edit/$',views.edit_category),
    url(r'^showall$',views.show_all_user),
    url(r'^adminuser/(?P<id>[0-9]+)/delc/$',views.del_category),
    url(r'^adminuser/cnew/$',views.category_new),
    url(r'^adminhome/$',views.adminhome),
    url(r'^user$',views.categ),
    url(r'^adminuser/post$',views.showall_post),

    url(r'^showrude/$', views.select_word),
    url(r'^account/create/$', views.create_word),
]
