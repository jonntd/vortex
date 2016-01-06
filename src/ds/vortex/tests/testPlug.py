import unittest
from ds.vortex.core import plug as plugs


class TestPlug(unittest.TestCase):
    def setUp(self):
        self.plug = plugs.InputPlug(name="testName")

    def testIsInput(self):
        self.assertTrue(self.plug.isInput())
        self.assertFalse(self.plug.isOutput())

    def testConnect(self):
        inputAttr = plugs.InputPlug(name="testInput")
        outputAttr = plugs.OutputPlug(name="testOutput")
        floatTypeAttr = plugs.OutputPlug(name="testOutput")
        self.plug.connect(outputAttr)
        self.plug.connect(floatTypeAttr)
        self.assertTrue(self.plug.isConnected())
        #  failed to connect as plug already exists
        self.assertIsNone(self.plug.connect(inputAttr))

    def remove(self):
        floatTypeAttr = plugs.OutputPlug(name="testOutput")
        self.plug.connect(floatTypeAttr)
        self.plug.disconnect(floatTypeAttr)
        self.assertEquals(len(self.plug), 0)

    def testSerialize(self):
        pass


if __name__ == "__main__":
    import logging

    logger = logging.getLogger(__name__)
    logger.setLevel(level=logging.INFO)
    unittest.main(verbosity=2)
