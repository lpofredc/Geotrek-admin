from django.contrib import admin
from django.utils.html import format_html

from geotrek.common.mixins.actions import MergeActionMixin
from geotrek.sensitivity.models import Rule, SportPractice, Species


class RuleAdmin(MergeActionMixin, admin.ModelAdmin):
    merge_field = "name"
    list_display = ('name', 'code', 'thumb')
    search_fields = ('name', 'code', )

    def thumb(self, obj):
        return format_html(
            f'''<a href="{obj.pictogram.url}" target="_blank">
                  <img
                    src="{obj.pictogram.url}" alt="{obj.pictogram.url}"
                    width="30" height="30"
                    style="object-fit: cover;"
                  />
                </a>''')


class SportPracticeAdmin(MergeActionMixin, admin.ModelAdmin):
    merge_field = "name"


class SpeciesAdmin(MergeActionMixin, admin.ModelAdmin):
    merge_field = "name"

    def get_queryset(self, request):
        return super().get_queryset(request).filter(category=Species.SPECIES)


admin.site.register(Rule, RuleAdmin)
admin.site.register(SportPractice, SportPracticeAdmin)
admin.site.register(Species, SpeciesAdmin)
