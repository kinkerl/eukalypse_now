from django.db import models

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
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
        return self.identifier

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
    def __unicode__(self):
        return "{0}-{1}".format(self.project.name, self.created)

    def get_absolute_url(self):
        return "/testrun/detail/%i/" % self.id
