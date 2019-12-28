from constants import ACCESS_FLAG, ACCESS_FLAG_DESC


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
            result = datas.decode(encoding='utf8')
        return result

    @staticmethod
    def getAccessFlag(accessFlagBytes):
        i = 0
        accessFlagArray = []
        while i < len(ACCESS_FLAG):
            if ACCESS_FLAG[i] & accessFlagBytes > 0:
                accessFlagArray.append('ACC_' + ACCESS_FLAG_DESC[i])
            i += 1
        accessFlag = (','.join(accessFlagArray))
        return accessFlag