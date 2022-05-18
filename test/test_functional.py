
import unittest
import sys
sys.path.append("..")
from number_to_words import number_to_words
from HCF import get_hcf
from test.TestUtils import TestUtils
class FuctionalTests(unittest.TestCase):
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
