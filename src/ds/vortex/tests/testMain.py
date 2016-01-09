import unittest


def createTestSuites():
    tests = ["ds.vortex.tests.testEdge", "ds.vortex.tests.testGraph", "ds.vortex.tests.testBaseNodes",
             "ds.vortex.tests.testBasicMathNodes", "ds.vortex.tests.testPlug"]

    suites = [unittest.defaultTestLoader.loadTestsFromName(name) for name in tests]
    testSuite = unittest.TestSuite(suites)
    return testSuite


if __name__ == "__main__":
    from ds.vortex import customLogger

    logger = customLogger.getCustomLogger()
    unittest.main(verbosity=2)
    unittest.TextTestRunner(verbosity=2).run(createTestSuites())
