class Utils:
    @staticmethod
    def formatDataByte(datas, formatter):
        array = []
        for d in datas:
            array.append(format(d, formatter)) 
        result = ''.join(array)

        if formatter == 'x' or formatter == 'X':
            result = ''.join(['0X', result])
        elif formatter == 'd':
            result =  int(result) 
        return result