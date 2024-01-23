
import cmd
import os
import sys
import socket
import subprocess
import logging
import time
import threading
import json
import re
import shlex


import logging, coloredlogs
from datetime import datetime
from reloaded.kern import basis
from reloaded.farben import  *
from cmd import Cmd

HOST = "0.0.0.0"
PORT = 5333




class Main(basis.Module):
    """Socket Client"""



    parameters = {
        "host": "0.0.0.0",
        "port": "5333"
    }
    
    completions = list(parameters.keys())
    
  

    
    def complete_set(self, text, line, begidx, endidx):
        mline = line.partition(' ')[2]
        offs = len(mline) - len(text)
        return [s[offs:] for s in self.completions if s.startswith(mline)]
    
    
    def do_run(self, line):
        print('Running server...')
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((HOST, PORT))
        server.listen(5)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            incoming_client_socket, incoming_client_address = server.accept()
            print(f"Incomming connection from: {incoming_client_address[0]}:{incoming_client_address[1]}")
            
            while True:
                req = incoming_client_address = incoming_client_socket.recv(1024)
                req = req.decode("utf-8")
                
                if req.lower() == 'close':
                    print("Closing connection...")
                    incoming_client_socket.send("closed".encode("utf-8"))
                    break
                print(f"Received: {req}")
            
                res = "Accepted".encode("utf-8")
                
                incoming_client_socket.send(res)
            
            incoming_client_socket.close()
            server.close()
            
            print("Connection closed.")





    def complete_set(self, text, line, begidx, endidx):
        mline = line.partition(' ')[2]
        offs = len(mline) - len(text)
        return [s[offs:] for s in self.completions if s.startswith(mline)]