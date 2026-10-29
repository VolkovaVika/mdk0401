from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from apps.tickets.models import Category, Ticket, Comment

class Command(BaseCommand):
    help = "Создать демонстрационные данные для Help Desk"

    def handle(self, *args, **options):
        User = get_user_model()
        operator, created = User.objects.get_or_create(
            username="demo_operator",
            defaults={"email": "operator@example.com", "first_name": "Демо", "last_name": "Оператор",
                      "role": User.Role.OPERATOR, "is_staff": True}
        )
        if created:
            operator.set_password("HelpDesk123!")
            operator.save()
        agent, _ = User.objects.get_or_create(
            username="demo_agent",
            defaults={"email": "agent@example.com", "first_name": "Иван", "last_name": "Исполнитель",
                      "role": User.Role.AGENT}
        )
        if _:
            agent.set_password("HelpDesk123!")
            agent.save()
        requester, _ = User.objects.get_or_create(
            username="demo_requester",
            defaults={"email": "requester@example.com", "first_name": "Анна", "last_name": "Пользователь",
                      "role": User.Role.REQUESTER}
        )
        if _:
            requester.set_password("HelpDesk123!")
            requester.save()

        admin_user, admin_created = User.objects.get_or_create(
            username="demo_admin",
            defaults={"email": "admin@example.com", "first_name": "Демо", "last_name": "Администратор",
                      "role": User.Role.ADMIN, "is_staff": True, "is_superuser": True}
        )
        if admin_created:
            admin_user.set_password("HelpDesk123!")
            admin_user.save()

        categories = [
            ("Оборудование", "Компьютеры, принтеры и периферия"),
            ("Программное обеспечение", "Установка и ошибки программ"),
            ("Доступы", "Учётные записи и права доступа"),
            ("Сеть", "Интернет и локальная сеть"),
        ]
        category_objects = {}
        for name, desc in categories:
            obj, _ = Category.objects.get_or_create(name=name, defaults={"description": desc})
            category_objects[name] = obj

        demo_tickets = [
            ("Не работает принтер", "Принтер в кабинете не печатает документы.", "Оборудование", "high", "new"),
            ("Установить офисный пакет", "Необходимо установить офисное программное обеспечение.", "Программное обеспечение", "medium", "in_progress"),
            ("Нет доступа к общей папке", "При открытии сетевой папки появляется отказ в доступе.", "Доступы", "critical", "waiting"),
            ("Нестабильное подключение к сети", "Соединение периодически пропадает в течение дня.", "Сеть", "high", "resolved"),
        ]
        for title, description, cat, priority, status in demo_tickets:
            ticket, created = Ticket.objects.get_or_create(
                title=title,
                defaults={"description": description, "requester": requester, "assignee": agent,
                          "category": category_objects[cat], "priority": priority, "status": status}
            )
            if created:
                Comment.objects.create(ticket=ticket, author=operator, text="Демонстрационный комментарий.")
        self.stdout.write(self.style.SUCCESS("Демонстрационные данные готовы."))
        self.stdout.write("Админ-панель: demo_admin / HelpDesk123!")
        self.stdout.write("Дашборд/API: demo_operator / HelpDesk123!")
