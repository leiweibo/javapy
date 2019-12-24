from utils import Utils
class MethodRefInfo:
    def __init__(self, order, tag, classIndex, nameAndTypeIndex):
        self.order = order
        self.tag = tag
        self.classIndex = classIndex
        self.nameAndTypeIndex = nameAndTypeIndex

    def setOrder(self, order):
        self.order = order

    def setTag(self, tag):
        self.tag = tag

    def setClassIndex(self, classIndex):
        self.classIndex = classIndex

    def setnameAndTypeIndex(self, nameAndTypeIndex):
        self.nameAndTypeIndex = nameAndTypeIndex

    def printString(self):
        print('#{} = Methodref              #{}.#{}'.format(self.order, self.classIndex, self.nameAndTypeIndex))
    
    @staticmethod
    def parseMethodInfo(order, tag, classIndexBytes, nameAndTypeIndexBytes):
        classIndex = Utils.formatDataByte(classIndexBytes, 'd')
        nameAndTypeIndex = Utils.formatDataByte(nameAndTypeIndexBytes, 'd')
        methodRefInfo = MethodRefInfo(order, tag, classIndex, nameAndTypeIndex)
        methodRefInfo.printString()