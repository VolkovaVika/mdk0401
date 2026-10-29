import os
import requests
import pandas as pd
import streamlit as st

API_BASE = os.getenv("API_BASE_URL", "http://127.0.0.1:8000/api/reports").rstrip("/")
st.set_page_config(page_title="Автосалон — аналитика", page_icon="🚗", layout="wide")
st.title("🚗 Панель аналитики автосалона")
st.caption("Данные загружаются из Django REST API. Для просмотра отчётов войдите в систему.")

with st.sidebar:
    st.header("Подключение")
    api_base = st.text_input("URL API отчётов", API_BASE)
    token = st.text_input("JWT access token", type="password")
    days = st.slider("Период (дней)", min_value=7, max_value=365, value=30, step=7)
    refresh = st.button("Обновить данные")

headers = {"Authorization": f"Bearer {token}"} if token else {}
def get_data(endpoint, params=None):
    try:
        response = requests.get(f"{api_base}/{endpoint}/", headers=headers, params=params, timeout=8)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as exc:
        st.warning(f"Не удалось загрузить {endpoint}: {exc}")
        return None

if not token:
    st.info("Введите access token из POST /api/auth/login/ или /api/token/, чтобы загрузить защищённые отчёты.")
else:
    kpi = get_data("kpi", {"days": days})
    if isinstance(kpi, dict):
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Заказов за период", kpi.get("orders_total", 0))
        c2.metric("Завершено", kpi.get("orders_completed", 0))
        c3.metric("Выручка", f'{float(kpi.get("revenue", 0)):,.2f}')
        c4.metric("Авто в наличии", kpi.get("cars_available", 0))

    left, right = st.columns(2)
    with left:
        st.subheader("Выручка по дням")
        revenue = get_data("revenue", {"days": days})
        if isinstance(revenue, list) and revenue:
            df = pd.DataFrame(revenue)
            df["date"] = pd.to_datetime(df["date"])
            st.line_chart(df.set_index("date")["revenue"])
            st.dataframe(df, use_container_width=True)
        elif revenue == []:
            st.write("За выбранный период завершённых заказов нет.")
    with right:
        st.subheader("Популярные модели")
        models = get_data("top-models")
        if isinstance(models, list) and models:
            st.dataframe(pd.DataFrame(models), use_container_width=True)
        elif models == []:
            st.write("Пока нет завершённых продаж.")

    left, right = st.columns(2)
    with left:
        st.subheader("Загрузка менеджеров")
        managers = get_data("manager-load", {"days": days})
        if isinstance(managers, list) and managers:
            st.bar_chart(pd.DataFrame(managers).set_index("manager")[["total", "completed"]])
        elif managers == []:
            st.write("Нет заказов за период.")
    with right:
        st.subheader("Склад автомобилей")
        stock = get_data("stock")
        if isinstance(stock, list) and stock:
            st.bar_chart(pd.DataFrame(stock).set_index("label")["count"])
            st.dataframe(pd.DataFrame(stock), use_container_width=True)
