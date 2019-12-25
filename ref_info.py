from utils import Utils


class CommonRefInfo:
    '''
    通用的refinfo, 包括：
    Methodref_Info
    Fieldref_Info
    '''
    def __init__(self, type, order, tag, classIndex, nameAndTypeIndex):
        self.order = order
        self.type = type
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
        print('#{} = {}              #{}.#{}'.format(self.order, self.type,
                                                     self.classIndex,
                                                     self.nameAndTypeIndex))

    @staticmethod
    def parseInfo(type, order, tag, classIndexBytes, nameAndTypeIndexBytes):
        classIndex = Utils.formatDataByte(classIndexBytes, 'd')
        nameAndTypeIndex = Utils.formatDataByte(nameAndTypeIndexBytes, 'd')
        methodRefInfo = CommonRefInfo(type, order, tag, classIndex,
                                      nameAndTypeIndex)
        methodRefInfo.printString()


class StringInfo:
    def __init__(self, type, order, tag, classIndex):
        self.order = order
        self.type = type
        self.tag = tag
        self.classIndex = classIndex

    def printString(self):
        print('#{} = {}              #{}'.format(self.order, self.type,
                                                 self.classIndex))

    @staticmethod
    def parseInfo(type, order, tag, classIndexBytes):
        classIndex = Utils.formatDataByte(classIndexBytes, 'd')
        stringRefInfo = StringInfo(type, order, tag, classIndex)
        stringRefInfo.printString()
