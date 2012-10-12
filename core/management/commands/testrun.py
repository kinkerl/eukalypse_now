from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from core.models import Project
from core.models import Testresult
from core.models import Testrun
from eukalypse.eukalypse import Eukalypse
import os
from datetime import datetime

class Command(BaseCommand):

    def _getMediaUrl(self, path):


        return path[len(settings.MEDIA_ROOT):]

    def handle(self, arg_project = None, *args, **options):
        project =  Project.objects.get(name=arg_project)
        testrun = Testrun.objects.create(project=project)
        
        for test in project.tests.all():

            e = Eukalypse()
            e.browser = 'chrome'
            e.output = os.path.join(settings.MEDIA_ROOT , 'images')
            eukalypse_result_object = e.compare(test.identifier + "-" + str(datetime.now()).replace(' ', '-'), test.image, test.url)
            e.disconnect()
            if eukalypse_result_object.clean:
                testresult = Testresult.objects.create(test=test, testrun = testrun, resultimage=self._getMediaUrl(eukalypse_result_object.target_img))
            else:
                testresult = Testresult.objects.create(\
                    test=test, \
                    testrun = testrun, \
                    error = True, \
                    resultimage=self._getMediaUrl(eukalypse_result_object.target_img), \
                    referenceimage=test.image, \
                    errorimage=self._getMediaUrl(eukalypse_result_object.difference_img), \
                    errorimage_improved=self._getMediaUrl(eukalypse_result_object.difference_img_improved)\
                    )

            testresult.save()

        testrun.save()


