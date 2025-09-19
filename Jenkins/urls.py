from django.contrib import admin
from django.urls import path
from myapp.views import home,viewall
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('all/',viewall,name='all'),
    path('all/<int:pk>/',viewall,name='all'),
]
