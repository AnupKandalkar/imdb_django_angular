from django.conf.urls import include, url
from django.contrib import admin
from movies import views
urlpatterns = [
    
    url(r'^movies/$', views.MoviesList.as_view()),
    url(r'^movies/(?P<pk>[0-9]+)/$', views.MoviesDetail.as_view()),
    url(r'^genre/$', views.GenreList.as_view()),
    url(r'^genre/(?P<pk>[0-9]+)/$', views.GenreDetails.as_view()),

]