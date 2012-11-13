from celery.task import  task, Task
from django.core.management import call_command
from models import Project
import  logging

logger = logging.getLogger('eukalypse-now.task')

class PeriodicalCheck(Task):
    """ Task to automatically check all the active projects and run the testruns one after another."""
    def run(self, **kwargs):
        print "test"
        logger.debug("run PeriodicalCheck")
        for project in Project.objects.filter(active=True):
            logger.error(project)
            call_command("testrun", project.name)
        
