from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from . import views

app_name = 'game'
urlpatterns = [
    path('', views.index, name='index'),
    path('scores', views.player_score, name='player_score'),

    path('game/', views.new_game, name='game'),
    path('game_play/<int:pk>/', views.game_play, name='game_play'),
    path('get_tiles/<int:pk>/', views.get_tiles, name='get_tiles'),
    path('set_finished/', views.set_finished, name='set_finished'),

    path('testing_place/', views.testing_place, name='testing_place'),
    # path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
]
