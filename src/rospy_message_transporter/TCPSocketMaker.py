import socket

from rospy_message_transporter.SocketMaker import SocketMaker

class TCPSocketMaker(SocketMaker):
        
    # Create stream socket
    def create_socket(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            print 'TCPSocketMaker: Socket created'
            return s
        except socket.error:
            print 'TCPSocketMaker: Failed to create socket'
            return None
    create_socket = classmethod(create_socket)
