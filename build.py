import sys
import subprocess
import unittest

from tests.models import *
from tests.controllers import *
from tests.RepositoryServices.KingdomRepositoryServices import *
from tests.services.SoutherosRulerServices import *
from tests.utils import *
"""
Test Adder Functions
"""


def addTestCipherFactory(test_suite):
    test_suite.addTests([
        TestCipherFactory.TestCipherFactory(
            'testReturnCaesarCipher'),
        TestCipherFactory.TestCipherFactory(
            'testEncryptPlainText'),
        TestCipherFactory.TestCipherFactory(
            'TestDecryptCipherText')
    ])


def addTestDataLoaderFactory(test_suite):
    test_suite.addTests([
        TestDataLoaderFactory.TestDataLoaderFactory(
            'testReturnCorrectDict')
    ])


def addTestKingdomRepositoryServiceFactory(test_suite):
    test_suite.addTests([
        TestKingdomRepositoryServiceFactory.
        TestKingdomRepositoryServiceFactory(
            'testReturnCsvService')
    ])


def addTestKingdomRepositoryCsvService(test_suite):
    test_suite.addTests([
        TestKingdomRepositoryCsvService.
        TestKingdomRepositoryCsvService('testReturnCorrectData')
    ])


def addTestKingdom(test_suite):
    test_suite.addTests([
        TestKingdom.TestKingdom('testCreateCorrectObject'),
        TestKingdom.TestKingdom(
            'testReturnAllyForCorrectResponse'),
        TestKingdom.TestKingdom(
            'testReceiveSupportFromKingdom'),
        TestKingdom.TestKingdom(
            'testEvaluateRightAllies'
        )
    ])


def addTestMessageFileReader(test_suite):
    test_suite.addTests([
        TestMessageFileReader.TestMessageFileReader(
            'testGenerateMessageDict'),
        TestMessageFileReader.TestMessageFileReader(
            'testRaiseIOError')
    ])


def addTestSoutherosRulerController(test_suite):
    test_suite.addTests([
        TestSoutherosRulerController.TestSoutherosRulerController(
            'testReturnAllies'),
        TestSoutherosRulerController.TestSoutherosRulerController(
            'testReturnNone')
    ])


def addTestSoutherosRulerByMessagesService(test_suite):
    test_suite.addTests([
        TestSoutherosRulerByMessagesService.
        TestSoutherosRulerByMessagesService('testReturnRuler'),
        TestSoutherosRulerByMessagesService.
        TestSoutherosRulerByMessagesService('testReturnNone')
    ])


def addTestSoutherosRulerServiceFactory(test_suite):
    test_suite.addTests([
        TestSoutherosRulerServiceFactory.TestSoutherosRulerServiceFactory(
            'testReturnMessagesService')
    ])


def addAllTestsToSuite(test_suite):
    """
    Add tests Module wise
    """
    addTestCipherFactory(test_suite)
    addTestDataLoaderFactory(test_suite)
    addTestKingdomRepositoryCsvService(test_suite)
    addTestKingdomRepositoryServiceFactory(test_suite)
    addTestKingdom(test_suite)
    addTestMessageFileReader(test_suite)
    addTestSoutherosRulerController(test_suite)
    addTestSoutherosRulerByMessagesService(test_suite)
    addTestSoutherosRulerServiceFactory(test_suite)


def runTestSuite():
    """
    - Create a Test Suite
    - Add all tests to the suite
    - Run the test suite
    - Return if test ran successfully
    """

    testRunner = unittest.TextTestRunner()
    testSuite = unittest.TestSuite()
    addAllTestsToSuite(testSuite)
    return testRunner.run(testSuite).wasSuccessful()


if __name__ == "__main__":
    """
    Run all the test and then run the comaand to run the program
    """

    inputFilePath = sys.argv[1]

    if runTestSuite():
        print("All tests ran successfully.")
        print('\nRunning Geektrust Program...')
        print('\nResult:')
        subprocess.run("py -m geektrust " + inputFilePath)