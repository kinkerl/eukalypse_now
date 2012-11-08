from models import Test, Project, Testrun, Testresult
from django.contrib import admin


class TestInline(admin.StackedInline):
    model = Test
    extra = 0

class ProjectAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name']}),
        ('Notification Mail',               {'fields': ['notify_mail', 'notify_only_error', 'notify_recipient']}),
    ]
    inlines = [TestInline]

admin.site.register(Project, ProjectAdmin)


admin.site.register(Test)
admin.site.register(Testrun)
admin.site.register(Testresult)

