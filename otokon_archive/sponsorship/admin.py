from django.contrib import admin
from sponsorship.models import Category, Company, Organization


class CategoryAdmin(admin.ModelAdmin):
    exclude = ["slug"]
    list_display = ["title", "sponsorship", "created"]


class OrganizationAdmin(admin.ModelAdmin):
    exclude = ["slug"]
    ordering = ["order"]
    list_display = ["title", "active", "created"]
    list_filter = ["active", "created"]
    search_fields = ["title"]


class CompanyAdmin(admin.ModelAdmin):
    exclude = ["slug"]
    list_display = ["name", "meeting", "success", "created"]
    search_fields = ["name"]
    list_filter = ["meeting", "created", "success"]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Organization, OrganizationAdmin)
