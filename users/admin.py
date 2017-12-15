from django.contrib import admin
from .models import *


class FinishTestAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'test', 'count_true_answer', 'count_false_answer', 'percent']
    readonly_fields = ['id', 'user', 'test', 'count_true_answer', 'count_false_answer', 'percent']
    list_filter = ['user', 'test', 'created']

    class Meta:
        model = FinishTest

    def has_add_permission(self, request):
        return False
    

admin.site.register(FinishTest, FinishTestAdmin)
