from django.db import models


class Cards(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    priority = models.PositiveSmallIntegerField()
    main = models.BooleanField()
    category = models.CharField(max_length=255)
    startdate = models.DateField(null=True)
    enddate = models.DateField(null=True)
    cardtype = models.CharField(max_length=255)
    place = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    keywords = models.CharField(max_length=1023)
    description = models.CharField(max_length=1023)

    class Meta:
        app_label = 'portfolio'
        db_table = 'cards'


class Projects(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    project_name = models.CharField(max_length=32)
    source_code_url_fk = models.ForeignKey(
        'portfolio.Urls',
        models.DO_NOTHING,
        db_column='source_code_url_fk',
        blank=True,
        null=True,
        related_name='source_code_url'
    )
    site_url_fk = models.ForeignKey(
        'portfolio.Urls',
        models.DO_NOTHING,
        db_column='site_url_fk',
        blank=True,
        null=True,
        related_name='site_url'
    )
    keywords = models.CharField(max_length=1024)
    description = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        app_label = 'portfolio'
        db_table = 'projects'


class Urls(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    site_name = models.CharField(max_length=32, blank=True, null=True)
    url = models.CharField(max_length=1024)

    class Meta:
        app_label = 'portfolio'
        db_table = 'urls'
