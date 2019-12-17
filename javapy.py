import os
import click
import subprocess

def append(file, appendix):
    if file and not file.endswith(appendix):
        return file+appendix
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
    out_bytes = subprocess.check_output(['javap', '-v', 'javas/'+file])
    out_text = out_bytes.decode('utf-8')
    click.echo(out_text)
    # out_bytes = subprocess.check_output(['cd','javas'])
    # out_text = out_bytes.decode('utf-8')
    # click.echo(out_text)

cli.add_command(javac)
cli.add_command(java)
cli.add_command(javap)

if __name__ == '__main__':
    '''
    main函数，通过click添加startCrawl和startApi两个启动命令
    '''
    cli(obj={})
