
import unittest
import sys
sys.path.append("..")
from number_to_words import number_to_words
from HCF import get_hcf
from test.TestUtils import TestUtils
class ExceptionalTest(unittest.TestCase):
    def test_error_type_for_words(self):
        test_obj = TestUtils()
        try:
            number_to_words(58)
            test_obj.yakshaAssert("TestErrorTypeForWords",True,"exception")
            print("TestErrorTypeForWords = Passed")
        except ValueError:
            test_obj.yakshaAssert("TestErrorTypeForWords",False,"exception")
            print("TestErrorTypeForWords = Failed ")

    def test_error_type_for_hcf(self):
        test_obj = TestUtils()
        try:
            get_hcf(58,40)
            test_obj.yakshaAssert("TestErrorTypeForHcf",True,"exception")
            print("TestErrorTypeForHcf = Passed")
        except ValueError:
            test_obj.yakshaAssert("TestErrorTypeForHcf",False,"exception")
            print("TestErrorTypeForHcf = Failed")
