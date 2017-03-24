from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^register$', views.register, name='register'),
    url(r'^login$', views.login, name='login'),
    url(r'^quotes$', views.quotes, name='quotes'),
    url(r'^user_display/(?P<user_id>\d+)$', views.user_display, name='user_display'),
    url(r'^logout$', views.logout, name='logout'),
    url(r'^post_quote$', views.post_quote, name='post_quote'),
    url(r'^add_favorite/(?P<quote_id>\d+)$', views.add_favorite, name='add_favorite'),
    url(r'^remove_favorite/(?P<quote_id>\d+)$', views.remove_favorite, name='remove_favorite'),
]