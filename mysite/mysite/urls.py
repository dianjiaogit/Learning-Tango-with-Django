from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from myapp import views

urlpatterns = [
url(r'^$', views.index, name='index'),
url(r'^myapp/', include('myapp.urls')),
# 上面的映射把以 myapp/ 开头的 URL 交给 myapp 应用处理
url(r'^admin/', admin.site.urls),
]
