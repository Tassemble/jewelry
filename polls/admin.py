from django.contrib import admin

# Register your models here.


from polls.models import Question,Choice



class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3



class QuestionAdmin(admin.ModelAdmin):
	fields = ["question_text", "pub_date"]
	inlines = [ChoiceInline]
	list_display = ('question_text', 'pub_date', 'was_published_recently')
	search_fields = ['question_text']
	list_filter = ['pub_date']



admin.site.register(Question, QuestionAdmin)

