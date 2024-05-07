

from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect #다른 주소로 넘기기
urlpatterns = [
    path('admin/', admin.site.urls),
    path('myapp/', include('myapp.urls')),
    path('', view=lambda request: redirect('/myapp/'))
]