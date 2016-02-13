from django.db import models
import os

def generate_filename(self, filename):
    url = "files/%s/%s" % (self.title, filename)
    return url

class VideoUpload(models.Model):
	title=models.CharField(max_length=50)
	file=models.FileField(upload_to=generate_filename)
	def __unicode__(self):              # __unicode__ on Python 3
		return "Video(title:%s )"%(self.title)