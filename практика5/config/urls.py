from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from apps.accounts.views import UserViewSet
from apps.tickets.views import TicketViewSet, CategoryViewSet, CommentViewSet
from apps.reports.views import SummaryReportView, StatusReportView, PriorityReportView, HealthView

router = DefaultRouter()
router.register("users", UserViewSet, basename="user")
router.register("tickets", TicketViewSet, basename="ticket")
router.register("categories", CategoryViewSet, basename="category")
router.register("comments", CommentViewSet, basename="comment")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("api/reports/summary/", SummaryReportView.as_view(), name="report-summary"),
    path("api/reports/by-status/", StatusReportView.as_view(), name="report-status"),
    path("api/reports/by-priority/", PriorityReportView.as_view(), name="report-priority"),
    path("api/health/", HealthView.as_view(), name="health"),
    path("api-auth/", include("rest_framework.urls")),
]
