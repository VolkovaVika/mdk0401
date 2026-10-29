from django.conf import settings
from django.db import models

class Category(models.Model):
    name = models.CharField("Название", max_length=100, unique=True)
    description = models.TextField("Описание", blank=True)
    is_active = models.BooleanField("Активна", default=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name

class Ticket(models.Model):
    class Status(models.TextChoices):
        NEW = "new", "Новая"
        IN_PROGRESS = "in_progress", "В работе"
        WAITING = "waiting", "Ожидает ответа"
        RESOLVED = "resolved", "Решена"
        CLOSED = "closed", "Закрыта"

    class Priority(models.TextChoices):
        LOW = "low", "Низкий"
        MEDIUM = "medium", "Средний"
        HIGH = "high", "Высокий"
        CRITICAL = "critical", "Критический"

    title = models.CharField("Тема", max_length=200)
    description = models.TextField("Описание обращения")
    requester = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT,
                                  related_name="submitted_tickets", verbose_name="Заявитель")
    assignee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
                                 null=True, blank=True, related_name="assigned_tickets",
                                 verbose_name="Исполнитель")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True,
                                 related_name="tickets", verbose_name="Категория")
    status = models.CharField("Статус", max_length=20, choices=Status.choices, default=Status.NEW)
    priority = models.CharField("Приоритет", max_length=20, choices=Priority.choices, default=Priority.MEDIUM)
    created_at = models.DateTimeField("Создана", auto_now_add=True)
    updated_at = models.DateTimeField("Обновлена", auto_now=True)
    resolved_at = models.DateTimeField("Дата решения", null=True, blank=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"

    def __str__(self):
        return f"Заявка #{self.pk}: {self.title}"

class Comment(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name="comments", verbose_name="Заявка")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT,
                               related_name="ticket_comments", verbose_name="Автор")
    text = models.TextField("Комментарий")
    created_at = models.DateTimeField("Создан", auto_now_add=True)

    class Meta:
        ordering = ["created_at"]
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    def __str__(self):
        return f"Комментарий к заявке #{self.ticket_id}"
