from django.conf import settings
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Пользователь")
    bio = models.TextField(blank=True, verbose_name="О себе")
    birth_date = models.DateField(
        null=True, blank=True, verbose_name="Дата рождения")

    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профиль пользователя'

    def __str__(self):
        return f"Profile of {self.user.username}"


class Status(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="Название"
    )
    is_final = models.BooleanField(
        default=False,
        verbose_name="Финальный статус"
    )

    class Meta:
        verbose_name = "Статус"
        verbose_name_plural = "Статусы"

    def __str__(self):
        return self.name


class Category(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name="Название"
    )
    description = models.TextField(
        blank=True,
        verbose_name="Описание"
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.title


class Note(models.Model):
    text = models.TextField(
        verbose_name="Текст"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Автор"
    )
    status = models.ForeignKey(
        Status,
        on_delete=models.CASCADE,
        verbose_name="Статус"
    )
    categories = models.ManyToManyField(
        Category,
        related_name="notes",
        verbose_name="Категории"
    )

    class Meta:
        verbose_name = "Заметка"
        verbose_name_plural = "Заметки"

    def __str__(self):
        return f"Заметка от {self.author.username} ({self.status.name})"
