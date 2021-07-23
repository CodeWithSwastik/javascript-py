from threading import Timer
import inspect, os
from tkinter import Tk, messagebox, simpledialog

filename = os.path.basename(inspect.stack()[-1].filename)
title = f"{filename} says..."


def alert(event):
    root = Tk()
    root.withdraw()
    messagebox.showinfo(title, event)
    root.destroy()


def confirm(question):
    root = Tk()
    root.withdraw()
    res = messagebox.askokcancel(title, question)
    root.destroy()
    return res


def prompt(text):
    root = Tk()
    root.withdraw()
    ans = simpledialog.askstring(title, text)
    root.destroy()
    return ans


def setTimeout(callback, time_in_ms, *args):
    t = Timer(time_in_ms / 1000, callback, *args)
    # t.setDaemon(True)
    t.start()
    return t


def clearTimeout(*timers):
    for timer in timers:
        timer.cancel()


def setInterval(callback, time_in_ms, *args):
    class RXTimer(Timer):
        def run(self):
            while not self.finished.is_set():
                self.finished.wait(self.interval)
                self.function(*self.args, **self.kwargs)

            self.finished.set()

    t = RXTimer(time_in_ms / 1000, callback, *args)
    # t.setDaemon(True)
    t.start()
    return t


def clearInterval(*intervals):
    for interval in intervals:
        interval.cancel()
