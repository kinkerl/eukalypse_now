from django.shortcuts import render
from models import Testrun
from django.shortcuts import get_object_or_404

def testrun_list(request):
    testruns = Testrun.objects.all()
    return render(request, 'testrun/list.html', {"testruns": testruns})

def testrun_detail(request, testrun_id):
    testrun = get_object_or_404(Testrun, pk=testrun_id)
    return render(request, 'testrun/detail.html', {"testrun": testrun})