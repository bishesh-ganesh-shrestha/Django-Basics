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
    search_fields = ["question_text"]
    list_display = ["question_text", "pub_date", "was_published_recently"]
    list_filter = ["pub_date"]
    
    # fields = ["pub_date", "question_text"]
    fieldsets = [
        ('Write down your question', {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"]}),
    ]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)