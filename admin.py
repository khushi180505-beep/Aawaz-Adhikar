
from django.contrib import admin
from .models import Complaint, EmergencyContact


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'name',
        'category',
        'status',
        'created_at',
    )

    list_filter = (
        'status',
        'category',
        'created_at',
    )

    search_fields = (
        'title',
        'name',
        'email',
        'tracking_id',
    )

    readonly_fields = (
        'tracking_id',
        'created_at',
    )

    list_editable = ('status',)

    ordering = ('-created_at',)
@admin.register(EmergencyContact)
class EmergencyContactAdmin(admin.ModelAdmin):

    list_display = (
        'contact_name',
        'phone_number',
        'relationship',
        'user',
        'created_at',
    )

    search_fields = (
        'contact_name',
        'phone_number',
        'user__username',
    )

    list_filter = (
        'relationship',
        'created_at',
    )

    readonly_fields = ('created_at',)