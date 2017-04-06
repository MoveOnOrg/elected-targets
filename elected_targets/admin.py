# from django import forms
from django.contrib import admin
from .models import Housemem, Senatemem
try:
    from moveon_theme.filters import DropdownFilter
except ImportError:
    DropdownFilter = None

class HousememAdmin(admin.ModelAdmin):
    readonly_fields = [
        'district', 'state', 'fresh', 'prefix', 'suffix', 'phone',
        'fax', 'building', 'suite', 'leadership', 'plus4', 'web', 'tweet'
    ]
    fields = [
        'first', 'last', 'email', 'nickname', 'gender', 'party',
        'district', 'state', 'fresh', 'prefix', 'suffix', 'phone',
        'fax', 'building', 'suite', 'leadership', 'plus4', 'web', 'tweet'
    ]
    list_display = ('district', 'first', 'last')
    list_filter = (('state', DropdownFilter),) if DropdownFilter else ['state']
    list_sort = ['district', 'first', 'last']
    search_fields = ['first', 'last']

admin.site.register(Housemem, HousememAdmin)

class SenatememAdmin(admin.ModelAdmin):
    readonly_fields = [
        'seat', 'state', 'prefix', 'suffix', 'phone', 'fax', 'building',
        'suite', 'leadership', 'plus4', 'web', 'tweet'
    ]
    fields = [
        'first', 'last', 'email', 'nickname', 'gender', 'party',
        'seat', 'state', 'prefix', 'suffix', 'phone', 'fax', 'building',
        'suite', 'leadership', 'plus4', 'web', 'tweet'
    ]
    list_display = ('state', 'first', 'last')
    list_filter = (('state', DropdownFilter),) if DropdownFilter else ['state']
    list_sort = ['state', 'first', 'last']
    search_fields = ['first', 'last']

admin.site.register(Senatemem, SenatememAdmin)
