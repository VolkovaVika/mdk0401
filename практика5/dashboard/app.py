import os
import requests
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Help Desk — панель управления", page_icon="🎫", layout="wide")
st.title("🎫 Help Desk — панель управления")
st.caption("Учебная система централизованной регистрации и обработки обращений")

api_url = st.sidebar.text_input("Адрес API", os.getenv("HELPDESK_API_URL", "http://127.0.0.1:8000/api")).rstrip("/")
username = st.sidebar.text_input("Имя пользователя", "demo_operator")
password = st.sidebar.text_input("Пароль", "HelpDesk123!", type="password")

def get_api(path):
    try:
        response = requests.get(f"{api_url}/{path}", auth=(username, password), timeout=5)
        response.raise_for_status()
        return response.json(), None
    except requests.RequestException as exc:
        return None, str(exc)

summary, error = get_api("reports/summary/")
if error:
    st.error("Не удалось получить данные от API. Убедитесь, что Django запущен и выполнена команда seed_demo.")
    st.code(error)
    st.stop()

cols = st.columns(4)
metrics = [
    ("Всего заявок", summary.get("total", 0)),
    ("Новые", summary.get("new", 0)),
    ("В работе", summary.get("in_progress", 0)),
    ("Критические", summary.get("critical", 0)),
]
for col, (label, value) in zip(cols, metrics):
    col.metric(label, value)

left, right = st.columns(2)
status_data, status_error = get_api("reports/by-status/")
priority_data, priority_error = get_api("reports/by-priority/")
with left:
    st.subheader("Заявки по статусам")
    if status_data:
        df = pd.DataFrame(status_data)
        st.bar_chart(df.set_index("label")["count"])
    else:
        st.info("Нет данных по статусам.")
with right:
    st.subheader("Заявки по приоритетам")
    if priority_data:
        df = pd.DataFrame(priority_data)
        st.bar_chart(df.set_index("label")["count"])
    else:
        st.info("Нет данных по приоритетам.")

st.subheader("Список заявок")
tickets, ticket_error = get_api("tickets/?page_size=100")
if ticket_error:
    st.warning("Не удалось загрузить список заявок.")
else:
    rows = tickets.get("results", tickets if isinstance(tickets, list) else [])
    if rows:
        display_fields = {
            "id": "№", "title": "Тема", "requester_name": "Заявитель",
            "assignee_name": "Исполнитель", "category_name": "Категория",
            "status_display": "Статус", "priority_display": "Приоритет",
            "created_at": "Создана",
        }
        df = pd.DataFrame(rows)
        keep = [key for key in display_fields if key in df.columns]
        st.dataframe(df[keep].rename(columns=display_fields), use_container_width=True, hide_index=True)
    else:
        st.info("Заявок пока нет.")

st.caption("Для управления заявками, пользователями и категориями используйте Django Admin: /admin/.")
