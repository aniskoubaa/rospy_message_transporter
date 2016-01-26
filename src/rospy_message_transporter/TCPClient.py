import socket

from rospy_message_transporter.Client import Client
from rospy_message_transporter.TCPSocketMaker import TCPSocketMaker

class TCPClient(Client):
    
    def __init__(self,name,target_ip,target_port,message_formatter,buffer_size=1024):
        Client.__init__(self, name,target_ip,target_port,message_formatter)
        self.buffer_size = buffer_size
    
    def _send(self,sock,message,wait_response=False):
        try :
            sock.connect((self.target_ip,self.target_port))
            sock.send(message+"\n")
            print self.name + ': Sent Message: ' + message
            date = None
            ros_msg = None
            if wait_response:
                data = sock.recv(self.buffer_size)
                ros_msg = self.message_formatter.format_to_ros_msg(data.replace("\'", '"'))
            sock.close()
            return ros_msg
        except socket.error, msg:
            print self.name + ': Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
            return None

    # Send a ros message
    def send(self,message,wait_response=False):
        sock = TCPSocketMaker.create_socket()
        msg = message 
        msg = self.message_formatter.format_from_ros_msg(message)
        return self._send(sock,msg,wait_response)




