ENDC = '\033[0m'
class Console:
    info = print
    log = print

    def warn(self, *warnings):
        print(f"\033[1;33;40mWARNING:",*warnings,ENDC)

    def error(self, *errors):
        print(f"\033[1;31;40mERROR:",*errors, ENDC)

    def clear(self, show_message=True):
        from os import name, system
        _ = system('cls' if name == 'nt' else 'clear')
        if show_message:
            print(f"\033[3;35;40mConsole was cleared", ENDC)
