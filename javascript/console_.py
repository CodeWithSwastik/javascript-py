from .jstypes import Array
import time

ENDC = "\033[0m"


class Console:
    def __init__(self):
        self.timers = Array()

    def assert_(self, assertion, *data):
        if not data:
            data = ('console.assert',)
        try:
            assert assertion
        except AssertionError:
            print(f"\033[1;31;40mAssertion failed:", *data, ENDC)
            
    def log(self, *args, styles=None, **kwargs):
        if styles is None:
            print(*args, **kwargs)
        else:
            text_style = styles.get("font") or styles.get("text-style") or "1"
            color = styles.get("color") or styles.get("colour") or "30"
            bg_color = styles.get("bg-color") or styles.get("background-color") or "40"
            print(f"\033[{text_style};{color};{bg_color}m", *args, ENDC, **kwargs)

    def info(self, *messages):
        print(f"\033[1;32;40mINFO:", *messages, ENDC)

    def warn(self, *warnings):
        print(f"\033[1;33;40mWARNING:", *warnings, ENDC)

    def error(self, *errors):
        for err in errors:
            if isinstance(err, Exception):
                error_type = err.__class__.__name__
            else:
                error_type = "ERROR"
            print(f"\033[1;31;40m{error_type}:", err, ENDC)

    def clear(self, show_message=True):
        from os import name, system

        _ = system("cls" if name == "nt" else "clear")
        if show_message:
            print(f"\033[3;35;40mConsole was cleared", ENDC)

    def table(self, obj, headers=None):
        table = Table()
        if isinstance(obj, list):
            headers = headers or ["Index", "Value"]
            table.set_headers(headers)
            for x in enumerate(obj):
                table.add_row(x)
        elif isinstance(obj, dict):
            headers = headers or ["Key", "Value"]
            table.set_headers(headers)
            for x in obj.items():
                table.add_row(x)
        else:
            headers = headers or ["Attribute", "Value"]
            table.set_headers(headers)
            try:
                for x in obj.__dict__.items():
                    table.add_row(x)
            except AttributeError:
                table = obj

        print("\033[1;36;40m", table, ENDC, sep="")

    def time(self, label="default"):
        timer = self.timers.find(lambda x: x.label == label)
        if timer is not None:
            return self.warn(f"Timer '{label}' already exists")
        self.timers.push(Time(label))

    def timeLog(self, label="default"):
        timer = self.timers.find(lambda x: x.label == label)
        if timer is None:
            return self.warn(f"Timer '{label}' does not exist")
        timer.end = time.time()
        print(f"\033[1;37;40m{label}: {timer.timeElapsed} ms{ENDC}")

    def timeEnd(self, label="default"):
        timer = self.timers.find(lambda x: x.label == label)
        if timer is None:
            return self.warn(f"Timer '{label}' does not exist")
        timer.end = time.time()
        print(f"\033[1;37;40m{label}: {timer.timeElapsed} ms{ENDC}")
        self.timers = self.timers.filter(lambda x: x.label != label)


JUNC = "+"
VERT = "|"
HORIZ = "-"


class Table:
    def __init__(self, max_width = 50):
        self.rows = []
        self.max_width = max_width

    def set_headers(self, names):
        self.headers = names

    def add_row(self, row):
        frow = []
        for x in row:
            x = str(x).replace('\n','')
            if len(x) > self.max_width:
                frow.append(x[:self.max_width-3]+'...')
            else:
                frow.append(x)
        self.rows.append(frow)

    @property
    def length_of_cols(self):
        lengths = []
        for i, x in enumerate(self.headers):
            rows = [y[i] for y in (z for z in self.rows)] + [x]
            lengths.append(max(map(lambda x: len(str(x)), rows)))
        return list(map(lambda x: x + 2, lengths))

    def gen_row(self, index):
        f = VERT
        if index == -1:
            row = self.headers
        else:
            row = self.rows[index]
        for i, x in enumerate(row):
            length = self.length_of_cols
            cur = length[i]
            f += str(x).center(cur)
            f += VERT
        return f + "\n"

    def gen_sep(self):
        f = JUNC
        for x in self.length_of_cols:
            f += HORIZ * x
            f += JUNC
        return f + "\n"

    def __repr__(self):
        x = self.gen_sep()
        x += self.gen_row(-1)
        x += self.gen_sep()
        for i in range(len(self.rows)):
            x += self.gen_row(i)
        x += self.gen_sep()[:-1]
        return x


class Time:
    def __init__(self, label):
        self.label = label
        self.start = time.time()
        self.end = time.time()

    @property
    def timeElapsed(self):
        return round((self.end - self.start) * 1000, 4)

console = Console()
