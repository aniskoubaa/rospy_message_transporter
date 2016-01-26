class Formatter( object ):

    def format_to_ros_msg(self,formatted_message):
        raise NotImplementedError( "Should have implemented this" )
    
    def format_from_ros_msg(self,ros_message):
        raise NotImplementedError( "Should have implemented this" )

