from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Countries)
class CountriesAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'iso3', 'numeric_code', 'iso2', 'phonecode', 'capital', 'currency', 'currency_name', 'currency_symbol']
    search_fields = ['name']
    list_filter = ['currency']

    def has_add_permission(self, request) -> bool:
        return False

    def has_change_permission(self, request, obj=None) -> bool:
        return False

    def has_delete_permission(self, request, obj=None) -> bool:
        return False

    # def has_module_permission(self, request) -> bool:
    #     return True

    # def has_view_permission(self, request, obj) -> bool:
    #     return True

    # def __hash__(self) -> int:
    #     return super().__hash__()


@admin.register(States)
class StatesAdmin(admin.ModelAdmin):
    list_display = ['name', 'country', 'country_code', 'fips_code', 'iso2', 'type']
    search_fields = ['name', 'country__name']
    list_filter = ['type']

    def has_add_permission(self, request) -> bool:
        return False

    def has_change_permission(self, request, obj=None) -> bool:
        return False

    def has_delete_permission(self, request, obj=None) -> bool:
        return False

@admin.register(Cities)
class CitiesAdmin(admin.ModelAdmin):
    list_display = ['name', 'state', 'state_code', 'country', 'country_code']
    search_fields = ['name', 'country__name', 'state__name']

    def has_add_permission(self, request) -> bool:
        return False

    def has_change_permission(self, request, obj=None) -> bool:
        return False

    def has_delete_permission(self, request, obj=None) -> bool:
        return False