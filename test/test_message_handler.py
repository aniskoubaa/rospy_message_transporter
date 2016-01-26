#!/usr/bin/env python
import unittest
import rospy
import rostest
from pprint import pprint

from rospy_message_transporter.msg import HelloMessage
from rospy_message_transporter.msg import HeartbeatMessage
from rospy_message_transporter.PublishingHandler import PublishingHandler


class TestMessageHandler(unittest.TestCase):

    def test_publishing_handler_instanciation(self):
        try:
            expected_pub_info = {}
            expected_pub_info['HelloMessage'] = rospy.Publisher('listen_json', HelloMessage, queue_size=10)
            expected_pub_info['HeartbeatMessage'] = rospy.Publisher('listen_json', HeartbeatMessage, queue_size=10)
            pub_handler = PublishingHandler(expected_pub_info)
            self.assertEqual(pub_handler.pub_info, expected_pub_info) #@TODO: a more advanced test should be conducted
        except rospy.ROSInterruptException:
            pass

    def test_publishing_handler_handle(self):
        try:
            pub_info = {}
            pub_info['HelloMessage'] = rospy.Publisher('Hello_Topic', HelloMessage, queue_size=10)
            pub_info['HeartbeatMessage'] = rospy.Publisher('Heartbeat_Topic', HeartbeatMessage, queue_size=10)
            pub_handler = PublishingHandler(pub_info)
            expected_msg = HeartbeatMessage()
            expected_msg.droneID = "UAV123"
            expected_msg.sessionID = "SE123"
            expected_msg.batteryLevel = 0.7
            expected_msg.status = 0
            expected_msg.latitude = 40
            expected_msg.longitude = 40
            expected_msg.altitude = 40
            expected_msg.messageType = "HeartbeatMessage"
            self.assertEqual(pub_handler.handle(expected_msg),"HeartbeatMessage")
        except rospy.ROSInterruptException:
            pass

PKG = 'rospy_message_transporter'
NAME = 'rospy_message_transporter'
if __name__ == '__main__':
    rospy.init_node('TestMessageHandler', anonymous=True)
    rostest.unitrun(PKG, NAME, TestMessageHandler)
    
