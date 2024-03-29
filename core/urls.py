from django.urls import path
from . import views

urlpatterns = [
    path("create/", views.create_event),
    path("update/", views.update_event),
    path("delete/", views.delete_event),
    path("get/id/", views.get_event_by_id),
    path("get/", views.get_events),
    path("get/booked/", views.get_booked_events),
    path("get/created/", views.get_created_events),
    path("get/search/", views.search_events),
    path("get/upcoming/", views.get_upcoming_events),
    path("get/ongoing/", views.get_ongoing_events),
    path("invite/", views.invite),
    path("attend/", views.attend_event),
    path("unbook/", views.unbook_event),
    path("roles/create/", views.create_role),
    path("roles/update/", views.update_role),
    path("roles/delete/", views.delete_role),
    path("roles/assign/", views.assign_role),
    path("roles/unassign/", views.unassign_role),
    path("roles/get/", views.get_roles),
    path("roles/get/id/", views.get_role_by_id),
    path("attendees/get/", views.get_attendees),
    path("attendees/search/", views.search_attendee),
    path("event-types/get/", views.get_event_types),
]
