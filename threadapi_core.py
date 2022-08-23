import queue
import threading



import dogui.dogui_core as dg

class GUI:
    def __init__(self,number):
        self.number=number    
    
        print("Generate",number)
        self.gui1=dg.GUI()
        self.label1=dg.Label(self.gui1.window,"Window "+str(number),1,1)
        button1=dg.Button(self.gui1.window, "Submit", self.print_to_console, 2, 1)
        button2=dg.Button(self.gui1.window, "Fill Queue", self.fill_queue, 3, 1)
        button3=dg.Button(self.gui1.window, "Read Queue", self.read_queue, 4, 1)
        self.entry1=dg.Entry(self.gui1.window,5,1)
        self.label2=dg.Label(self.gui1.window,"Queue",6,1)
        self.label3=dg.Label(self.gui1.window,g.time,8,1)
        
        button3=dg.Button(self.gui1.window, "Read Queue", self.destroy_gui, 7, 1)
        
        
        self.gui1.build_gui()
        
        print("GUI Generated",number)
        
    def print_to_console(self):
        print(self.number)
        print(threads)
        
        
    def fill_queue(self):
        lock.acquire()
        text=self.entry1.text.get()
        queue1.put(text)
        
        self.label2.text.set(str(queue1.queue))
       
        lock.release()
        
        
    def read_queue(self):
        lock.acquire()
        if not queue1.empty():
            data=queue1.get()
            self.label1.text.set(data)
            self.label2.text.set(str(queue1.queue))
        lock.release()
    
    
    def destroy_gui(self):
        global threads
        text=self.entry1.text.get()
        
        threads[int(text)].exit_flag=True
        
        self.gui1.window.destroy()
        



import os
import time




guis=[]


def run_file(file):
    os.system("python "+file)


def initialize_gui(args):
    global guis
    guis.append(GUI(args))
            
    
    
class G:
    def __init__(self):
        self.time=0
    
g=G()
    

def loop(args):
    global time
    for i in range(args):
       
        time.sleep(1)
        g.time+=1
        print(g.time)
        

class Thread(threading.Thread):
    def __init__(self,name,function,args):
        super().__init__()
        self.name=name
        self.exit_flag=False
        self.function=function
        self.args=args
        
    def run(self):
        print("Starting " + self.name)
        #if self.args==1:
        #    generate_gui1()
        #else:
            
        #generate_gui(self.args)
        
        while not self.exit_flag:
            self.function(self.args)
            
            time.sleep(0.5)
        print("Exiting " + self.name)
        
    def run_function(self,function):
        function()
        
        



print("Main Thread")

lock=threading.Lock()
queue1=queue.Queue()

import sys

#thread1=Thread("Thread-1",initialize_gui,1,queue1,lock)
#thread1.start()


#time.sleep(2)
#thread2=Thread("Thread-2",initialize_gui,2,queue1,lock)
#thread2.start()


def new_thread(name,function,function_args):
    global threads
    thread=Thread(name,function,function_args)
    threads.append(thread)
    thread.start()


threads=[]

new_thread("MonitoringThread-1",initialize_gui,1)
new_thread("TimeThread-2",loop,100)
new_thread("ApplicationThread-3",loop,100)

print(threads)

print("main thread flagged")

for thread in threads:
    thread.exit_flag=True
    thread.join()


print("Exiting Main Thread")

 