from threading import Timer

def alert(event):
    from tkinter import Tk, messagebox 
    import inspect
    import os
    root = Tk()
    root.withdraw()
    filename =  os.path.basename(inspect.stack()[1].filename)
    messagebox.showinfo(f'{filename} says',event)  
    

def setTimeout(callback, time_in_ms, *args):
    t = Timer(time_in_ms/1000, callback, *args)
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
    
    t = RXTimer(time_in_ms/1000, callback, *args)
    # t.setDaemon(True)  
    t.start()
    return t

def clearInterval(*intervals):
    for interval in intervals:
        interval.cancel()


