from utils import Utils


class FieldInfo:
    def __init__(self, accessFlag, nameIndex, descriptorIndex, attributeCount,
                 attributes):
        # u2
        self.accessFlag = accessFlag
        # u2
        self.nameIndex = nameIndex
        # u2
        self.descriptorIndex = descriptorIndex
        # u2
        self.attributeCount = attributeCount
        # Attribute[len]
        self.attributes = attributes

    def printString(self):
        print('............')

    @staticmethod
    def parseInfo(f):
        accessFlagBytes = f.read(2)
        accessFlag = Utils.formatDataByte(accessFlagBytes, 'd')
        nameIndexBytes = f.read(2)
        nameIndex = Utils.formatDataByte(nameIndexBytes, 'd')
        descriptoIndexBytes = f.read(2)
        descriptorIndex = Utils.formatDataByte(descriptoIndexBytes, 'd')
        attrCntBytes = f.read(2)
        attrCnt = Utils.formatDataByte(attrCntBytes, 'd')

        attrs = []
        for i in range(0, attrCnt):
            attributeNameIndex = Utils.formatDataByte(f.read(2), 'd')
            attributeLenBytes = f.read(4)
            attributeLen = Utils.formatDataByte(attributeLenBytes, 'd')

            infos = []
            for j in range(0, attributeLen):
                info = Utils.formatDataByte(f.read(1), 'd')
                infos.append(info)

            attribute = AttributeInfo(attributeNameIndex, attributeLen, infos)
            attrs.append(attribute)

        fieldInfo = FieldInfo(accessFlag, nameIndex, descriptorIndex, attrCnt,
                              attrs)
        fieldInfo.printString()
        return fieldInfo


class AttributeInfo:
    def __init__(self, attributeNameIndex, attributeLen, infos):
        # u2
        self.attributeNameIndex = attributeNameIndex
        # u4
        self.attributeLen = attributeLen
        # u1[len]
        self.infos = infos
