import os

FILE_INPUT = os.path.join('input.txt')
FILE_OUTPUT = os.path.join('output.txt')
TEMPLATE = 'containerProvider.Resolve<{}>();'


def parse_file():
    print('--Start reading file ...')
    agrs = []
    
    with open(FILE_INPUT, 'r', encoding='utf8') as text_file:
        text = text_file.read()
        agrs = parse_args(' '.join(text.split()))

    print('--File readed')
    return agrs


def parse_args(constructor):
    raw_args = constructor.split(', ')
    agrs = []

    for arg in raw_args:
        typeArg = arg.split(' ')
        print(typeArg)
        agrs.append(typeArg[0])

    return agrs


def convert(interfaces):
    result = []
    with open(FILE_OUTPUT, 'w', encoding='utf8') as text_file:
        for intefcase in interfaces:
            result.append(TEMPLATE.format(intefcase))
        text_file.write(os.linesep.join(result))


def main():
    args = parse_file()
    convert(args)
    print('--Done')


if __name__ == '__main__':
    main()


