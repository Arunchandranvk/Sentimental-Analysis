from django.urls import path
from .views import *

urlpatterns = [ 
        path('adminlogin/',LoginView.as_view(),name="log"),
        path('home/',indexadmin,name="h"),
        path('feedback/',Feedback.as_view(),name="feed"),
        path('jobs/',JobAdd.as_view(),name="job"),
]
