import datetime
from django.db import models
from django.utils import timezone
from autoslug import AutoSlugField
from .utils import getcountry


countr_l = getcountry()


class Sport(models.Model):
    name = models.CharField(max_length=100, unique=True)
    duration = models.TimeField(default='')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Event(models.Model):
    name = models.CharField(blank=False, max_length=50)
    sport = models.ForeignKey(Sport, on_delete=models.SET_NULL, null=True, to_field='name')
    website = models.URLField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Venue(models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


group_choice = (('A', 'A'), ('B', 'B'),('C', 'C'),('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H'))


class Team(models.Model):
    #group_choice = (('A', 'A'), ('B', 'B'),('C', 'C'),('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H'))
    gender_choice = (('F', 'Female'), ('M', 'Male'), ('N', 'No Gender'))
    name = models.CharField(blank=False, max_length=50)
    group = models.CharField(choices=group_choice, max_length=1, blank=True, null=True)
    sport = models.ForeignKey(Sport, on_delete=models.SET_NULL, blank=True, null=True)
    country = models.CharField(choices=countr_l, max_length=50)
    country_code = models.CharField(max_length=6, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    gender = models.CharField(max_length=1, choices=gender_choice)
    website = models.URLField()
    image = models.ImageField(blank=True,null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.country_code != self.country:
            self.country_code = self.country
        super(Team, self).save(*args, **kwargs)

    class Meta:
        ordering = ['name']    


class Channel(models.Model):
    name = models.CharField(blank=False, max_length=50)
    country = models.CharField(blank=True, max_length=50)
    language = models.CharField(blank=False, max_length=50)
    website = models.URLField()

    def __str__(self):
        return self.name


def get_populate_from(instance):
        return '%s-%s-%s' % (instance.date, instance.team1, instance.team2)


class Game(models.Model):
    
    sport = models.ForeignKey(Sport,  on_delete=models.SET_NULL, null=True)
    event = models.ForeignKey(Event, on_delete=models.SET_NULL, null=True)
    venue = models.ForeignKey(Venue, on_delete=models.SET_NULL, null=True)
    date = models.DateField()
    start_time = models.TimeField()
    team1 = models.ForeignKey(Team, related_name='team1', on_delete=models.SET_NULL, null=True)
    team2 = models.ForeignKey(Team, related_name='team2', on_delete=models.SET_NULL, null=True)
    slug = AutoSlugField(populate_from=get_populate_from, unique=True, editable=False)
    channels = models.ManyToManyField(Channel)
    

    def __str__(self):
        return '%s-%s' % (self.team1, self.team2)

    class Meta:
        ordering = ['date','start_time']