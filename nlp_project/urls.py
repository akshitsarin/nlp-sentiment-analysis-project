from django.contrib import admin
from django.urls import path

from sentiment_analyser.views import home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view)
]