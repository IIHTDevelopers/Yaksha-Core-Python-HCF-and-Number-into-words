import unittest
from number_to_words import number_to_words
from HCF import get_hcf
from test.TestUtils import TestUtils
class ExceptionalTest(unittest.TestCase):
    def test_incorrect_result_for_1045(self):
        result=number_to_words(1045)
        test_obj = TestUtils()
        if result!="ONE ZERO FOUR FIVE":
            test_obj.yakshaAssert("TestIncorrectResultFor1045", False, "exception")
            print("TestIncorrectResultFor1045 = Failed")
        else:
            test_obj.yakshaAssert("TestIncorrectResultFor1045", True, "exception")
            print("TestIncorrectResultFor1045 = Passed")

    def test_hef_incorrect_result_for_12and4(self):
        result=get_hcf(12,4)
        test_obj = TestUtils()
        if result!=4:
            test_obj.yakshaAssert("TestHcfIncorrectResultFor12and4", False, "exception")
            print("TestHcfIncorrectResultFor12and4 = Failed")
        else:
            test_obj.yakshaAssert("TestHcfIncorrectResultFor12and4", True, "exception")
            print("TestHcfIncorrectResultFor12and4 = Passed")

    def test_error_type_for_words(self):
        test_obj = TestUtils()
        try:
            number_to_words('58')
            test_obj.yakshaAssert("TestErrorTypeForWords",False,"exception")
            print("TestErrorTypeForWords = Failed ")
        except TypeError:
            test_obj.yakshaAssert("TestErrorTypeForWords",True,"exception")
            print("TestErrorTypeForWords = Passed")

    def test_error_type_for_hcf(self):
        test_obj = TestUtils()
        try:
            get_hcf('58','40')
            test_obj.yakshaAssert("TestErrorTypeForHcf",False,"exception")
            print("TestErrorTypeForHcf = Failed")
        except TypeError:
            test_obj.yakshaAssert("TestErrorTypeForHcf",True,"exception")
            print("TestErrorTypeForHcf = Passed")
