from django.contrib import admin
from django.urls import path, include  # Tu dodaliśmy import 'include'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),  # To przekierowuje ruch do naszej aplikacji core
]