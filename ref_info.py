from utils import Utils


class CommonRefInfo:
    '''
    通用的refinfo, 包括：
    Methodref_Info
    Fieldref_Info
    NameAndType_Info
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


class CommonRefInfo1:
    '''
    String_RefInfo
    Class_Info
    '''
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
        stringRefInfo = CommonRefInfo1(type, order, tag, classIndex)
        stringRefInfo.printString()

class CommonRefInfo2(CommonRefInfo):
    def printString(self):
        print('#{} = {}              #{}:#{}'.format(self.order, self.type,
                                                     self.classIndex,
                                                     self.nameAndTypeIndex))

    @staticmethod
    def parseInfo(type, order, tag, classIndexBytes, nameAndTypeIndexBytes):
        classIndex = Utils.formatDataByte(classIndexBytes, 'd')
        nameAndTypeIndex = Utils.formatDataByte(nameAndTypeIndexBytes, 'd')
        methodRefInfo = CommonRefInfo2(type, order, tag, classIndex,
                                      nameAndTypeIndex)
        methodRefInfo.printString()

class Utf8Info:
    def __init__(self, type, order, tag, contentBytes):
        self.type = type
        self.order = order
        self.tag = tag
        self.contentBytes = contentBytes
    
    @staticmethod
    def parseInfo(type, order, tag, contentBytes):
        utf8Info = Utf8Info(type, order, tag, contentBytes)
        utf8Info.printString()

    def printString(self):
        content = Utils.formatDataByte(self.contentBytes, 's')
        print('#{} = {}              {}'.format(self.order, self.type, content))
