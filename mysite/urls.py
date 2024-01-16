
from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "Port Scanner Admin"
admin.site.site_title = "Port Scanner Admin Portal"
admin.site.index_title = "Welcome to Port Scanner Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls'))
]
