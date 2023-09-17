from django.urls import path
from .views import SignUpView,SignInView,Lgout
urlpatterns=[
    path('signup',SignUpView.as_view(),name='signup'),
    path('signin',SignInView.as_view(),name='signin'),
    path('lgout',Lgout.as_view(),name='logout')
    ]