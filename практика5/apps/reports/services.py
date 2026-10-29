from django.db.models import Count
from apps.tickets.models import Ticket

def build_summary():
    """Возвращает основные показатели для отчёта Help Desk."""
    tickets = Ticket.objects.all()
    return {
        "total": tickets.count(),
        "new": tickets.filter(status=Ticket.Status.NEW).count(),
        "in_progress": tickets.filter(status=Ticket.Status.IN_PROGRESS).count(),
        "waiting": tickets.filter(status=Ticket.Status.WAITING).count(),
        "resolved": tickets.filter(status=Ticket.Status.RESOLVED).count(),
        "closed": tickets.filter(status=Ticket.Status.CLOSED).count(),
        "unassigned": tickets.filter(assignee__isnull=True).count(),
    }

def tickets_by_status():
    return list(Ticket.objects.values("status").annotate(count=Count("id")).order_by("status"))
