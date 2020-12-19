from django.urls import path
from . import views


urlpatterns = [
    path('', views.Login, name="Login"),
    path('Home', views.Home, name="Home"),
    path('Profile/', views.Profile, name="Profile"),
    path('Family/', views.Family, name="Family"),
    path('Rubber/', views.Rubber_Farm, name="Rubber"),
    path('Profile_Home', views.Profile_Home, name="Profile_Home"),
    path('Main_Home/', views.Main_Home, name="Main_Home"),
    path('Animal/', views.Animal, name="Animal"),
    path('Vegitable_Fruits/', views.Veg_Fru, name="Veg_Fru"),
    path('Fish/', views.Fish_Farm, name="Fish"),
    path('Survey/', views.Survey_Data, name="Survey"),
    path('Contact/', views.Contact, name="Contact"),
    path('UpdateFamily/', views.updateFamily, name="updateFamily"),
    path('UpdateRubber/', views.updateRubber, name="updateRubber"),
    path('UpdateFish/', views.updateFish, name="updateFish"),
    path('UpdateDomestic/', views.updateDomestic, name="updateDomestic"),
    path('UpdateVegFru/', views.updateVegFru, name="updateVegFru"),
    path('UpdateProfile/', views.updateprofile, name="updateprofile"),
    path('Logout/',views.Logout,name='Logout'),
    path('Change_Password/',views.Passwordupdate,name='Passwordupdate'),
]

handler404 = views.handler404
handler500 = views.handler500
