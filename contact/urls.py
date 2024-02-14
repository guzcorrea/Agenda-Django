from django.urls import path
from contact import views


app_name = 'contact'



urlpatterns = [
    
    #contact (CRUD)
    
    path('',views.index, name='index' ), #type:ignore
    path('search/',views.search, name='search' ), #type:ignore
    
    path('contact/<int:contact_id>/',views.contact, name='contact' ), #type:ignore
    path('contact/create/',views.create, name='create' ), #type:ignore
]
