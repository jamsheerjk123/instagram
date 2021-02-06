from django.urls import path
from accounts import views



urlpatterns=[
    path('login/',views.login_view,name='login'),
    path('signup/',views.RegisterView.as_view(),name='register'),
    path('signout/',views.signout,name="signout"),
    path('activate/<uidb64><token>/',views.activate)
]