import socket

from rospy_message_transporter.SocketMaker import SocketMaker

class UDPSocketMaker(SocketMaker):
        
    # Create datagram socket
    def create_socket(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            print 'UDPSocketMaker: Socket created'
            return s
        except socket.error:
            print 'UDPSocketMaker: Failed to create socket'
            return None
    create_socket = classmethod(create_socket)
