from utils import Utils

class AttributeInfo:
    def __init__(self, attributeNameIndex, attributeLen, infos):
        # u2
        self.attributeNameIndex = attributeNameIndex
        # u4
        self.attributeLen = attributeLen
        # u1[len]
        self.infos = infos

    def printString(self):
        print("attributeNameIndex:{}, attributeLen: {}, info: {}".format(self.attributeNameIndex, self.attributeLen, self.infos))
    def __str__(self):
        return self.attributeNameIndex + ", " + self.attributeLen + ", " + self.infos