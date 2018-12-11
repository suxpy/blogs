from django.conf.urls import url
from django.contrib import admin
from backweb import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/', views.login),
    url(r'^index/', views.index),
    url(r'^article/', views.article, name='article_list'),
    url(r'^add_article/', views.add_article),

]