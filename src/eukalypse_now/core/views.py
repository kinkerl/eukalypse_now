from django.shortcuts import render
from models import Testrun
from django.shortcuts import get_object_or_404
from django.utils import simplejson

def testrun_list(request):
    testruns = Testrun.objects.all()
    return render(request, 'testrun/list.html', {"testruns": testruns})

def testrun_detail(request, testrun_id):
    testrun = get_object_or_404(Testrun, pk=testrun_id)
    return render(request, 'testrun/detail.html', {"testrun": testrun})

def testresult_as_reference(request, testresult_id):
    testresult = get_object_or_404(Testrun, pk=testrun_id)
    testresult.become_reference()
    to_json = {"return": "clear"}
    return HttpResponse(simplejson.dumps(to_json), mimetype="application/json")
