from exam import views
from django.urls import path,re_path


urlpatterns = [
    re_path('^$',views.home),
    re_path('first',views.first)
]
