from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

# Try to import models if they exist; otherwise use None and provide safe fallbacks
try:
    from .models import Notification, Announcement, Badge
except Exception:
    Notification = None
    Announcement = None
    Badge = None

@login_required
def notifications_list(request):
    """
    Main list: all notifications (read + unread) for the user.
    """
    if Notification:
        qs = Notification.objects.filter(user=request.user).order_by('-created_at')
    else:
        qs = []  # fallback: empty list
    context = {"notifications": qs}
    return render(request, "notifications/notifications_list.html", context)


@login_required
def notification_detail(request, pk):
    """
    Detail view for a single notification.
    Mark as read if a model supports it.
    """
    if Notification:
        notif = get_object_or_404(Notification, pk=pk, user=request.user)
        # optional: mark read if field exists
        if hasattr(notif, "is_read") and not notif.is_read:
            notif.is_read = True
            notif.save(update_fields=["is_read"])
    else:
        # fallback object for template (simple dict)
        notif = {"title": "Sample notification", "message": "Details not available (model missing)."}
    return render(request, "notifications/notification_detail.html", {"notification": notif})


@login_required
def unread_notifications(request):
    """
    Return only unread notifications. Good for notifications dropdown or dedicated page.
    """
    if Notification:
        qs = Notification.objects.filter(user=request.user, is_read=False).order_by('-created_at')
    else:
        qs = []
    return render(request, "notifications/unread_notifications.html", {"notifications": qs})


@login_required
def notification_dropdown(request):
    """
    Partial/fragment to include in navbar.
    Typically returns N latest notifications (limit).
    """
    limit = 6
    if Notification:
        qs = Notification.objects.filter(user=request.user).order_by('-created_at')[:limit]
    else:
        qs = []
    # This template is intended to be included (e.g., in base.html navbar)
    return render(request, "notifications/notification_dropdown.html", {"notifications": qs})


@login_required
def system_announcements(request):
    """
    Platform-wide announcements (non-user-specific).
    """
    if Announcement:
        qs = Announcement.objects.filter(active=True).order_by('-published_at')
    else:
        qs = []
    return render(request, "notifications/system_announcements.html", {"announcements": qs})


@login_required
def achievement_notifications(request):
    """
    Show achievement/badge related notifications or earned badges.
    """
    if Badge:
        badges = Badge.objects.filter(user=request.user).order_by('-awarded_at')
    else:
        badges = []
    return render(request, "notifications/achievement_notifications.html", {"badges": badges})


@login_required
def notification_settings(request):
    """
    User settings for notifications (toggle email/push, frequency etc.)
    For now renders a page; later handle POST to save preferences.
    """
    # If you have a user profile with notification preferences, pass it here.
    prefs = getattr(request.user, "notification_preferences", None)
    return render(request, "notifications/settings.html", {"preferences": prefs})
