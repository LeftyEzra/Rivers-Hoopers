from django.urls import path
from . import views


#Api urls
#from .views import CompetitionListAPI, CompetitionDetailAPI, GameScheduleListAPI, GameScheduleDetailAPI

urlpatterns = [
                #Extras
                path('', views.home, name='home'),


               ]