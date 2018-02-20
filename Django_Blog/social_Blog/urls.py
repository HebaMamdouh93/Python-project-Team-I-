
#from django.conf.urls import include, url
from django.conf.urls import include, url ,patterns
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    url(r'^home/$', views.home),

    url(r'^(?P<cat_id>[0-9]+)/showCatPosts/$',views.showCatPosts),

    url(r'^dashbord/$', views.adminhome, name='dashbord'),


    url(r'^post/(?P<post_id>[0-9]+)$', views.getPost),
    url(r'^comment/(?P<comment_id>[0-9]+)/(?P<post_id>[0-9]+)$', views.reply),
    url(r'^post/addLike/(?P<post_id>[0-9]+)$', views.addLike),  
    url(r'^post/DisLike/(?P<post_id>[0-9]+)$', views.DisLike), 

    url(r'^posts/$', views.allpost, name='posts'),
    url(r'^posts/(?P<postId>[0-9]+)/update$', views.editpost),
    url(r'^posts/(?P<postId>[0-9]+)/delete$', views.delete),
    url(r'^posts/create$',  views.createpost, name="create"),

    url(r'^categorys/$', views.allcats, name='cats'),
    url(r'^categorys/(?P<catId>[0-9]+)/update$', views.editcat),
    url(r'^categorys/(?P<catId>[0-9]+)/delete$', views.deletecat),
    url(r'^categorys/create$',  views.createcat, name="createcat"),

    url(r'^tags/$', views.alltags, name='tags'),
    url(r'^tags/(?P<tagId>[0-9]+)/update$', views.edittag),
    url(r'^tags/(?P<tagId>[0-9]+)/delete$', views.deletetag),
    url(r'^tags/create$',  views.createtag, name="createtag"),

    url(r'^forbiddenwords/$', views.allwords, name='words'),
    url(r'^forbiddenwords/(?P<wordId>[0-9]+)/update$', views.editword),
    url(r'^forbiddenwords/(?P<wordId>[0-9]+)/delete$', views.deleteword),
    url(r'^forbiddenwords/create$', views.createword, name="createword"),

    url(r'^users/$', views.allusers, name='users'),
    url(r'^users/(?P<userId>[0-9]+)/update$', views.edituser, name="edituser"),
    url(r'^users/(?P<userId>[0-9]+)/delete$', views.deleteuser),
    url(r'^users/create$',  views.createuser, name="createuser"),

    url(r'^users/block$',  views.block, name="block"),
    url(r'^users/promottoadmin$',  views.promottoadmin, name="promottoadmin"),


    url(r'^tags/create_ajax$',  views.createtagAjax, name="ajax_create"),

]

