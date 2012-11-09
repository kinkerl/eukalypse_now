from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from eukalypse_now.models import Project
from eukalypse_now.models import Testresult
from eukalypse_now.models import Testrun
from eukalypse.eukalypse import Eukalypse
import os
from datetime import datetime
import smtplib
from email.mime.text import MIMEText

class Command(BaseCommand):

    def _getMediaUrl(self, path):

        return path[len(settings.MEDIA_ROOT):]

    def handle(self, arg_project = None, *args, **options):
        project =  Project.objects.get(name=arg_project)
        testrun = Testrun.objects.create(project=project)
        for test in project.tests.all():

            e = Eukalypse()
            e.browser = settings.EUKALYPSE_BROWSER
            e.host = settings.EUKALYPSE_HOST
            e.output = os.path.join(settings.MEDIA_ROOT , 'images')
            eukalypse_result_object = e.compare(test.get_identifier(), test.image, test.url)
            e.disconnect()
            if eukalypse_result_object.clean:
                testresult = Testresult.objects.create(\
                    test=test, \
                    testrun = testrun, \
                    error = False, \
                    resultimage=self._getMediaUrl(eukalypse_result_object.target_img),\
                    referenceimage=test.image, \
                    )
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
                testrun.error = True

            testresult.save()

        testrun.save()

        if project.notify_mail:
            if (project.notify_only_error and testrun.error) or not project.notify_only_error:
                from django.template.loader import render_to_string
                render = render_to_string('eukalypse_now/mail.html', {'testrun': testrun, 'SITE_URL': settings.SITE_URL})
                msg = MIMEText(render, 'html')
                msg['Subject'] = 'MB.com Pixel Reporting'
                msg['From'] = settings.NOTIFY_MAIL_SENDER
                msg['To'] = project.notify_recipient
                s = smtplib.SMTP(settings.EMAIL_HOST)
                s.sendmail(settings.NOTIFY_MAIL_SENDER, project.notify_recipient, msg.as_string())
                s.quit()



