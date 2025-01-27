import datetime
from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator

class Government(models.Model):
    stats = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ]
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    monarch = models.CharField(max_length=250)
    formed = models.PositiveIntegerField(default=2000, validators=[
        MinValueValidator(2000),
        MaxValueValidator(datetime.datetime.now().year)
    ])
    status = models.CharField(max_length=250, choices=stats)
    bio = models.TextField()
    objects = models.Manager()
    

    class Meta:
        db_table = Government
        ordering = ('-formed')
        verbose_name = _("Government")
        verbose_name_plural = _("Governments")
    
    def _init__(self):
        return self.name

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Government_detail", kwargs={"pk": self.pk})
    
    @classmethod
    def ref(cls):
        related_fields = [
            rel for rel in cls._meta.related_objects
            if isinstance(rel.field, models.ForeignKey)
        ]
        return related_fields


class Empire(models.Model):
    power = [
        ('I','Irrelevant'),
        ('H','Feeble'),
        ('G','Weak'),
        ('F','Limited'),
        ('E','Influential'),
        ('D','Strong'),
        ('C','Ascendant'),
        ('B','Superpower'),
        ('A','Godly'),
    ]
    plat = [
        ('A', 'Facebook'),
        ('B', 'Discord'),
        ('C', 'Reddit'),
        ('D', 'Whatsapp'),
    ]
    rep = [
        ('evil','Evil'),
        ('crooked','Crooked'),
        ('immoral','Immoral'),
        ('normal','Normal'),
        ('gentle','Gentle'),
        ('honorable','Honorable'),
        ('virtuous','Virtuous'),
        ('saintly','Saintly'),
    ]
    act  = [
        ('active','Active'),
        ('inactive','Inactive')
    ]
    name = models.CharField(max_length=250)
    emblem = models.ImageField(upload_to='Images/Empires/%Y/%m/%d/')
    formed = models.PositiveIntegerField(default=2000,validators=[
        MinValueValidator(2000),
        MaxValueValidator(datetime.datetime.now().year)
    ])
    monarch = models.CharField(max_length=250)
    strength = models.CharField(max_length=50, choices=power, default='E')
    reputation = models.CharField(max_length=20, choices=rep, default='normal')
    government = models.ForeignKey(Government, on_delete=models.CASCADE, default=self)
    platform = models.CharField(max_length=50, choices=plat)
    status = models.CharField( max_length=40, choices=act, default='active')
    objects = models.Manager()
    

    class Meta:
        db_table = 'Empires'
        ordering = ('strength')
        verbose_name = _("Empire")
        verbose_name_plural = _("Empires")
    
    def __init__(self):
        return self.name

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Empire_detail", kwargs={"pk": self.pk})
    
    @classmethod
    def ref(cls):
        related_fields = [
            rel for rel in cls._meta.related_objects
            if isinstance(rel.field, models.ForeignKey)
        ]
        return related_fields
    
    
    class Clan(models.Model):
        power = [
        ('I','Irrelevant'),
        ('H','Feeble'),
        ('G','Weak'),
        ('F','Limited'),
        ('E','Influential'),
        ('D','Strong'),
        ('C','Ascendant'),
        ('B','Superpower'),
        ('A','Godly'),
    ]
    plat = [
        ('A', 'Facebook'),
        ('B', 'Discord'),
        ('C', 'Reddit'),
        ('D', 'Whatsapp'),
    ]
    rep = [
        ('evil','Evil'),
        ('crooked','Crooked'),
        ('immoral','Immoral'),
        ('normal','Normal'),
        ('gentle','Gentle'),
        ('honorable','Honorable'),
        ('virtuous','Virtuous'),
        ('saintly','Saintly'),
    ]
    act  = [
        ('active','Active'),
        ('inactive','Inactive')
    ]
    name = models.CharField(max_length=250)
    emblem = models.ImageField(upload_to='Images/Clans/%Y/%m/%d/')
    formed = models.PositiveIntegerField(default=2000,validators=[
        MinValueValidator(2000),
        MaxValueValidator(datetime.datetime.now().year)
    ])
    monarch = models.CharField(max_length=250)
    strength = models.CharField(max_length=50, choices=power, default='E')
    reputation = models.CharField(max_length=20, choices=rep, default='normal')
    government = models.ForeignKey(Empire, on_delete=models.CASCADE, default=self)
    platform = models.CharField(max_length=50, choices=plat)
    status = models.CharField( max_length=40, choices=act, default='active')
    objects = models.Manager()
    

    class Meta:
        db_table = 'Clans'
        ordering = ('strength')
        verbose_name = _("Clan")
        verbose_name_plural = _("Clans")
    
    def __init__(self):
        return self.name

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Clan_detail", kwargs={"pk": self.pk})
    
    @classmethod
    def ref(cls):
        related_fields = [
            rel for rel in cls._meta.related_objects
            if isinstance(rel.field, models.ForeignKey)
        ]
        return related_fields