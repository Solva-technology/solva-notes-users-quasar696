from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.contrib.auth.models import User
from .models import UserProfile, Status, Category, Note


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = "Профиль пользователя"


class CustomUserAdmin(DjangoUserAdmin):
    inlines = (UserProfileInline,)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "is_final")
    list_filter = ("is_final",)
    search_fields = ("name",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    search_fields = ("title", "description")
    list_filter = ("title",)


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ("id", "author", "status", "created_at")
    search_fields = ("text", "author__name", "status__name")
    list_filter = ("status", "categories", "created_at")
    filter_horizontal = ("categories",)
