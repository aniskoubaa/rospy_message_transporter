cmake_minimum_required(VERSION 2.8.3)
project(rospy_message_transporter)

find_package(catkin REQUIRED COMPONENTS
  message_generation
  rospy
  std_msgs
  rostest
  rospy_message_converter
)

# Generate messages for testing (NOINSTALL)
add_message_files(
  FILES HelloMessage.msg RegistrationRequestMessage.msg RegistrationResponseMessage.msg HeartbeatMessage.msg NOINSTALL
)

catkin_python_setup()

generate_messages()

catkin_package(
  CATKIN_DEPENDS message_runtime std_msgs 
)

# Test launch files
add_rostest(test/test_all.test)