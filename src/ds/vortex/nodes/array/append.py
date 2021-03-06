from ds.vortex.core import baseNode
from ds.vortex.core import plug as plugs


class ArrayAppend(baseNode.BaseNode):
    """Appends a passed object into a list
    plugs:
        value1: The list to append to.
        value2: The object to append
        output: the combined list
    """
    def __init__(self, name):
        """
        :param name: str, the name of the node
        """
        baseNode.BaseNode.__init__(self, name)

    def initialize(self):
        baseNode.BaseNode.initialize(self)
        self.outputPlug_ = plugs.OutputPlug("output", self)
        self.value1Plug_ = plugs.InputPlug("value1", self, value=[])
        self.value2Plug_ = plugs.InputPlug("value2", self, value="")

        self.addPlug(self.outputPlug_, clean=True)
        self.addPlug(self.value1Plug_, clean=True)
        self.addPlug(self.value2Plug_, clean=True)

        self.plugAffects(self.value1Plug_, self.outputPlug_)
        self.plugAffects(self.value2Plug_, self.outputPlug_)

    def compute(self, requestPlug):
        baseNode.BaseNode.compute(self, requestPlug=requestPlug)
        if requestPlug != self.outputPlug_:
            return None
        self.value1Plug_.value.append(self.value2Plug_.value)
        result = self.value1Plug_.value

        requestPlug.value = result
        requestPlug.dirty = False
        return result


def getNode():
    """General function that returns our node, used to get create our node via Ui etc
    :return: Node instance
    """
    return ArrayAppend
