from datetime import timedelta
from django.db.models import Sum, Count, Avg
from django.db.models.functions import TruncDate
from django.utils import timezone
from apps.catalog.models import Car
from apps.orders.models import Order

def date_from_days(days=30):
    return timezone.now() - timedelta(days=max(1, min(int(days), 3650)))

def get_kpi(days=30):
    since = date_from_days(days)
    orders = Order.objects.filter(created_at__gte=since)
    completed = orders.filter(status=Order.Status.COMPLETED)
    return {
        "period_days": int(days),
        "orders_total": orders.count(),
        "orders_completed": completed.count(),
        "revenue": completed.aggregate(total=Sum("price"))["total"] or 0,
        "average_check": completed.aggregate(avg=Avg("price"))["avg"] or 0,
        "clients_total": __import__("apps.clients.models", fromlist=["Client"]).Client.objects.count(),
        "cars_available": Car.objects.filter(status=Car.Status.AVAILABLE).count(),
    }

def get_revenue(days=30):
    since = date_from_days(days)
    qs = (Order.objects.filter(status=Order.Status.COMPLETED, created_at__gte=since)
          .annotate(date=TruncDate("completed_at"))
          .values("date").annotate(revenue=Sum("price"), orders=Count("id")).order_by("date"))
    return [{"date": row["date"].isoformat() if row["date"] else None,
             "revenue": float(row["revenue"] or 0), "orders": row["orders"]} for row in qs]

def get_top_models():
    qs = (Order.objects.filter(status=Order.Status.COMPLETED)
          .values("car__brand__name", "car__model")
          .annotate(sales=Count("id"), revenue=Sum("price"))
          .order_by("-sales")[:10])
    return [{"brand": x["car__brand__name"], "model": x["car__model"],
             "sales": x["sales"], "revenue": float(x["revenue"] or 0)} for x in qs]

def get_manager_load(days=30):
    since = date_from_days(days)
    qs = (Order.objects.filter(created_at__gte=since)
          .values("manager__username", "manager__first_name", "manager__last_name")
          .annotate(total=Count("id"), completed=Count("id", filter=__import__("django.db.models", fromlist=["Q"]).Q(status=Order.Status.COMPLETED)))
          .order_by("-total"))
    return [{"manager": (f'{x["manager__first_name"]} {x["manager__last_name"]}'.strip()
                         or x["manager__username"]), "total": x["total"], "completed": x["completed"]}
            for x in qs]

def get_stock():
    qs = (Car.objects.values("status").annotate(count=Count("id")).order_by("status"))
    return [{"status": x["status"], "label": dict(Car.Status.choices).get(x["status"], x["status"]),
             "count": x["count"]} for x in qs]
