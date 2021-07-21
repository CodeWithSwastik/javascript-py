ENDC = '\033[0m'
class Console:
    def log(self, *args, **kwargs):
        print(*args, **kwargs)

    def info(self, *messages):
        print(f"\033[1;32;40mINFO:",*messages,ENDC)

    def warn(self, *warnings):
        print(f"\033[1;33;40mWARNING:",*warnings,ENDC)

    def error(self, *errors):
        print(f"\033[1;31;40mERROR:",*errors, ENDC)

    def clear(self, show_message=True):
        from os import name, system
        _ = system('cls' if name == 'nt' else 'clear')
        if show_message:
            print(f"\033[3;35;40mConsole was cleared", ENDC)

    def table(self, obj):
        table = Table()
        if isinstance(obj,list):
            headers = ['Index', 'Value']
            table.set_headers(headers)
            for x in enumerate(obj):
                table.add_row(x)
        elif isinstance(obj,dict):
            headers = ['Key', 'Value']
            table.set_headers(headers)
            for x in obj.items():
                table.add_row(x)

        print("\033[1;36;40m",table, ENDC, sep='')

JUNC = "+"
VERT = "|"
HORIZ = "-"
class Table:
    def __init__(self):
        self.rows = []
    
    def set_headers(self, names):
        self.headers = names
        
    def add_row(self, row):
        self.rows.append(row)

    @property
    def length_of_cols(self):
        lengths = []
        for i,x in enumerate(self.headers):
            rows = [y[i] for y in (z for z in self.rows)]+[x]
            lengths.append(max(map(lambda x: len(str(x)), rows)))
        return list(map(lambda x: x+2, lengths))

    def gen_row(self, index):
        f = VERT
        if index == -1:
            row = self.headers
        else:
            row = self.rows[index]
        for i,x in enumerate(row):
            length = self.length_of_cols
            cur = length[i]
            a = divmod(cur - len(str(x)), 2)
            b = a[0]+a[1]
            a = a[0]
            f += " "*a + str(x) + " "*b
            f += VERT
        return f + '\n'
    
    def gen_sep(self):
        f = JUNC
        for x in self.length_of_cols:
            f += HORIZ * x
            f += JUNC
        return f + '\n'

    def __repr__(self):
        x = self.gen_sep()
        x += self.gen_row(-1)
        x += self.gen_sep()
        for i in range(len(self.rows)):
            x += self.gen_row(i) 
        x += self.gen_sep()
        return x
