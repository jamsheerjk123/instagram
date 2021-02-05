from django.urls import path
from accounts import views



urlpatterns=[
    path('login/',views.login_view),
    path('signup/',views.sign_up),
    path('signout/',views.signout,name="signout")
]