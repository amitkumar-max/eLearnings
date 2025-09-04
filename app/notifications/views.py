from django.shortcuts import render
from django.views import View
from .models import Notification

class NotificationListView(View):
    def get(self, request):
        notifications = Notification.objects.filter(user=request.user)
        return render(request, 'notifications/notification_list.html', {'notifications': notifications})
