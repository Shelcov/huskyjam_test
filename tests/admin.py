from django.contrib import admin
from .models import *


class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 0


class TestAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Test._meta.fields]

    class Meta:
        model = Test


admin.site.register(Test, TestAdmin)


class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]
    list_display = [field.name for field in Question._meta.fields]
    list_filter = ['test', 'is_active']
    search_fields = ['name']


    class Meta:
        model = Question


admin.site.register(Question, QuestionAdmin)


class AnswerAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Answer._meta.fields]

    class Meta:
        model = Answer


admin.site.register(Answer, TestAdmin)
