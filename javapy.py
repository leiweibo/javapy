import os
import click
import subprocess


def append(file, appendix):
    if file and not file.endswith(appendix):
        return file + appendix
    return file


@click.group()
@click.option('--file')
@click.pass_context
def cli(ctx, file):
    # ensure that ctx.obj exists and is a dict (in case `cli()` is called
    # by means other than the `if` block below
    ctx.ensure_object(dict)

    ctx.obj['file'] = file


@click.command()
@click.pass_context
def javac(ctx):
    '''
    执行javac指令，如果路径中没有java后缀，那么添加上java后缀
    @param ctx: 用来存储传递参数
    '''
    file = ctx.obj['file']
    file = append(file, ".java")
    res = os.popen('cd javas; javac {}'.format(file))
    if not res or (len(res.read()) == 0):
        click.echo('执行javac成功')


@click.command()
def java():
    click.echo('execute java')


@click.command()
@click.pass_context
def javap(ctx):
    '''
    执行javap指令，如果路径中没有java后缀，那么添加上class后缀
    @param ctx: 用来存储传递参数
    '''
    file = ctx.obj['file']
    file = append(file, ".class")
    subprocess.Popen('cd', shell=True, stdout=subprocess.PIPE, cwd='javas')
    out_bytes = subprocess.check_output(['javap', '-v', 'javas/' + file])
    out_text = out_bytes.decode('utf-8')
    click.echo(out_text)
    # out_bytes = subprocess.check_output(['cd','javas'])
    # out_text = out_bytes.decode('utf-8')
    # click.echo(out_text)


cli.add_command(javac)
cli.add_command(java)
cli.add_command(javap)

from ref_info import CommonRefInfo, CommonRefInfo1, CommonRefInfo2, Utf8Info
from field_info import FieldInfo
from method_info import MethodInfo
from utils import Utils


def readClass():
    file = 'javas/Main.class'
    switchers = {
        12: parseNameAndType,
        10: parseMethodInfo,
        9: parseFieldInfo,
        8: parseStringInfo,
        7: parseClassInfo,
        1: parseUtf8Info
    }
    with open(file, 'rb') as f:
        data = f.read(4)
        parseData(data, 'magic number', 'X')

        data = f.read(2)
        parseData(data, 'mini version', 'd')

        data = f.read(2)
        parseData(data, 'major version', 'd')

        data = f.read(2)
        constantPoolCount = parseData(
            data,
            'constant pool count(final result should be the shown value - 1)',
            'd')
        constantPoolCount = int(constantPoolCount)
        constantPools = []
        for i in range(1, constantPoolCount):
            tag = Utils.formatDataByte(f.read(1), 'd')
            constantPool = executeMethod(str(i), tag, switchers, f)
            constantPools.append(constantPool)
        print()
        accessFlagBytes = Utils.formatDataByte(f.read(2), 'd')
        accessFlag = Utils.getClassAccessFlag(accessFlagBytes)
        print('Class Access Flags:           ' + accessFlag)

        parseClassType('this class', f, constantPools)
        parseClassType('supper class', f, constantPools)

        print()
        interfaceCnt = Utils.formatDataByte(f.read(2), 'd')
        print('interface count:         ' + str(interfaceCnt))
        for i in range(1, 1 + interfaceCnt):
            interfaceIndex = Utils.formatDataByte(f.read(2), 'd') - 1
            finalInterfaceIndex = getattr(constantPools[interfaceIndex],
                                          'classIndex') - 1

            print('Interface #{}:            {}'.format(
                i, str(constantPools[finalInterfaceIndex].getContent())))

        print()
        fieldCount = Utils.formatDataByte(f.read(2), 'd')
        print('field count:             ' + str(fieldCount))
        for i in range(0, fieldCount):
            FieldInfo.parseInfo(f)

        print()
        methodCount = Utils.formatDataByte(f.read(2), 'd')
        print(f'method count is : {methodCount}')

        for i in range(0, methodCount):
            MethodInfo.parseInfo(f)


def parseClassType(classTypeStr, f, constantPools):
    '''
    解析this class 和 super class 类型
    '''
    thisClassBytes = f.read(2)
    # 获取的位置跟数组里面的为止要进行 - 1操作
    indexOfClass = Utils.formatDataByte(thisClassBytes, 'd') - 1
    try:
        relatedIndexOfClass = getattr(constantPools[indexOfClass],
                                      'classIndex')
    except:
        print('get exception when get the relatedIndexOfClass')
    thisClass = constantPools[relatedIndexOfClass]
    if isinstance(thisClass, Utf8Info):
        print('{}:              {}'.format(classTypeStr,
                                           thisClass.getContent()))


def parseMethodInfo(order, tag, classIndexBytes, nameAndTypeIndexBytes):
    '''
    方法信息
    '''
    return parseInfo("MethodRef", order, tag, classIndexBytes,
                     nameAndTypeIndexBytes)


def parseFieldInfo(order, tag, classIndexBytes, nameAndTypeIndexBytes):
    '''
    变量信息
    '''
    return parseInfo("FieldRef", order, tag, classIndexBytes,
                     nameAndTypeIndexBytes)


def parseStringInfo(order, tag, classIndexBytes):
    '''
    字符串信息
    '''
    return CommonRefInfo1.parseInfo("String", order, tag, classIndexBytes)


def parseClassInfo(order, tag, classIndexBytes):
    '''
    Class信息
    '''
    return CommonRefInfo1.parseInfo("Class", order, tag, classIndexBytes)


def parseInfo(type, order, tag, classIndexBytes, nameAndTypeIndexBytes):
    '''
    方法信息
    '''
    return CommonRefInfo.parseInfo(type, order, tag, classIndexBytes,
                                   nameAndTypeIndexBytes)


def parseUtf8Info(order, tag, contentBytes):
    '''
    utf-8 信息
    '''
    return Utf8Info.parseInfo("Utf8", order, tag, contentBytes)


def parseNameAndType(order, tag, classIndexBytes, nameAndTypeIndexBytes):
    '''
    解析 NameAndType信息
    '''
    return CommonRefInfo2.parseInfo("NameAndType", order, tag, classIndexBytes,
                                    nameAndTypeIndexBytes)


def executeMethod(order, tag, switchers, f):
    if tag == 12 or tag == 10 or tag == 9:
        nameIndexBytes = f.read(2)
        nameAndTypeIndexBytes = f.read(2)
    elif tag == 8 or tag == 7:
        nameIndexBytes = f.read(2)
        nameAndTypeIndexBytes = None
    elif tag == 1:
        length = Utils.formatDataByte(f.read(2), 'd')
        nameIndexBytes = f.read(length)
        nameAndTypeIndexBytes = None

    if nameIndexBytes == None and nameAndTypeIndexBytes == None:
        pass

    method = switchers.get(tag)

    if method:
        if nameAndTypeIndexBytes:
            return method(order, tag, nameIndexBytes, nameAndTypeIndexBytes)
        else:
            return method(order, tag, nameIndexBytes)


def parseData(datas, desc, formatter):
    '''
    根据指定的格式解析指定的data
    datas: 字节数组
    formatter: X -> 16 进制，并且大写
               x -> 16 进制，并且小写
    desc: 输出内容的描述
    '''
    result = Utils.formatDataByte(datas, formatter)
    print('the {} is: {}'.format(desc, result))
    return result


if __name__ == '__main__':
    readClass()
    '''
    main函数，通过click添加startCrawl和startApi两个启动命令
    '''
    # cli(obj={})
