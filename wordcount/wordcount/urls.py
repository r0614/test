from django.contrib import admin
from wcount import views
from django.conf.urls import include, url


urlpatterns = [
    url(r'^admin/', admin.site.urls),
     url(r'^$', views.show),
      url(r'^add/', views.add),
]
