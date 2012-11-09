# -*- coding: utf-8 -*-
import os
from django.db import models
from django.conf import settings
from datetime import datetime
from eukalypse.eukalypse import Eukalypse


class Project(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    notify_mail = models.BooleanField(default=False, help_text="send notification mail after a testrun")
    notify_only_error = models.BooleanField(default=False, help_text="only send the mail if an error occurs")
    notify_recipient =  models.TextField(blank=True, null=True)
    
    def __unicode__(self):
        return self.name

class Test(models.Model):
    project = models.ForeignKey('Project', related_name='tests')
    identifier = models.SlugField(max_length=200)
    url = models.URLField()
    image = models.ImageField(upload_to='images', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u"%s <%s>" % (self.identifier, self.image)

    def get_identifier(self):
        from django.template.defaultfilters import slugify
        """Liefert einen identifier String für dieses Screenshotbild."""
        return u"%s" % slugify(self.identifier + "-" + str(datetime.now()).replace(' ', '-'))

    def _set_image_from_url(self):
        """Erzeugt Screenshot von url mit Eukalypse und speichert selbiges image (überschreibt evtl vorhandenes image)."""
        identifier = self.get_identifier() # Vorher speichern!
        e = Eukalypse()
        e.browser = settings.EUKALYPSE_BROWSER
        e.host = settings.EUKALYPSE_HOST
        e.output = os.path.join(settings.MEDIA_ROOT , 'images')
        e.screenshot(identifier, self.url)
        self.image = "images/" + identifier + ".png"
        self.save()

class Testresult(models.Model):
    test = models.ForeignKey('Test')
    testrun = models.ForeignKey('Testrun',  related_name='testresult')
    resultimage = models.ImageField(upload_to='images', null=True, blank=True)
    error = models.BooleanField(default=False)
    referenceimage = models.ImageField(upload_to='images', null=True, blank=True)
    errorimage = models.ImageField(upload_to='images', null=True, blank=True)
    errorimage_improved = models.ImageField(upload_to='images', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "{0}-{1}".format(self.test.identifier, self.testrun.created)

    def become_reference(self):
        self.test.image = self.resultimage

class Testrun(models.Model):
    project = models.ForeignKey('Project', null=True,  related_name='testrun')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    error = models.BooleanField(default=True)
    def __unicode__(self):
        return "{0}-{1}".format(self.project.name, self.created)

    def get_absolute_url(self):
        return "/testrun/detail/%i/" % self.id
