import csv

from django.contrib import admin
from django.http import HttpResponse

from .models import Choice, Question


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

    actions = ['download_csv']

    def download_csv(self, request, queryset):
        print 'hi'
        print queryset
        print self.list_display
        f = open('questions.csv', 'wb')
        writer = csv.writer(f)
        writer.writerow(self.list_display)

        for q in queryset:
            writer.writerow([q.id, q.question_text, q.was_published_recently()])

        f.close()

        f = open('questions.csv', 'r')
        response = HttpResponse(f, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=stat-info.csv'
        return response

    download_csv.short_description = "Download CSV file for selected stats."

admin.site.register(Question, QuestionAdmin)
