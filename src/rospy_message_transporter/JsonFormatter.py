import ast
from importlib import import_module
from rospy_message_converter import json_message_converter
from rospy_message_transporter.Formatter import Formatter

class JsonFormatter( Formatter ):

    def __init__(self,message_type_attribute_name,message_types_info):
        self.msg_typ_attr_name = message_type_attribute_name
        self.msg_typ_info = message_types_info
        # import all the modules containing ros messagess
        for key in self.msg_typ_info:
            pkg = self.msg_typ_info[key]+".msg"  
            mod = import_module(pkg)

    def format_to_ros_msg(self,json_message):
        print "json_message" + json_message
        temp_dict = ast.literal_eval(json_message)
        if self.msg_typ_attr_name in temp_dict:
            ros_msg_type = temp_dict[self.msg_typ_attr_name]
        else: 
            print "JsonFormatter: message doesn't contains '" + self.msg_typ_attr_name +"' attribute"
            return None
        print 'JsonFormatter: message type ' + str(ros_msg_type)
        if ros_msg_type in self.msg_typ_info:
            print ' recognized'
            ros_msg_pkg = self.msg_typ_info[ros_msg_type]
            ros_msg = json_message_converter.convert_json_to_ros_message(ros_msg_pkg+'/'+ros_msg_type, json_message)
            return ros_msg
        else:
            print ' not recognized'
            return None
                       

    def format_from_ros_msg(self,ros_message):
        return json_message_converter.convert_ros_message_to_json(ros_message)
