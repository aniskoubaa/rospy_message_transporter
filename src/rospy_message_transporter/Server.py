class Server( object ):
    
    def __init__(self,name,port,message_formatter,message_handler,buffer_size):
        self.name = name 
        self.port = port
        self.message_formatter = message_formatter
        self.message_handler = message_handler
        self.buffer_size = buffer_size

    def receive(self):
        raise NotImplementedError( "Should have implemented this" )
    
    def receive(self,wait_for):
        """
    	@type wait_for: int
        @param wait: The max number of messages to be received (0: unlimited). 
        """
        raise NotImplementedError( "Should have implemented this" )

