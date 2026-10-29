from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .services import get_kpi, get_revenue, get_top_models, get_manager_load, get_stock

class ReportsBaseView(APIView):
    permission_classes = [IsAuthenticated]
    def days(self, request):
        try:
            return max(1, min(int(request.query_params.get("days", 30)), 3650))
        except (TypeError, ValueError):
            return 30

class KPIView(ReportsBaseView):
    def get(self, request):
        return Response(get_kpi(self.days(request)))

class RevenueView(ReportsBaseView):
    def get(self, request):
        return Response(get_revenue(self.days(request)))

class TopModelsView(ReportsBaseView):
    def get(self, request):
        return Response(get_top_models())

class ManagerLoadView(ReportsBaseView):
    def get(self, request):
        return Response(get_manager_load(self.days(request)))

class StockView(ReportsBaseView):
    def get(self, request):
        return Response(get_stock())
