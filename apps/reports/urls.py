from django.urls import path
from .views import KPIView, RevenueView, TopModelsView, ManagerLoadView, StockView
app_name = "reports"
urlpatterns = [
    path("kpi/", KPIView.as_view(), name="kpi"),
    path("revenue/", RevenueView.as_view(), name="revenue"),
    path("top-models/", TopModelsView.as_view(), name="top_models"),
    path("manager-load/", ManagerLoadView.as_view(), name="manager_load"),
    path("stock/", StockView.as_view(), name="stock"),
]
