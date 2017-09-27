from django.contrib import admin
from robotics.models import Season, Robot, RoboticsPress, RoboticsSponsors, Competition


class SeasonAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]
    exclude = ["slug"]


class RobotAdmin(admin.ModelAdmin):
    list_display = ["name", "competition"]
    list_filter = ["competition"]
    search_fields = ["name"]
    exclude = ["slug"]


class CompetitionAdmin(admin.ModelAdmin):
    list_display = ["name"]
    list_filter = ["season"]
    search_fields = ["name"]
    exclude = ["slug"]


class RoboticsSponsorsAdmin(admin.ModelAdmin):
    list_display = ["name", "is_success"]
    search_fields = ["name"]
    exclude = ["slug"]


class RoboticsPressAdmin(admin.ModelAdmin):
    list_display = ["name", "created_at"]
    search_fields = ["name"]
    exclude = ["slug"]


admin.site.register(Season, SeasonAdmin)
admin.site.register(Competition, CompetitionAdmin)
admin.site.register(Robot, RobotAdmin)
admin.site.register(RoboticsPress, RoboticsPressAdmin)
admin.site.register(RoboticsSponsors, RoboticsSponsorsAdmin)