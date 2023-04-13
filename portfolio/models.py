# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Cards(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    startdate = models.DateField()
    enddate = models.DateField()
    cardtype = models.CharField(max_length=255)
    place = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    keywords = models.CharField(max_length=1023)
    description = models.CharField(max_length=1023)

    class Meta:
        app_label = 'portfolio'
        managed = False
        db_table = 'cards'


class Projects(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    project_name = models.CharField(max_length=32)
    source_code_url_fk = models.ForeignKey('Urls', models.DO_NOTHING, db_column='source_code_url_fk', blank=True, null=True)
    site_url_fk = models.ForeignKey('Urls', models.DO_NOTHING, db_column='site_url_fk', blank=True, null=True)
    keywords = models.CharField(max_length=1024)
    description = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        app_label = 'portfolio'
        managed = False
        db_table = 'projects'


class Urls(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    site_name = models.CharField(max_length=32, blank=True, null=True)
    url = models.CharField(max_length=1024)

    class Meta:
        app_label = 'portfolio'
        managed = False
        db_table = 'urls'
