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
    path("roomShow/<int:id>/checkout/confirmationPage", views.confirmationPage, name="confirmationPage"),
    #path("profile/update/<int:id>", views.modifyInfo, name = "Update Profile"),
    path("reservations/", views.reservationFunction2, name = "reservations"),
    path("selectRoom/", views.selectRoomTemp, name = "selectRoomTemp"),
    path("viewRoom/", views.viewRoom, name = "viewRoom"),
    path("selectRoom/reservations/", views.reservationFunction2, name = "reservations2"),
    #path("reservations/book/"), views.bookRoomFinal,
    path("selectRoom/reservations/book/<int:id>/<int:start>/<int:end>/", views.bookRoomFinal, name = "booking"),
    path("selectRoomTemp/", views.selectRoomTemp, name = "selectRoomLOL"),
    path("reservations/book/<int:id>/<int:start>/<int:end>/", views.bookRoomFinal, name = "booking"),
    path("selectDate/<int:id>/confirm/", views.calculatePrice, name = "Confirm Order"),
    path("selectDate/<int:id>", views.selectDateOnly, name = "Select Date"),
    path("reservations/invoice/<int:id>/<int:start>/<int:end>", views.calculateInvoice, name = "Invoice")
]