from django.urls import path

from . import views

urlpatterns = [
    path("roomShow/<int:id>", views.index, name="index"),
    path("", views.home, name="home"),
    path("profile/", views.profile, name="profile"),
    path("home/", views.home, name="home"),
    path("view/", views.view, name="view"),
    #path("login/", ),
    path("reserve/", views.reserve, name="reserve"),
    path("reserve/roomShow/", views.roomShow, name="roomShow"),
    path("roomShow/<int:id>/checkout/", views.checkOut, name="checkOut"),
    path("profile/update/<int:id>", views.modifyInfo, name = "Update Profile")
]