from django.urls import path
from . import views

from userpage.views import(
    CreateOwner_view,
    OwnerPage_view,
    UpdateOwner_view,
)



urlpatterns = [
    path('createowner/', CreateOwner_view, name="createowner"),
    path('ownerpage/', OwnerPage_view, name="ownerpage"), 
    path('updateowner/', UpdateOwner_view, name="updateowner"),   
]