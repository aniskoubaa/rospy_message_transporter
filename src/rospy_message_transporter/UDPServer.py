from rospy_message_transporter.Server import Server
from rospy_message_transporter.UDPSocketMaker import UDPSocketMaker

class UDPServer( Server ):
    
    def __init__(self,name,port,message_formatter,message_handler,buffer_size=1024):
        Server.__init__(self,name,port,message_formatter,message_handler,buffer_size)
    
    def _bind(self):
        sock = UDPSocketMaker.create_socket()
        # Bind socket to local host and port
        try:
            sock.bind(('', self.port))
            print self.name + ': Socket bound'
            return sock
        except socket.error , msg:
            print self.name + ': Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
            return None

    def _listen(self,sock):   
        print self.name + ': Listening started on port' + str(self.port)
        while 1:
            d = sock.recvfrom(self.buffer_size)
            data = d[0]
            addr = d[1]
        
            if not data: 
                break
            
            print self.name + ': Message[' + addr[0] + ':' + str(addr[1]) + '] - ' + data.strip()
            ros_msg = message_formatter.format_to_ros_msg(data.replace("\'", '"'))
            self.message_handler.handle(ros_msg,addr[0])
        s.close()

    def receive(self):
        self._listen(self._bind())