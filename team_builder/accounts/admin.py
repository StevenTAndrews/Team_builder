from django.contrib import admin

from .models import User, Skill


class SkillInline(admin.StackedInline):
    model = Skill


class UserAdmin(admin.ModelAdmin):
    inlines = [SkillInline,]


admin.site.register(User, UserAdmin)
admin.site.register(Skill)