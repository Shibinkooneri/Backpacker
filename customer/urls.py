from django.urls import path
from .views import UserView,Proview,Editprofile,Delview,Delpro,DelPic,RoomView

urlpatterns=[
    path('Home',UserView.as_view(),name='userhome'),
    path('profile',Proview.as_view(),name='profile'),
    path('eprofile',Editprofile.as_view(),name='editpro'),
    path('del/<int:id>',Delview.as_view(),name='del'),
    path('delp/<int:id>',Delpro.as_view(),name='delprofile'),
    path('delpic/<int:id>',DelPic.as_view(),name='delpic'),
    path('room/<slug:slug>/',RoomView.as_view(),name='room')

]