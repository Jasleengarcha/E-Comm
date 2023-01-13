from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('signin/', signin),
    path('signup/', signup),
    path('user-detail/', user_details),
    path('healthy-food/', healthy_food),
    path('logout/', logout_view)

]
