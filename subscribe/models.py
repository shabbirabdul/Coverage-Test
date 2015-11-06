from django.contrib.gis.db import models
from django.contrib.gis import admin

class subscriber(models.Model):
    email = models.EmailField("Email Address", max_length=254)
    fname = models.CharField("First Name", max_length=25, blank=True)
    lname = models.CharField("Last Name", max_length=25, blank=True)

    SECTORS = (               
               ('AG', 'Agriculture'),
               ('FR', 'Forestry'),
               ('-',  'All')
               )
    sector = models.CharField("Sector", max_length=2, choices=SECTORS, default="-")        
    
    range = models.IntegerField(default='0')    
    geom = models.PointField(srid=4326)

    date_created= models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.email

    class Meta:
        verbose_name_plural = "Subscribers"
        
admin.site.register(subscriber, admin.OSMGeoAdmin)