
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    # Complaint System
    path(
        'complaint/',
        views.submit_complaint,
        name='submit_complaint'
    ),
    path(
        'track-complaint/',
        views.track_complaint,
        name='track_complaint'
    ),

    # Admin Dashboard
    path(
        'admin-dashboard/',
        views.admin_dashboard,
        name='admin_dashboard'
    ),
    path(
        'assign-department/<int:complaint_id>/',
        views.assign_department,
        name='assign_department'
    ),
    path(
        'update-status/<int:complaint_id>/',
        views.update_complaint_status,
        name='update_complaint_status'
    ),

    # AI Legal Assistant
    path(
        'legal-assistant/',
        views.legal_assistant,
        name='legal_assistant'
    ),

    # Citizen Authentication
    path(
        'citizen/register/',
        views.citizen_register,
        name='citizen_register'
    ),
    path(
        'citizen/login/',
        views.citizen_login,
        name='citizen_login'
    ),
    path(
        'citizen/logout/',
        views.citizen_logout,
        name='citizen_logout'
    ),

    # Emergency Contacts
    path(
        'emergency-contacts/',
        views.emergency_contacts,
        name='emergency_contacts'
    ),
   
    path(
        'delete-emergency-contact/<int:contact_id>/',
        views.delete_emergency_contact,
        name='delete_emergency_contact'
    ),

    # Live Location Sharing
    path(
        'live-location/start/',
        views.start_live_location,
        name='start_live_location'
    ),
    path(
        'live-location/update/<uuid:token>/',
        views.update_live_location,
        name='update_live_location'
    ),
    path(
        'live-location/stop/<int:location_id>/',
        views.stop_live_location,
        name='stop_live_location'
    ),
    path(
        'live-location/view/<uuid:token>/',
        views.view_live_location,
        name='view_live_location'
    ),
]
