from django.contrib import admin
from django.urls import path
from app1.views import My_ModelAPI

urlpatterns = [
    path('admin/', admin.site.urls),
    path('API/', My_ModelAPI.as_view())
]
