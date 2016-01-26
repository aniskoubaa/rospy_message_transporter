class Client( object ):
    
    def __init__(self,name,target_ip,target_port,message_formatter):
        self.name = name 
        self.target_ip = target_ip
        self.target_port = target_port
        self.message_formatter = message_formatter

    def send(self,message,wait_response=False):
        raise NotImplementedError( "Should have implemented this" )
    
    