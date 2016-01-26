import rospy
from rospy_message_transporter.Server import Server
from rospy_message_transporter.TCPSocketMaker import TCPSocketMaker

class TCPServer( Server ):
    
    def __init__(self,name,port,message_formatter,message_handler,buffer_size=1024):
        Server.__init__(self,name,port,message_formatter,message_handler,buffer_size)
    
    def _bind(self):
        sock = TCPSocketMaker.create_socket()
        # Bind socket to local host and port
        try:
            sock.bind(('', self.port))
            print self.name + ': Socket bound'
            return sock
        except socket.error , msg:
            print self.name + ': Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
            return None

    def _listen(self,sock):   
        print self.name + ': Listening started on port ' + str(self.port)
        sock.listen(5)

        while not rospy.is_shutdown(): # TODO: should be implemented independantly of ros
            conn, addr = sock.accept()
            print self.name + ': Connection address: ', addr
            data = conn.recv(self.buffer_size)
            if not data: break
            print self.name + ": received data:", data
            ros_msg = self.message_formatter.format_to_ros_msg(data.replace("\'", '"'))
            
            if ros_msg != None:
                self.message_handler.handle(ros_msg,conn) #echo
            conn.close()

    def receive(self):
        self._listen(self._bind())
    



