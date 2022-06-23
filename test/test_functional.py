import unittest
from number_to_words import number_to_words
from HCF import get_hcf
from test.TestUtils import TestUtils
class FuctionalTests(unittest.TestCase):
    def test_result_for_58(self):
        result=number_to_words(58)
        test_obj = TestUtils()
        if result=="FIVE EIGHT":
            test_obj.yakshaAssert("TestResultFor58", True, "functional")
            print("TestResultFor58 = Passed")
        else:
            test_obj.yakshaAssert("TestResultFor58", False, "functional")
            print("TestResultFor58 = Failed")

    def test_result_type_for_1045(self):
        result=number_to_words(1045)
        test_obj = TestUtils()
        if result=="ONE ZERO FOUR FIVE":
            test_obj.yakshaAssert("TestResultFor1045", True, "functional")
            print("TestResultFor1045 = Passed")
        else:
            test_obj.yakshaAssert("TestResultFor1045", False, "functional")
            print("TestResultFor1045 = Failed")

    def test_hef_result_for_12and4(self):
        result=get_hcf(12,4)
        test_obj = TestUtils()
        if result==4:
            test_obj.yakshaAssert("TestHcfResultFor12and4", True, "functional")
            print("TestHcfResultFor12and4 = Passed")
        else:
            test_obj.yakshaAssert("TestHcfResultFor12and4", False, "functional")
            print("TestHcfResultFor12and4 = Failed")

    def test_hef_result_for_30and50(self):
        result=get_hcf(30,50)
        test_obj = TestUtils()
        if result==10:
            test_obj.yakshaAssert("TestHcfResultFor30and50", True, "functional")
            print("TestHcfResultFor30and50 = Passed")
        else:
            test_obj.yakshaAssert("TestHcfResultFor30and50", False, "functional")
            print("TestHcfResultFor30and50 = Failed")

    def test_result_type_for_words(self):
        s=number_to_words(58)
        test_obj = TestUtils()
        if type(s)==type(" "):
            test_obj.yakshaAssert("TestResultTypeForWords", True, "functional")
            print("TestResultTypeForWords = Passed")
        else:
            test_obj.yakshaAssert("TestResultTypeForWords", False, "functional")
            print("TestResultTypeForWords = Failed")
    def test_result_type_for_hcf(self):
        n=get_hcf(10,8)
        test_obj = TestUtils()
        if type(n)==type(1):
            test_obj.yakshaAssert("TestResultTypeForHcf", True, "functional")
            print("TestResultTypeForHcf = Passed")
        else:
            test_obj.yakshaAssert("TestResultTypeForHcf", False, "functional")
            print("TestResultTypeForHcf = Failed")
