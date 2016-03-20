from django.contrib import admin

from models import Question, Author, Answer


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['title', 'added_at']
    search_fields = ['title', 'added_at']
    #inlines = [ArticleInline]
    list_filter = ['added_at']


admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
admin.site.register(Author)

# Register your models here.
