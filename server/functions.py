import socket
import threading
from PyQt5.QtGui import QPixmap,QIcon
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QSize
import platform
import os
connections = []
total_connections = 0
combo_box=None
text_sender=None
glob_socket=None
connections_names=[]
names_validation={}


class Client(threading.Thread):
    def __init__(self, socket, address, id, name, signal,label):
        threading.Thread.__init__(self)
        self.socket = socket
        self.address = address
        self.id = id
        self.name = name
        self.signal = signal
        self.label=label
    def __str__(self):
        return str(self.id) + " " + str(self.address)+" "+str(self.name)
    def run(self):
        while (self.signal==True):
            try:
                data = self.socket.recv(32)
            
            except:
                text="Client " + str(self.address) + " has disconnected"
                threading.Thread(target=add_label_text,args=(text,self.label,self.id)).start()
                self.signal = False
                break
            if data != "":
                text="ID " + str(self.id) + ": " + str(data.decode("utf-8"))                           
                if(self.name==''):
                    self.name=str(data.decode("utf-8"))
                    global connections_names
                    connections_names.append(self.name)
                threading.Thread(target=add_label_text,args=(text,self.label,self.id)).start()
  
def add_label_text(text,label,id):
      global combo_box
      global text_labels
      current_id=combo_box.currentText().split(" ")[0]
      try:
            if(int(id)==int(current_id)): 
                text_labels[combo_box.currentIndex()].append(text)
      except:pass

def update_text_labels(lab):
    global text_labels
    text_labels=lab
def add_client_to_combobox(client_name):
      combo_box.addItem(client_name)
def newConnections(socket,label):
    while True:
        sock, address = socket.accept()
        global total_connections
        connections.append(Client(sock, address, total_connections, '', True,label))
        connections[len(connections) - 1].start()
        total_connections += 1
        

def main(host1,port1,widgets):
    global glob_socket
    global text_sender
    host = host1
    port = port1
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, port))
    sock.listen(5)
    newConnectionsThread = threading.Thread(target = newConnections, args = (sock,widgets[0]))
    newConnectionsThread.start()
    change_state(True, widgets[1])
    global combo_box
    combo_box= widgets[2]
    glob_socket=sock
    text_sender=widgets[3]



def send_msg(s=None,id=None):
  try:
    global combo_box
    global text_sender
    
    if(id==None):
        s=text_sender.text()
        if(s==''):
            return

        txt=combo_box.currentText()
        k=str(txt).split(" ")[0]
        if(s=='help'):
            s=[]
            s.append("Welcome to the chat!")
            s.append("Type 'quit' to exit the chat room")
            s.append("Type 'clear' to clear the screen")
            s.append("Type 'help' to see the commands")
            s.append("Type 'users' to see the users in the chat room")
            s.append("Type 'os' to see the operating system of the machine")
            s.append("Type 'ip' to see the ip address of the machine")
            for i in s:
                threading.Thread(target=lambda :text_labels[combo_box.currentIndex()].append(i)).start()
            return
        if(s=='clear'):
            text_labels[combo_box.currentIndex()].clear()
        if(s=='users'):
            for i in connections_names:
                if(names_validation[i]==True):
                  threading.Thread(target=lambda :text_labels[combo_box.currentIndex()].append(i)).start()
            return
        if(s=='quit'):
            s='you got removed from chat room'
            
            
        for i in connections:
            if(str(i.id)==k):
             i.socket.sendall(str.encode(s))
        if(text_sender.text()=='quit'):
            connections[combo_box.currentIndex()-1].socket.close()
           
    else:
        for i in connections:
            if(str(i.id)==id):
             i.socket.sendall(str.encode(s))
  except:print('error')
def change_state(x,icon):
    if(x==True):
        pixmap = QPixmap('green_circle.png')
        pixmap=pixmap.scaled(QSize(25,25))
        icon.setPixmap(pixmap)
    
def show_info_messagebox(title,text):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
  
    # setting message for Message Box
    msg.setText(text)
      
    # setting Message box window title
    msg.setWindowTitle(title)
      
    # declaring buttons on Message Box
    msg.setStandardButtons(QMessageBox.Ok | QMessageBox.No)
      
    return msg

def remove():
  try:
    global text_labels
    global combo_box
    global names_validation
    global connections_names
    txt=combo_box.currentText()
    k=str(txt).split(" ")[0]
    name=str(txt).split(" ")[3]
    indx=combo_box.currentIndex()
    for i in connections:
            if(str(i.id)==k):
              i.socket.close()
              connections.remove(i)
    
    

    combo_box.removeItem(indx)
    text_labels[indx].hide()
    text_labels[indx].destroy()
    text_labels[indx-1].show()

    text_labels.remove(text_labels[indx])

    connections_names.remove(name)
    names_validation[name]=False
  except:pass
  

    


