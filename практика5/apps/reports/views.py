from django.db.models import Count
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.tickets.models import Ticket

class SummaryReportView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        qs = Ticket.objects.all()
        return Response({
            "total": qs.count(),
            "new": qs.filter(status=Ticket.Status.NEW).count(),
            "in_progress": qs.filter(status=Ticket.Status.IN_PROGRESS).count(),
            "waiting": qs.filter(status=Ticket.Status.WAITING).count(),
            "resolved": qs.filter(status=Ticket.Status.RESOLVED).count(),
            "closed": qs.filter(status=Ticket.Status.CLOSED).count(),
            "unassigned": qs.filter(assignee__isnull=True).count(),
            "critical": qs.filter(priority=Ticket.Priority.CRITICAL).count(),
        })

class StatusReportView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        data = Ticket.objects.values("status").annotate(count=Count("id")).order_by("status")
        labels = dict(Ticket.Status.choices)
        return Response([{"status": x["status"], "label": labels.get(x["status"], x["status"]), "count": x["count"]} for x in data])

class PriorityReportView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        data = Ticket.objects.values("priority").annotate(count=Count("id")).order_by("priority")
        labels = dict(Ticket.Priority.choices)
        return Response([{"priority": x["priority"], "label": labels.get(x["priority"], x["priority"]), "count": x["count"]} for x in data])

class HealthView(APIView):
    permission_classes = []
    authentication_classes = []
    def get(self, request):
        return Response({"status": "ok", "service": "Help Desk API"})
