#!/usr/bin/env python
import unittest
import rospy
import rostest
from pprint import pprint

from rospy_message_transporter.msg import HeartbeatMessage

from rospy_message_transporter.JsonFormatter import JsonFormatter


class TestMessageFormatter(unittest.TestCase):

    def test_json_formatter_instanciation(self):
        expected_msg_typ_attr_name = 'messageType'
        msg_typ_info = {}
        msg_typ_info['HelloMessage'] = 'rospy_message_transporter'
        msg_typ_info['HeartbeatMessage'] = 'rospy_message_transporter'
        message_formatter = JsonFormatter(expected_msg_typ_attr_name,msg_typ_info)
        self.assertEqual(message_formatter.msg_typ_attr_name, expected_msg_typ_attr_name)
        self.assertEqual(message_formatter.msg_typ_info, msg_typ_info)
    
    def test_json_format_from_ros_msg(self):
        msg_typ_info = {}
        msg_typ_info['HelloMessage'] = 'rospy_message_transporter'
        msg_typ_info['HeartbeatMessage'] = 'rospy_message_transporter'
        message_formatter = JsonFormatter('messageType',msg_typ_info)
        msg = HeartbeatMessage()
        msg.droneID = "UAV123"
        msg.sessionID = "SE123"
        msg.batteryLevel = 0.7
        msg.status = 0
        msg.latitude = 40
        msg.longitude = 40
        msg.altitude = 40
        json = message_formatter.format_from_ros_msg(msg)
        expected_json = '{"status": 0, "droneID": "UAV123", "altitude": 40, "longitude": 40, "sessionID": "SE123", "messageType": "", "latitude": 40, "batteryLevel": 0.7}'
        self.assertEqual(json, expected_json)

    def test_json_formatter_to_ros_msg(self):
        msg_typ_info = {}
        msg_typ_info['HelloMessage'] = 'rospy_message_transporter'
        msg_typ_info['HeartbeatMessage'] = 'rospy_message_transporter'
        message_formatter = JsonFormatter('messageType',msg_typ_info)
        json = '{"status": 0, "droneID": "UAV123", "altitude": 40, "longitude": 40, "sessionID": "SE123", "latitude": 40, "batteryLevel": 0.7, "messageType": "HeartbeatMessage"}'
        msg = message_formatter.format_to_ros_msg(json)
        expected_msg = HeartbeatMessage()
        expected_msg.droneID = "UAV123"
        expected_msg.sessionID = "SE123"
        expected_msg.batteryLevel = 0.7
        expected_msg.status = 0
        expected_msg.latitude = 40
        expected_msg.longitude = 40
        expected_msg.altitude = 40
        expected_msg.messageType = "HeartbeatMessage"
        self.assertEqual(msg, expected_msg)
        self.assertTrue(isinstance(msg, HeartbeatMessage))

PKG = 'rospy_message_transporter'
NAME = 'rospy_message_transporter'
if __name__ == '__main__':
    rostest.unitrun(PKG, NAME, TestMessageFormatter)
