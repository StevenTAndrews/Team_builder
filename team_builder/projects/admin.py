from django.contrib import admin

from .models import Project, Position, Application, Notification


class PositionInline(admin.StackedInline):
    model = Position


class ProjectAdmin(admin.ModelAdmin):
    inlines = [PositionInline,]


admin.site.register(Project, ProjectAdmin)
admin.site.register(Position)
admin.site.register(Application)
admin.site.register(Notification)