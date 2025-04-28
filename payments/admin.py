from django.contrib import admin
from .models import Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'amount', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('id', )
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)
