from constants import CLASS_ACCESS_FLAG, CLASS_ACCESS_FLAG_DESC, FIELD_ACCESS_FLAG, FIELD_ACCESS_FLAG_DESC


class Utils:
    @staticmethod
    def formatDataByte(datas, formatter):
        array = []
        if formatter != 's':
            for d in datas:
                array.append(format(d, formatter))
            result = ''.join(array)

        if formatter == 'x' or formatter == 'X':
            result = ''.join(['0X', result])
        elif formatter == 'd':
            result = int(result)
        elif formatter == 's':
            result = datas.decode(encoding='utf-8')
        return result

    @staticmethod
    def getClassAccessFlag(accessFlagBytes):
        i = 0
        accessFlagArray = []
        while i < len(CLASS_ACCESS_FLAG):
            if CLASS_ACCESS_FLAG[i] & accessFlagBytes > 0:
                accessFlagArray.append('ACC_' + CLASS_ACCESS_FLAG_DESC[i])
            i += 1
        accessFlag = (','.join(accessFlagArray))
        return accessFlag

    @staticmethod
    def getFieldAccessFlag(accessFlagBytes):
        i = 0
        accessFlagArray = []
        while i < len(FIELD_ACCESS_FLAG):
            if FIELD_ACCESS_FLAG[i] & accessFlagBytes > 0:
                accessFlagArray.append('ACC_' + FIELD_ACCESS_FLAG_DESC[i])
            i += 1
        accessFlag = (','.join(accessFlagArray))
        return accessFlag