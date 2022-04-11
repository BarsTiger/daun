prep, parsers, functions = dict(), dict(), dict()

with open("daun.py", 'r') as f:
    daun_code = f.readlines()

i = 0
while i < len(daun_code):
    if daun_code[i][-2:-5:-1] == '///':
        line = daun_code[i].replace('///', '').replace('\n', '').replace('#', '').strip()
        i += 1
        add_this = str()
        while i < len(daun_code) and daun_code[i][-2:-5:-1] != '///':
            add_this += daun_code[i]
            i += 1
        match line.split(' ')[0].count('-'):
            case 3:
                prep[line.replace('-', '').strip()] = add_this
            case 2:
                functions[line.replace('-', '').strip()] = \
                    [
                        add_this.split('"""')[1].strip(),
                        add_this.split('"""')[2]
                    ]
            case 1:
                parsers[line.replace('-', '').strip()] = add_this
