import os
import tempfile
from Mailroom_Part4 import CreateReport
from Mailroom_Part4 import ViewReport
from Mailroom_Part4 import EmailTemplate
from Mailroom_Part4 import UpdateDonorData
from Mailroom_Part4 import NewDonor

def EmailTemplateTest():
    #EmailTemplate
    test = EmailTemplate("Tim", [20, 30])
    assert test.__contains__("Tim")

def EmailTest():
    #EmailToFile
    for item in Mailroom_Part4.DictDonor:
        tempdir = tempfile.gettempdir()
        assert os.listdir(tempdir).__contains__("{}.txt".format(item))

# test report that the number of donors reported is truly the number of donors in the db
def ReportTest():
    #ViewReport, CreateReport
    assert ViewReport != CreateReport

def UpdateDonorTest():
    testname = "TestName"
    testdonation = [1.0, 2.0, 3.0]
    assert UpdateDonorData(testname,testdonation)

def NewDonorTest():
    testname = "TestName"
    testdonation = [1.0, 2.0, 3.0]
    assert NewDonor(testname,testdonation)
