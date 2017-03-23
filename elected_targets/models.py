# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models

class Housemem(models.Model):
    congress_id = models.IntegerField(blank=True, null=True)
    district = models.CharField(primary_key=True, max_length=5)
    state = models.CharField(max_length=14, blank=True, null=True)
    district2 = models.CharField(max_length=8, blank=True, null=True)
    fresh = models.CharField(max_length=1, blank=True, null=True)
    prefix = models.CharField(max_length=4, blank=True, null=True)
    last = models.CharField(max_length=21, blank=True, null=True)
    first = models.CharField(max_length=40, blank=True, null=True)
    middlename = models.CharField(max_length=8, blank=True, null=True)
    nickname = models.CharField(max_length=20, blank=True, null=True)
    suffix = models.CharField(max_length=5, blank=True, null=True)
    gender = models.CharField(max_length=1, blank=True, null=True)
    party = models.CharField(max_length=1, blank=True, null=True)
    phone = models.CharField(max_length=12, blank=True, null=True)
    fax = models.CharField(max_length=12, blank=True, null=True)
    email = models.CharField(max_length=103, blank=True, null=True)
    building = models.CharField(max_length=4, blank=True, null=True)
    suite = models.CharField(max_length=4, blank=True, null=True)
    leadership = models.CharField(max_length=53, blank=True, null=True)
    plus4 = models.CharField(max_length=4, blank=True, null=True)
    web = models.CharField(max_length=79, blank=True, null=True)
    tweet = models.CharField(max_length=255, blank=True, null=True)
    formal_name = models.CharField(max_length=255, blank=True, null=True)
    informal_name = models.CharField(max_length=255, blank=True, null=True)
    state_abbrev = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'housemem'
        verbose_name = 'Representative'


class HousememContact(models.Model):
    district = models.CharField(primary_key=True, max_length=5)
    title = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'housemem_contact'

class Senatemem(models.Model):
    congress_id = models.IntegerField(blank=True, null=True)
    seat = models.CharField(primary_key=True, max_length=4)
    state = models.CharField(max_length=14, blank=True, null=True)
    fresh = models.CharField(max_length=1, blank=True, null=True)
    prefix = models.CharField(max_length=4, blank=True, null=True)
    last = models.CharField(max_length=11, blank=True, null=True)
    first = models.CharField(max_length=11, blank=True, null=True)
    middlename = models.CharField(db_column='middleName', max_length=7, blank=True, null=True)  # Field name made lowercase.
    nickname = models.CharField(max_length=255, blank=True, null=True)
    suffix = models.CharField(max_length=5, blank=True, null=True)
    gender = models.CharField(max_length=1, blank=True, null=True)
    party = models.CharField(max_length=1, blank=True, null=True)
    phone = models.CharField(max_length=12, blank=True, null=True)
    fax = models.CharField(max_length=12, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    building = models.CharField(max_length=4, blank=True, null=True)
    suite = models.CharField(max_length=8, blank=True, null=True)
    type = models.CharField(max_length=1, blank=True, null=True)
    leadership = models.CharField(max_length=46, blank=True, null=True)
    seatnumstrg = models.CharField(max_length=1, blank=True, null=True)
    plus4 = models.CharField(max_length=4, blank=True, null=True)
    election = models.CharField(max_length=4, blank=True, null=True)
    web = models.CharField(max_length=37, blank=True, null=True)
    tweet = models.CharField(max_length=255, blank=True, null=True)
    formal_name = models.CharField(max_length=255, blank=True, null=True)
    informal_name = models.CharField(max_length=255, blank=True, null=True)
    state_abbrev = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'senatemem'
        verbose_name = 'Senator'
