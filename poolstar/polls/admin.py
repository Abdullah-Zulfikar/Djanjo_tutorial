from django.contrib import admin

# Register your models here.
from .models import Question, Choices

admin.site.site_header = "Pollster Admin"
admin.site.site_title = "Pollster Admin Area"
admin.site.index_title = "Welcome to the Pollster Admin"
class ChoiceInline(admin.TabularInline):
    model = Choices
    extra = 3
    

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline] 
    fieldsets = [(None, {"fields": ['question_text']}),
                 ("Date Information", {"fields": ['pub_date'], 'classes':['collapse']})]

admin.site.register(Question, QuestionAdmin)