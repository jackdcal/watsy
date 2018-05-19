from django.contrib import admin

# Register your models here.
from .models import Sport, Event, Team, Channel, Game, Venue

admin.site.register(Sport)
admin.site.register(Event)
admin.site.register(Venue)
admin.site.register(Channel)
admin.site.register(Team)
admin.site.register(Game)