# from django import forms
from django.contrib import admin
from .models import (Housemem, HousememContact, Senatemem, SenatememContact, 
    Statehousemem, Statesenatemem, Governor)
try:
    from moveon_theme.filters import DropdownFilter
except ImportError:
    DropdownFilter = None


class HousememContactInline(admin.StackedInline):
    fieldsets = (
        (None, {'fields': ('title', 'name', 'email')}),
    )
    model = HousememContact
    extra = 0


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
    inlines = (HousememContactInline, )
    list_display = ('district', 'first', 'last')
    list_filter = (('state', DropdownFilter),) if DropdownFilter else ['state']
    list_sort = ['district', 'first', 'last']
    search_fields = ['first', 'last']

admin.site.register(Housemem, HousememAdmin)


class SenateMemContactInline(admin.StackedInline):
    fieldsets = (
        (None, {'fields': ('title', 'name', 'email')}),
    )
    model = SenatememContact
    extra = 0


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
    inlines = (SenateMemContactInline, )
    list_display = ('state', 'first', 'last')
    list_filter = (('state', DropdownFilter),) if DropdownFilter else ['state']
    list_sort = ['state', 'first', 'last']
    search_fields = ['first', 'last']

admin.site.register(Senatemem, SenatememAdmin)


class StatesenatememAdmin(admin.ModelAdmin):
    readonly_fields = [
        'state', 'prefix', 'suffix', 'phone', 'fax',
        'suite', 'leadership', 'plus4', 'web'
    ]
    fields = [
        'first', 'last', 'email', 'nickname', 'gender', 'party',
        'state', 'prefix', 'suffix', 'phone', 'fax',
        'suite', 'leadership', 'plus4', 'web'
    ]
    list_display = ('state', 'seat', 'first', 'last')
    list_filter = (('state', DropdownFilter),) if DropdownFilter else ['state']
    list_sort = ['state', 'seat', 'first', 'last']
    search_fields = ['first', 'last', 'seat']

admin.site.register(Statesenatemem, StatesenatememAdmin)


class StatehousememAdmin(admin.ModelAdmin):
    readonly_fields = [
        'state', 'prefix', 'suffix', 'phone', 'fax',
        'suite', 'leadership', 'plus4', 'web'
    ]
    fields = [
        'first', 'last', 'email', 'nickname', 'gender', 'party',
        'state', 'prefix', 'suffix', 'phone', 'fax',
        'suite', 'leadership', 'plus4', 'web'
    ]
    list_display = ('state', 'district', 'first', 'last')
    list_filter = (('state', DropdownFilter),) if DropdownFilter else ['state']
    list_sort = ['state', 'district', 'first', 'last']
    search_fields = ['first', 'last', 'district']

admin.site.register(Statehousemem, StatehousememAdmin)


class GovernorAdmin(admin.ModelAdmin):
    readonly_fields = [
        'state', 'phone', 'fax'
    ]
    fields = [
        'first', 'last', 'email', 'gender', 'party','state', 'phone', 'fax'
    ]
    list_display = ('state', 'first', 'last')
    list_filter = (('state', DropdownFilter),) if DropdownFilter else ['state']
    list_sort = ['state', 'first', 'last']
    search_fields = ['first', 'last']

admin.site.register(Governor, GovernorAdmin)


