from django.urls import path

from . import views

urlpatterns = [
    path("roomShow/<int:id>", views.index, name="index"),
    path("", views.home, name="home"),
<<<<<<< HEAD
    path("create/", views.create, name="create"),
    path("profile/", views.profile, name="profile")
=======
    path("home/", views.home, name="home"),
    path("create/", views.create, name="create"),
    path("view/", views.view, name="view"),
    path("reserve/", views.reserve, name="reserve"),
    path("reserve/roomShow/", views.roomShow, name="roomShow"),
    path("reserve/roomShow/checkout", views.checkOut, name="checkOut")
>>>>>>> 216e16a5bb31ce442488143ace4a2e24031257f9
]