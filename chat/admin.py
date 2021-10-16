from django.contrib import admin
from chat.models import Message


class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'email', 'text', 'create_date', 'update_date')
    search_fields = ('id', 'author', 'text')
    list_filter = ('author', 'email')


admin.site.register(Message, MessageAdmin)
