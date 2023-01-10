# README By Massimo Aureli RT221

---

# Installation process

These procedures are really important to go step by step. Do not skip to another part or else the project won't work.

Requirements 

- Python3
- Pyqt5
- Pandas
    
This command would install the requirements on most machines for sure.

    apt install python3 
    pip install Pyqt5
    pip install pandas 

/Launching the Server

    python3 main_window.py

/Launching the Client

    python3 client.py

I haven't tested this on a Mac OSX machine. I don't have any Mac, but I'm confident that the command above should work. It's a Linux-based system, so it should be somewhat compatible with other Linux systems.

1. The first step would be to press the connect button once a green button would appear this mean that the server started and is awaiting an import

![Untitled](README%20bc32bc2670d8454d9bcd135ad167f5d1/Untitled.png)


2. Launch the [client.py](http://client.py) on a local machine 

![Untitled](README%20bc32bc2670d8454d9bcd135ad167f5d1/Untitled%201.png)

3. Import the [test.](http://test.py)json that’s been modified to the [server.py](http://server.py) 

4. On the server, select the client you wish to connect to. Once selected, it is already connected; no need to press "connect" again.

You are able to send commands such as os , ip , users , help, clear , quit

For the moment, the public connection between client and server is available only if you port forward. I've tried it, and it does work. Testing on a local machine will work, too you won't need any port forwarding.

Regards 

Thanks for reading and analyzing my project. If there are any problems or issues, do not hesitate to contact me, I'll answer as soon as possible.

I wish you a happy new year, with best wishes. 🥂
