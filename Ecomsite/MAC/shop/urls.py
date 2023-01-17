from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="Shophome"),
    path("aboutus/",views.aboutus,name="aboutus"),
    path("contact/",views.contact,name="ContactUs"),
    path("tracker",views.tracker,name="TrackingStatus"),
    path("search",views.search,name="search"),
    path("productview",views.productview,name="ProductView"),
    path("checkout",views.checkout,name="checkout"),
]