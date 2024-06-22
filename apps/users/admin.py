from django.contrib import admin
from django.contrib.auth import get_user_model

User = get_user_model()


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_email_verified', 'is_seller', 'is_staff', 'is_active', 'date_joined')
    list_display_links = ('email',)
    raw_id_fields = ('user_permissions',)
