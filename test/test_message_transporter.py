#!/usr/bin/env python
import unittest
import rospy
import rostest
from pprint import pprint
from rospy_message_transporter.SocketMaker import SocketMaker
from rospy_message_transporter.Formatter import Formatter
from rospy_message_transporter.Handler import Handler
from rospy_message_transporter.Client import Client
from rospy_message_transporter.Server import Server

class TestMessageTransporter(unittest.TestCase):

    def test_client_instanciation(self):
        expected_name = 'UAVClient'
        expected_ip = 'localhost'
        expected_port = 5555
        message_formatter = Formatter()
        client = Client(expected_name,expected_ip,expected_port,message_formatter)
        self.assertEqual(client.name, expected_name)
        self.assertEqual(client.target_ip, expected_ip)
        self.assertEqual(client.target_port, expected_port)
        self.assertTrue(client.message_formatter is not None and isinstance(client.message_formatter, Formatter) )

    def test_server_instanciation(self):
        expected_name = 'UAVServer'
        expected_port = 5555
        expected_size = 1024
        message_formatter = Formatter()
        message_handler = Handler()
        server = Server(expected_name,expected_port,message_formatter,message_handler,expected_size)
        self.assertEqual(server.name, expected_name)
        self.assertEqual(server.port, expected_port)
        self.assertEqual(server.buffer_size, expected_size)
        self.assertTrue(server.message_formatter is not None and isinstance(server.message_formatter, Formatter) )
        self.assertTrue(server.message_handler is not None and isinstance(server.message_handler, Handler) )
    
PKG = 'rospy_message_transporter'
NAME = 'rospy_message_transporter'
if __name__ == '__main__':
    rostest.unitrun(PKG, NAME, TestMessageTransporter)
