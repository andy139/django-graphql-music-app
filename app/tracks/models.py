from django.db import models

from django.contrib.auth import get_user_model

# Create your models here.
class Track(models.Model):
    # id is added automatically
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    posted_by = models.ForeignKey(get_user_model(), null=True, on_delete=models.CASCADE) ##casecade if user deleted entire track will be deleted also


## class like

class Like(models.Model):
    user = models.ForeignKey(get_user_model(), null=True, on_delete=models.CASCADE)
    track = models.ForeignKey('tracks.Track', related_name='likes', on_delete=models.CASCADE)

    ## REFERENCES THE USER FOR A GIVEN TRACK