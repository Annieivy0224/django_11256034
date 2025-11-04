from django.contrib import admin
from django.urls import path

from whoamI import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('whoamI/', views.whoamI, name='index'),
]