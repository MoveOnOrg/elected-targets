from __future__ import unicode_literals

import re

from django.db import models
from django.db.models.expressions import RawSQL

class Target(models.Model):

    class Meta:
        abstract = True

    state_column = 'state_abbrev'
    target_column = ''
    title_abbrev = ''

    def full_title(self):
        parts = []
        if self.title_abbrev:
            parts.append(self.title_abbrev)
        parts.extend([self.first, self.last])
        target = self.target_name()
        if target:
            parts.append('({})'.format(target))
        return ' '.join(parts)

    def target_name(self):
        target = getattr(self, self.target_column, '')
        return re.sub(r'(_|-0+)', '-', target)

    def target_type(self):
        return self._meta.db_table

    def target_id(self):
        return getattr(self, self.target_column, '')

    @classmethod
    def name_like(cls, query, name):
        return query.annotate(
            name=RawSQL('concat(first, \' \', last)',[])).filter(name__contains=name)

    @classmethod
    def search(cls, name=None, state=None, **kw):
        query = cls.objects
        queryargs = {}
        if state:
            queryargs[cls.state_column] = state
        if kw:
            queryargs.update(kw)
        if queryargs:
            query = query.filter(**queryargs)
        if name:
            query = cls.name_like(query, name)
        return query

    @classmethod
    def targetinfo(cls, query):
        """
        target_id, full_title, target_type = <table name>
        needs columns: first, last, target_column
        """
        return query.only('first', 'last', cls.target_column)


class Governor(Target):
    title_abbrev = 'Gov.'
    state_column = 'state'
    target_column = 'state'
    state = models.CharField(primary_key=True, max_length=2)
    governor = models.CharField(max_length=255)
    first = models.CharField(max_length=255)
    last = models.CharField(max_length=255)
    party = models.CharField(max_length=1)
    email = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    fax = models.CharField(max_length=255, blank=True, null=True)
    facebook = models.CharField(max_length=255, blank=True, null=True)
    twitter = models.CharField(max_length=255, blank=True, null=True)
    website = models.CharField(max_length=255, blank=True, null=True)
    contact_form = models.CharField(max_length=255, blank=True, null=True)
    additional_contact = models.TextField(blank=True, null=True)
    gender = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'governor'

    def full_title(self):
        return ' '.join([self.title_abbrev, self.governor])

    @classmethod
    def name_like(cls, query, name):
        return query.filter(governor__contains=name)

    @classmethod
    def targetinfo(cls, query):
        """
        target_id, full_title, target_type = <table name>
        needs columns: first, last, target_column
        """
        return query.only('governor', cls.target_column)


class Housemem(Target):
    title_abbrev = 'Rep.'
    target_column = 'district'  # to match to target_id
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
    district = models.OneToOneField(
        Housemem, related_name='contact', primary_key=True,
        db_column='district'
    )
    title = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'housemem_contact'
        verbose_name = 'Representative Contact'


class Senatemem(Target):
    title_abbrev = 'Sen.'
    target_column = 'seat'  # to match to target_id
    congress_id = models.IntegerField(blank=True, null=True)
    seat = models.CharField(primary_key=True, max_length=4)
    state = models.CharField(max_length=14, blank=True, null=True)
    fresh = models.CharField(max_length=1, blank=True, null=True)
    prefix = models.CharField(max_length=4, blank=True, null=True)
    last = models.CharField(max_length=11, blank=True, null=True)
    first = models.CharField(max_length=11, blank=True, null=True)
    middlename = models.CharField(
        db_column='middleName', max_length=7, blank=True, null=True
    )  # Field name made lowercase.
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


class SenatememContact(models.Model):
    seat = models.OneToOneField(
        Senatemem, related_name='contact', primary_key=True, db_column='seat'
    )
    title = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'senatemem_contact'
        verbose_name = 'Senator Contact'


