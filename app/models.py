import uuid
from django.db import models
from django.contrib.auth.models import User


class Site(models.Model):
    id                 = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user               = models.ForeignKey(User, on_delete=models.CASCADE, editable=False, null=False, blank=False)
    name               = models.CharField(max_length=30, unique=True, db_index=True, null=False, blank=False)
    url                = models.URLField(max_length=200, null=False, blank=False)
    visit_count        = models.IntegerField(default=0)    # Counts of visits a site through proxy 
    routed_data_amount = models.BigIntegerField(default=0) # Amount of data in bytes routed by proxy 
    
    def __str__(self):
        return self.name
    