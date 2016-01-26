from rospy_message_transporter.Client import Client
from rospy_message_transporter.UDPSocketMaker import UDPSocketMaker

class UDPClient(Client):
    
    def __init__(self,name,target_ip,target_port,message_formatter):
        Client.__init__(self, name,target_ip,target_port,message_formatter)
    
    def _send(self,sock,message):
        try :
            sock.sendto(message,(self.target_ip,self.target_port))
            print self.name + ': Sent Message: ' + message
            return True
        except socket.error, msg:
            print self.name + ': Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
            return False

    # Send a string message
    def send(self,message):
        sock = UDPSocketMaker.create_socket()
        msg = message 
        msg = self.message_formatter.format_from_ros_msg(message)
        return self._send(sock,msg)




