from django.contrib import admin
from django.urls import path

from sentiment_analyser.views import review_view, review_added_view, ratings_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', review_view),
    path('review', review_view),
    path('review_added', review_added_view),
    path('ratings', ratings_view)
]