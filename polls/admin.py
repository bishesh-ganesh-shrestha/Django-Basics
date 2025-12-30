from django.contrib import admin

from .models import Question, Choice

# admin.site.register(Question)
admin.site.register(Choice)

# Register your models here.
# StackedInline = horizontal display
# TabularInline = vertical display
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 2

class QuestionAdmin(admin.ModelAdmin):
    # fields = ["pub_date", "question_text"]
    fieldsets = [
        ('Write down your question', {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"]}),
    ]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)