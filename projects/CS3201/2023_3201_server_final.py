import time
import socketserver
import struct,os
from socketserver import *
from socketserver import BaseRequestHandler, TCPServer
import socket


SENDING_COOLDOWN = 0.3
BUFFER_SIZE = 4096


class EchoHandler(BaseRequestHandler):
    postSwitch = False
    content = ""
    error_str = 'ERROR - Command not understood'
    ok_str = 'OK'
    input_buffer=[]
    init_password='123456'

    def send_str(self, string):
        self.request.send(bytes('server: ' + string, encoding='utf-8'))
        time.sleep(SENDING_COOLDOWN)


    def recv_str(self):
        post_msg = self.request.recv(BUFFER_SIZE)
        return str(post_msg, encoding='utf-8')

    def handle(self):
        print('Got connection from', self.client_address)
        while True:
            msg = self.request.recv(BUFFER_SIZE)
            if not msg:
                break
            msg_str = str(msg, encoding='utf-8')
            print('msg_str is :', msg_str)

            msg_pieces = msg_str.split()
            
            if len(msg_pieces) >= 2:  
                self.send_str(self.error_str)
            elif len(msg_pieces) == 1:
                command = msg_pieces[0]
                print('command is :', command)
                if command in ['POST_STRING', 'POST_FILE', 'EXIT','GET']:
                    if command == 'POST_STRING':
                        in_post = True
                        while in_post:
                            post_msg_str = self.recv_str()
                            if post_msg_str[-1] == "&":
                                in_post = False
                                self.send_str(self.ok_str)
                            else:
                                print(f"added: {post_msg_str}")
                                self.content += "\n" + post_msg_str

                    elif command == 'POST_FILE':
                        
                        print("Client is posting file")
                        in_mail = True
                        file_define_size = struct.calcsize('128sl')	
                        self.send_str('please send your file and its path name')
                        file = self.request.recv(file_define_size)
                        if file == b"close":
                            in_mail = False
                            self.send_str("The file not exist")

                        while in_mail:
                            if file:															
                                file_name,file_size=struct.unpack('128sl',file)	
                                file_name=file_name.decode('utf8').strip('\00')			
                                print('The file size: ',file_size,'The file name: ',file_name)
                                # here you can change the path to save the file sent by client
                                file_new_name = os.path.join("d:\\",file_name)
                                print('The save path',file_new_name)
                                recvd_filesize = 0 													
                                files = open(file_new_name,"wb")								
                                print("RECEIVE...")
                                while not recvd_filesize == file_size:
                                    if file_size==0:
                                        break
                                    elif file_size - recvd_filesize > 10:
                                        rdata = self.request.recv(10)								 
                                        recvd_filesize += len(rdata)
                                        print(str(recvd_filesize)+"is passing")
                                    else:
                                        rdata = self.request.recv(file_size - recvd_filesize)	
                                        recvd_filesize = file_size 							
                                        print(str(recvd_filesize)+"padding")										
                                    files.write(rdata)
                                files.close()														
                                self.send_str("OK")
                                in_mail=False




                    elif command == 'GET':
                        # self.send_str('Welcome socket programming')
                        if self.content == '':
                            self.send_str('&')
                            continue
                        for line in self.content.strip().split("\n"):
                            self.send_str(f"{line}")
                        self.send_str('&')

                    elif command == 'EXIT':
                        self.send_str(self.ok_str)
                else:
                    self.send_str(self.error_str)
            elif len(msg_pieces) < 1:
                self.send_str(self.error_str)



if __name__ == '__main__':
    serv = TCPServer(('', 16011), EchoHandler)
    serv.serve_forever()
