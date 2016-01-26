from rospy_message_transporter.Handler import Handler

class PublishingHandler( Handler ):

    def __init__(self,publishers_info):
    	self.pub_info = publishers_info

    def handle(self,ros_message, connection_info):
        pub = self.pub_info[ros_message.messageType]
        if pub is not None:
            pub.publish(ros_message)
        else:
            print "Message type unknown: " + ros_message.messageType
        return ros_message.messageType
