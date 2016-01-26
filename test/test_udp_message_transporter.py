#!/usr/bin/env python
import unittest
import rospy
import rostest
import logging
from pprint import pprint
from rospy_message_transporter.Formatter import Formatter
from rospy_message_transporter.JsonFormatter import JsonFormatter
from rospy_message_transporter.Handler import Handler
from rospy_message_transporter.UDPSocketMaker import UDPSocketMaker
from rospy_message_transporter.UDPClient import UDPClient
from rospy_message_transporter.UDPServer import UDPServer
from rospy_message_transporter.msg import HelloMessage

class TestUDPMessageTransporter(unittest.TestCase):

    def test_udp_socketmaker_create_socket(self):
        sock = UDPSocketMaker.create_socket()
        self.assertTrue(sock is not None)

    def test_udp_sender_instanciation(self):
        expected_name = 'UAVUdpSender'
        expected_ip = 'localhost'
        expected_port = 5555
        message_formatter = Formatter()
        client = UDPClient(expected_name,expected_ip,expected_port,message_formatter)
        self.assertEqual(client.name, expected_name)
        self.assertEqual(client.target_ip, expected_ip)
        self.assertEqual(client.target_port, expected_port)
        self.assertTrue(client.message_formatter is not None and  isinstance(client.message_formatter, Formatter) )

    def test_udp_client_send(self):
        expected_msg_typ_attr_name = 'messageType'
        msg_typ_info = {}
        msg_typ_info['HelloMessage'] = 'rospy_message_transporter'
        msg_typ_info['HeartbeatMessage'] = 'rospy_message_transporter'
        message_formatter = JsonFormatter(expected_msg_typ_attr_name,msg_typ_info)
        client = UDPClient('UAVUdpSender','localhost',6666,message_formatter)
        msg = HelloMessage()
        msg.msg_content = "Hello"
        self.assertTrue( client.send(msg) )

    def test_udp_server_instanciation(self):
        expected_name = 'UAVUdpReceiver'
        expected_port = 5555
        message_formatter = Formatter()
        message_handler = Handler()
        server = UDPServer(expected_name,expected_port,message_formatter,message_handler)
        self.assertEqual(server.name, expected_name)
        self.assertEqual(server.port, expected_port)
        self.assertTrue(server.message_formatter is not None and  isinstance(server.message_formatter, Formatter) )
        self.assertTrue(server.message_handler is not None and isinstance(server.message_handler, Handler) )


PKG = 'rospy_message_transporter'
NAME = 'rospy_message_transporter'
if __name__ == '__main__':
    rostest.unitrun(PKG, NAME, TestUDPMessageTransporter)
