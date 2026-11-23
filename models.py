
from django.db import models
from django.conf import settings
import uuid


class Complaint(models.Model):

    CATEGORY_CHOICES = [
        ('women_safety', 'Women Safety'),
        ('student_rights', 'Student Rights'),
        ('citizen_rights', 'Citizen Rights'),
        ('social_justice', 'Social Justice'),
        ('other', 'Other'),
    ]

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_review', 'In Review'),
        ('resolved', 'Resolved'),
        ('rejected', 'Rejected'),
    ]

    tracking_id = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    name = models.CharField(max_length=100)
    email = models.EmailField()

    category = models.CharField(
        max_length=30,
        choices=CATEGORY_CHOICES
    )

    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    # AI Complaint Analysis Fields

    ai_category = models.CharField(
        max_length=30,
        choices=CATEGORY_CHOICES,
        blank=True
    )

    ai_priority = models.CharField(
        max_length=10,
        choices=[
            ('high', 'High'),
            ('medium', 'Medium'),
            ('normal', 'Normal'),
        ],
        default='normal'
    )

    ai_summary = models.TextField(blank=True)
        # AI Complaint Sentiment & Emotion Detection

    ai_sentiment = models.CharField(
        max_length=20,
        choices=[
            ('negative', 'Negative'),
            ('neutral', 'Neutral'),
            ('positive', 'Positive'),
        ],
        default='neutral'
    )

    ai_emotion = models.CharField(
        max_length=20,
        choices=[
            ('fear', 'Fear'),
            ('anger', 'Anger'),
            ('distress', 'Distress'),
            ('sadness', 'Sadness'),
            ('neutral', 'Neutral'),
        ],
        default='neutral'
    )

    suggested_department = models.CharField(
        max_length=150,
        blank=True
    )

    # Smart Complaint Routing Field

    assigned_department = models.CharField(
        max_length=150,
        blank=True,
        default=''
    )

    # AI Duplicate Complaint Detection

    is_possible_duplicate = models.BooleanField(
        default=False
    )

    duplicate_of = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='duplicate_complaints'
    )

    duplicate_reason = models.TextField(blank=True)

    def __str__(self):
        return f"{self.title} - {self.tracking_id}"


class EmergencyContact(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='emergency_contacts'
    )

    contact_name = models.CharField(max_length=100)

    phone_number = models.CharField(max_length=15)

    relationship = models.CharField(
        max_length=50,
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.contact_name} - {self.phone_number}"

class LiveLocation(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='live_locations'
    )

    share_token = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False
    )

    latitude = models.DecimalField(
        max_digits=10,
        decimal_places=7
    )

    longitude = models.DecimalField(
        max_digits=10,
        decimal_places=7
    )

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Live Location - {self.user}"