class Statehousemem(Target):
    target_column = 'legislator_id'
    legislator_id = models.CharField(primary_key=True, max_length=6)
    district = models.CharField(max_length=15)
    state = models.CharField(max_length=20, blank=True, null=True)
    district2 = models.CharField(max_length=8, blank=True, null=True)
    fresh = models.CharField(max_length=1, blank=True, null=True)
    title = models.CharField(max_length=21, blank=True, null=True)
    prefix = models.CharField(max_length=4, blank=True, null=True)
    last = models.CharField(max_length=40, blank=True, null=True)
    first = models.CharField(max_length=40, blank=True, null=True)
    middlename = models.CharField(max_length=40, blank=True, null=True)
    nickname = models.CharField(max_length=40, blank=True, null=True)
    suffix = models.CharField(max_length=5, blank=True, null=True)
    gender = models.CharField(max_length=1, blank=True, null=True)
    party = models.CharField(max_length=3, blank=True, null=True)
    phone = models.CharField(max_length=12, blank=True, null=True)
    fax = models.CharField(max_length=12, blank=True, null=True)
    email = models.CharField(max_length=103, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    suite = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    zip = models.CharField(max_length=5, blank=True, null=True)
    plus4 = models.CharField(max_length=4, blank=True, null=True)
    leadership = models.CharField(max_length=53, blank=True, null=True)
    zip9 = models.CharField(max_length=9, blank=True, null=True)
    web = models.CharField(max_length=79, blank=True, null=True)
    state_abbrev = models.CharField(max_length=2)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'statehousemem'


class Statesenatemem(Target):
    target_column = 'legislator_id'
    legislator_id = models.CharField(primary_key=True, max_length=6)
    seat = models.CharField(max_length=15)
    state = models.CharField(max_length=20, blank=True, null=True)
    fresh = models.CharField(max_length=1, blank=True, null=True)
    title = models.CharField(max_length=40, blank=True, null=True)
    prefix = models.CharField(max_length=4, blank=True, null=True)
    last = models.CharField(max_length=40, blank=True, null=True)
    first = models.CharField(max_length=40, blank=True, null=True)
    middlename = models.CharField(
        db_column='middleName', max_length=40, blank=True, null=True
    )  # Field name made lowercase.
    nickname = models.CharField(max_length=255, blank=True, null=True)
    suffix = models.CharField(max_length=5, blank=True, null=True)
    gender = models.CharField(max_length=1, blank=True, null=True)
    party = models.CharField(max_length=3, blank=True, null=True)
    phone = models.CharField(max_length=12, blank=True, null=True)
    fax = models.CharField(max_length=12, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    suite = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    zip = models.CharField(max_length=5, blank=True, null=True)
    plus4 = models.CharField(max_length=4, blank=True, null=True)
    type = models.CharField(max_length=1, blank=True, null=True)
    leadership = models.CharField(max_length=46, blank=True, null=True)
    seatnumstrg = models.CharField(max_length=1, blank=True, null=True)
    zip9 = models.CharField(max_length=9, blank=True, null=True)
    election = models.CharField(max_length=4, blank=True, null=True)
    web = models.CharField(max_length=37, blank=True, null=True)
    state_abbrev = models.CharField(max_length=2, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'statesenatemem'


class ZipStateBodyDistrict(models.Model):
    class Meta:
        managed = False
        db_table = 'zip_to_statebody_district'

    zip = models.CharField(max_length=5, db_index=True)
    plus4_low = models.CharField(max_length=4)
    plus4_high = models.CharField(max_length=4, primary_key=True) # faking django
    house_or_sen = models.CharField(max_length=1,
                                    db_index=True,
                                    choices=(('H', 'House'), ('S', 'Senate')))
    # Most districts are XX_012, MD and MN have letters after the first 3 digits
    district = models.CharField(max_length=15)

    @classmethod
    def lookup_by_zip(cls, zip, plus4=None, house_or_sen=None):
        """
        if house_or_sen is None then we get both
        This returns results only when something is unique
        """
        mapkey = {'H': 'state_house', 'S': 'state_senate'}
        query = cls.objects.filter(zip=zip)
        if plus4:
            query = query.filter(plus4_low__lte=int(plus4),
                                 plus4_high__gte=int(plus4))
        if house_or_sen in ('H', 'S'):
            query = query.filter(house_or_sen=house_or_sen)
        look_for = 2 if house_or_sen else 4
        max_ok = 1 if house_or_sen else 2
        res = list(query.order_by('house_or_sen')[:look_for])
        if len(res) != max_ok:
            return {}
        rv = {}
        for find in res:
            endkey = mapkey[find.house_or_sen]
            if endkey in rv:
                # oops, a dupe!
                return {}
            rv[endkey] = find.district
        return rv


class ZipCongresionalDistrict(models.Model):
    class Meta:
        managed = False
        db_table = 'zip_to_district'

    zip = models.CharField(max_length=5, db_index=True, primary_key=True)
    district = models.CharField(max_length=6, null=True, blank=True, db_index=True)
    certainty = models.SmallIntegerField() # 0-100
